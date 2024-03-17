import asyncio
import aioserial

from py_qroma.qc_file_system import qfs_message_factory
from py_qroma.qroma_comm import utils, qc_message_factory

import base64

from py_qroma.test_resources.dev_settings import QROMA_ACTIVE_COM_PORT

#
# class IoEvents:
#     rx_ready: asyncio.Event = asyncio.Event()
#
#     request_sent: asyncio.Event = asyncio.Event()
#     response_received: asyncio.Event = asyncio.Event()
#
#     response = None
#
#     def __init__(self, file_path):
#         self.file_path = file_path
#
#
# async def run_script(io_events: IoEvents, serial: aioserial.AioSerial):
#
#     await io_events.rx_ready.wait()
#
#     msg_bytes = qfs_message_factory.create_get_report_filedata_bytes(io_events.file_path)
#     b64_msg_bytes = base64.b64encode(msg_bytes) + b"\n"
#
#     await serial.write_async(b64_msg_bytes)
#
#     print("GET FILE DATA REQUEST SENT")
#
#     await io_events.response_received.wait()
#
#     print("RESPONSE RECEIVED")
#     print("--------------")
#     print(io_events.response)
#     print("--------------")
#
#
# async def monitor_for_messages(io_events: IoEvents, serial: aioserial.AioSerial):
#     print("STARTING MONITOR")
#
#     read_buffer = bytearray()
#
#     while not io_events.response_received.is_set():
#         io_events.rx_ready.set()
#         data: bytes = await serial.read_async()
#         read_buffer.extend(data)
#         qc_response, read_buffer = utils.process_buffer_for_qc_response(read_buffer)
#         if qc_response:
#             if qc_response.HasField('fsResponse') and \
#                     qc_response.fsResponse.HasField('reportFileDataResponse'):
#                 io_events.response = qc_response
#                 io_events.response_received.set()


async def reset_device(aioserial_instance: aioserial.AioSerial):
    msg_bytes = qc_message_factory.create_get_reset_device_command_bytes()
    b64_msg_bytes = base64.b64encode(msg_bytes) + b"\n"

    await aioserial_instance.write_async(b64_msg_bytes)


if __name__ == "__main__":
    aioserialInstance: aioserial.AioSerial = aioserial.AioSerial(
        port=QROMA_ACTIVE_COM_PORT,
        baudrate=115200,
    )

    asyncio.run(reset_device(aioserialInstance))
