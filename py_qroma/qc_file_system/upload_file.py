import asyncio

from py_qroma.qc_file_system import qfs_message_factory
from py_qroma.qroma_comm import utils

import base64
import zlib
import time
import aioserial

from py_qroma.test_resources.dev_settings import QROMA_ACTIVE_COM_PORT, TEST_FILE


class UploadEvents:
    rx_ready: asyncio.Event = asyncio.Event()

    init_sent: asyncio.Event = asyncio.Event()
    ack_received: asyncio.Event = asyncio.Event()

    file_sent: asyncio.Event = asyncio.Event()
    upload_complete_received: asyncio.Event = asyncio.Event()


class UploadRateParameters:
    num_bytes_per_chunk: int
    delay_between_chunks: float


def create_default_upload_rate_parameters() -> UploadRateParameters:
    upload_rate_parameters = UploadRateParameters()
    upload_rate_parameters.num_bytes_per_chunk = 100
    upload_rate_parameters.delay_between_chunks = 0.1
    return upload_rate_parameters


class UploadFileDetails:
    upload_path: str
    expected_crc: int
    file_bytes: bytes


def create_upload_file_details_from_local_file(file_name, upload_path) -> UploadFileDetails:
    upload_file_details = UploadFileDetails()
    with open(file_name, "rb") as f:
        upload_file_details.file_bytes = bytearray(f.read())
        upload_file_details.expected_crc = zlib.crc32(upload_file_details.file_bytes)
        upload_file_details.upload_path = upload_path
        return upload_file_details


def create_upload_file_details_from_bytes(file_bytes, upload_path) -> UploadFileDetails:
    upload_file_details = UploadFileDetails()
    upload_file_details.file_bytes = file_bytes
    upload_file_details.expected_crc = zlib.crc32(file_bytes)
    upload_file_details.upload_path = upload_path
    return upload_file_details


class UploadDetails:
    events: UploadEvents
    file_details: UploadFileDetails
    serial: aioserial.AioSerial
    file_stream_id: str
    upload_rate_parameters: UploadRateParameters

    def __init__(self):
        self.events = UploadEvents()
        self.upload_ack_response = None
        self.upload_complete_response = None
        self.upload_rate_parameters = create_default_upload_rate_parameters()


async def upload_file_script(upload_details: UploadDetails):
    upload_events = upload_details.events
    serial = upload_details.serial

    await upload_events.rx_ready.wait()

    msg_bytes = qfs_message_factory.create_stream_file_contents_bytes(
        upload_details.file_details.upload_path,
        len(upload_details.file_details.file_bytes),
        upload_details.file_details.expected_crc,
        upload_details.file_stream_id
    )
    b64_msg_bytes = base64.b64encode(msg_bytes) + b"\n"

    await serial.write_async(b64_msg_bytes)

    await upload_events.ack_received.wait()
    print("FILE STREAM ACK RECEIVED")
    print(upload_details.upload_ack_response)

    print("STARTING UPLOAD")
    file_bytes = upload_details.file_details.file_bytes

    bytes_to_send = file_bytes[:]
    send_count = upload_details.upload_rate_parameters.num_bytes_per_chunk
    sleep_duration = upload_details.upload_rate_parameters.delay_between_chunks

    bytes_sent_count = 0

    while len(bytes_to_send) > send_count:
        the_bytes = bytes_to_send[0:send_count]
        bytes_to_send = bytes_to_send[send_count:]
        print(f"SENDING {len(the_bytes)} BYTES")
        await serial.write_async(the_bytes)
        await asyncio.sleep(sleep_duration)

        bytes_sent_count += len(the_bytes)

    print(f"SENDING {len(bytes_to_send)} BYTES")
    await serial.write_async(bytes_to_send)
    bytes_sent_count += len(bytes_to_send)

    print(f"SENT {bytes_sent_count} TOTAL BYTES")

    upload_events.file_sent.set()

    print("FILE BYTES SENT - WAITING FOR RESPONSE")
    await upload_events.upload_complete_received.wait()

    print("UPLOAD COMPLETE")
    print(upload_details.upload_complete_response)


async def monitor_for_messages(upload_details: UploadDetails):
    print("STARTING MONITOR")

    upload_events = upload_details.events
    serial = upload_details.serial

    read_buffer = bytearray()

    while not (upload_events.ack_received.is_set() and
               upload_events.upload_complete_received.is_set()):
    # while True:
        upload_events.rx_ready.set()
        data: bytes = await serial.read_async()
        read_buffer.extend(data)
        qc_response, read_buffer = utils.process_buffer_for_qc_response(read_buffer)
        if qc_response:
            print(f"HAS QC RESPONSE: {qc_response}")
            if qc_response.HasField('streamResponse') and \
                    qc_response.streamResponse.HasField('initWriteFileStreamAckResponse'):
                upload_details.upload_ack_response = qc_response.streamResponse.initWriteFileStreamAckResponse
                upload_events.ack_received.set()

            if qc_response.HasField('streamResponse') and \
                    qc_response.streamResponse.HasField('writeFileStreamCompleteResponse'):
                upload_details.upload_complete_response = qc_response.streamResponse.writeFileStreamCompleteResponse
                upload_events.upload_complete_received.set()


async def do_upload(upload_details: UploadDetails):
    await asyncio.gather(
        upload_file_script(upload_details),
        monitor_for_messages(upload_details),
    )

    upload_complete_response = upload_details.upload_complete_response

    print("UPLOAD COMPLETE")
    print(upload_complete_response)

    return upload_complete_response


if __name__ == "__main__":
    FILE_STREAM_ID = int(time.time())
    UPLOAD_PATH = f"/upload_{FILE_STREAM_ID}.txt"

    uploadFileDetails: UploadFileDetails = create_upload_file_details_from_local_file(TEST_FILE, UPLOAD_PATH)

    aioserialInstance: aioserial.AioSerial = aioserial.AioSerial(
        port=QROMA_ACTIVE_COM_PORT,
        baudrate=115200,
    )

    uploadDetails = UploadDetails()
    uploadDetails.file_details = uploadFileDetails
    uploadDetails.serial = aioserialInstance
    uploadDetails.file_stream_id = FILE_STREAM_ID

    asyncio.run(do_upload(uploadDetails))
