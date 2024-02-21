import asyncio
from py_qroma.qroma_comm.qcio_serial import QcioSerial
from settings import QROMA_ACTIVE_COM_PORT

from py_qroma.qroma_comm_proto import qroma_comm_pb2
from py_qroma.qroma_comm_proto import qroma_types_pb2
from py_qroma.qroma_comm_proto import file_system_commands_pb2
from py_qroma.qroma_comm_proto import qroma_streams_pb2

import base64
import zlib


def create_stream_file_contents_bytes(file_path, file_bytes, file_stream_id, checksum):
    file_data = qroma_types_pb2.FileData()
    file_data.filename = file_path
    file_data.filesize = len(file_bytes)
    file_data.checksum = checksum

    write_stream_command = qroma_streams_pb2.InitWriteFileStreamCommand()
    write_stream_command.fileStreamId = file_stream_id
    write_stream_command.fileData.CopyFrom(file_data)

    qs_command = qroma_streams_pb2.QromaStreamCommand()
    qs_command.initWriteFileStreamCommand.CopyFrom(write_stream_command)

    qroma_message = qroma_comm_pb2.QromaCommCommand()
    qroma_message.streamCommand.CopyFrom(qs_command)

    print(qroma_message)

    msg_bytes = qroma_message.SerializeToString()
    return msg_bytes


async def do_send(com_port, msg_bytes, file_bytes, send_count, sleep_duration):
    qcio = QcioSerial(com_port)
    asyncio.create_task(qcio.run())

    await qcio.is_ready()

    print("DO SEND READY")

    msg_bytes_b64 = base64.b64encode(msg_bytes) + b'\n'
    await qcio.send_bytes(msg_bytes_b64)

    bytes_to_send = file_bytes[:]
    print(f"TO SEND: {len(bytes_to_send)} BYTES")
    while len(bytes_to_send) > send_count:
        the_bytes = bytes_to_send[0:send_count]
        await qcio.send_bytes(the_bytes)
        bytes_to_send = bytes_to_send[send_count:]
        print("SLEEP")

        data = await qcio.read_bytes_until_timeout(sleep_duration)
        # await asyncio.sleep(sleep_duration)

        # print(f"LINE RECEIVED: {data}")
        text = data.decode('utf-8')
        lines = text.splitlines()
        print("")
        for l in lines:
            print(l)
        print("")

    if len(bytes_to_send) > 0:
        await qcio.send_bytes(bytes_to_send)

    final_data = await qcio.read_bytes_until_timeout(2.0)
    text = final_data.decode('utf-8')
    lines = text.splitlines()
    print("")
    for l in lines:
        print(l)
    # print(final_data)


if __name__ == "__main__":
    TEST_INDEX = 29

    send_count = 9000
    sleep_duration = 0.05
    char_count = 1265

    FILE_BYTES = b's' + b'-' * char_count + b'xe'
    FILE_PATH = f"/cc-{char_count}-sc-{send_count}-sd-{sleep_duration}.bytes"
    FILE_STREAM_ID = 1000 + TEST_INDEX
    print(len(FILE_BYTES))

    checksum = zlib.crc32(FILE_BYTES)
    fs_msg_bytes = create_stream_file_contents_bytes(FILE_PATH, FILE_BYTES, FILE_STREAM_ID, checksum)

    asyncio.run(do_send(QROMA_ACTIVE_COM_PORT, fs_msg_bytes, FILE_BYTES, send_count, sleep_duration))

    print(FILE_PATH)
    print(len(FILE_BYTES))
    print(checksum)
