import asyncio
import base64
import aioserial
from ..qroma_comm_proto import qroma_comm_pb2


def process_buffer_for_qc_response(buffer_contents: bytes) -> (qroma_comm_pb2.QromaCommResponse, bytes):
    qc_response = qroma_comm_pb2.QromaCommResponse()

    while b"\n" in buffer_contents:
        to_process, buffer_contents = buffer_contents.split(b"\n", 1)
        to_process = to_process.strip()

        try:
            b = base64.b64decode(to_process)
            if len(b) > 0:
                qc_response.ParseFromString(b)
                return qc_response, buffer_contents
        except:
            print(f"PARSE FAILURE: {to_process}")
            pass

    return None, buffer_contents


# class MessageDetails:
#     data_event: asyncio.Event
#     data: bytes
#
#     def __init__(self):
#         self.data = None
#         self.data_event = asyncio.Event()
#
#
# async def read_async_coroutine(serial: aioserial.AioSerial, md: MessageDetails) -> bytes:
#     while True:
#         data: bytes = await serial.read_async()
#         print(f"NEW DATA: {data}")
#         md.data = data


# async def monitor_for_messages(serial: aioserial.AioSerial, cancel_event: asyncio.Event):
#     print("STARTING MESSAGE MONITOR")
#
#     md = MessageDetails()
#     read_task = asyncio.create_task(read_async_coroutine(serial, md))
#
#     while not cancel_event.is_set():
#         read_task.cancel()
