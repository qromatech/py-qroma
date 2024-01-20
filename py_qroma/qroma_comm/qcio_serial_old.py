# import asyncio
# import serial
# import time
# import base64
# from dataclasses import dataclass
# from . import qcio_base
#
#
# @dataclass
# class QcioSerialConfig:
#     com_port: str
#     baud_rate: int = 115200
#     timeout: float = 0.5
#
#
# class QcioSerial(qcio_base.QcioBase):
#     ser: serial.Serial
#
#     ser_timeout: float
#
#     def __init__(self, arg: str | QcioSerialConfig):
#         self.ser = self._create_serial(arg)
#         self._keep_running = True
#
#     def _create_serial(self, arg: str | QcioSerialConfig):
#         if isinstance(arg, str):
#             return self._create_serial(QcioSerialConfig(arg))
#         else:
#             self.ser_timeout = arg.timeout
#             return serial.Serial(
#                 port=arg.com_port,
#                 baudrate=arg.baud_rate,
#                 # timeout=arg.timeout,
#                 timeout=0.1,
#             )
#
#     async def send_bytes(self, cmd_bytes: bytes):
#         def do_send(the_bytes):
#             print(f"SENDING {len(the_bytes)} BYTES")
#             self.ser.write(the_bytes)
#             self.ser.flush()
#
#         send_count = 1000
#         sleep_duration = 0.03
#
#         bytes_to_send = cmd_bytes[:]
#         print(f"TO SEND: {len(bytes_to_send)} BYTES")
#         while len(bytes_to_send) > send_count:
#             the_bytes = bytes_to_send[0:send_count]
#             do_send(the_bytes)
#             bytes_to_send = bytes_to_send[send_count:]
#             time.sleep(sleep_duration)
#
#         if len(bytes_to_send) > 0:
#             do_send(bytes_to_send)
#
#     async def send_bytes_base64_with_newline(self, cmd_bytes: bytes):
#         b64_cmd_bytes = base64.b64encode(cmd_bytes) + b"\n"
#         print(f"SENDING B64: {b64_cmd_bytes}")
#         await self.send_bytes(b64_cmd_bytes)
#
#     async def read_next_byte(self, timeout: float):
#         return await self.read_n_bytes(1, timeout)
#
#     async def read_n_bytes(self, byte_count: int, timeout: float):
#         """
#         Wait up until timeout seconds to receive a byte.
#         """
#         self.ser.timeout = timeout
#         n_bytes = self.ser.read(byte_count)
#         print(f"READx BYTES: {n_bytes}")
#         return n_bytes
#
#     async def run(self):
#         while self._keep_running:
#             await asyncio.sleep(0.01)
#
#     def stop(self):
#         self._keep_running = False
#
#     async def is_ready(self):
#         return True
