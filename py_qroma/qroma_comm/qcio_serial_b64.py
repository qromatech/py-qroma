import asyncio
import serial
import time
from dataclasses import dataclass
import base64
from ..qroma_comm_proto import qroma_comm_pb2
from ..qroma_comm_proto import file_system_commands_pb2



@dataclass
class QcioSerialConfig:
    com_port: str
    baud_rate: int = 115200
    timeout: float = 0.2
    read_size: int = 100


class QcioSerial:
    ser: serial.Serial

    ser_timeout: float
    read_size: int

    _rx_buffer: bytearray

    def __init__(self, arg: str | QcioSerialConfig):
        self.ser = self._create_serial(arg)
        self._rx_buffer = bytearray()
        self._keep_running = True

    def _create_serial(self, arg: str | QcioSerialConfig):
        if isinstance(arg, str):
            return self._create_serial(QcioSerialConfig(arg))
        else:
            self.ser_timeout = arg.timeout
            self.read_size = arg.read_size

            return serial.Serial(
                port=arg.com_port,
                baudrate=arg.baud_rate,
                timeout=arg.timeout,
            )

    async def send_bytes(self, cmd_bytes: bytes):
        def do_send(the_bytes):
            print(f"SENDING {len(the_bytes)} BYTES")
            self.ser.write(the_bytes)
            self.ser.flush()

        send_count = 1000
        sleep_duration = 0.03

        bytes_to_send = cmd_bytes[:]
        print(f"TO SEND: {len(bytes_to_send)} BYTES")
        while len(bytes_to_send) > send_count:
            the_bytes = bytes_to_send[0:send_count]
            do_send(the_bytes)
            bytes_to_send = bytes_to_send[send_count:]
            time.sleep(sleep_duration)

        if len(bytes_to_send) > 0:
            do_send(bytes_to_send)

    async def read_next_byte(self, timeout: float):
        return await self.read_n_bytes(1, timeout)

    async def read_n_bytes(self, byte_count: int, timeout: float):
        """
        Wait up until timeout seconds to receive a byte.
        """
        self.ser.timeout = timeout
        n_bytes = self.ser.read(byte_count)
        # print(f"READx BYTES: {n_bytes}")
        return n_bytes

    async def run(self):
        while self._keep_running:
            await asyncio.sleep(0.01)

    def stop(self):
        self._keep_running = False

    async def is_ready(self):
        return True

    async def read_line(self, timeout=5.0):
        done = False
        line = bytearray()

        now = time.time()
        give_up_time = now + timeout

        while time.time() < give_up_time and not done:
            time_remaining = give_up_time - time.time()
            b = await self.read_next_byte(time_remaining)
            if len(b) > 0:
                if b[0] == bytes(b'\n')[0]:
                    return bytes(line)
                line += b
            else:
                await asyncio.sleep(0.01)

        print("READLINE FAILED")
        return None

    async def read_until_base64_newline_pb_parsed(self, pb_message_instance, timeout: float):
        give_up_time = time.time() + timeout
        while time.time() < give_up_time:
            line = await self.read_line(timeout)
            if line:
                print(line)
                try:
                    b = base64.b64decode(line)
                    if len(b) > 0:
                        pb_message_instance.ParseFromString(b)
                        print(f"PARSE SUCCESS: {line} [{b}]")
                        print("pb_message_instance received")
                        print(pb_message_instance)
                        return pb_message_instance
                except:
                    print(f"PARSE FAILURE: {line}")
                    pass

        return None

    async def send_bytes_base64_with_newline(self, cmd_bytes: bytes):
        b64_cmd_bytes = base64.b64encode(cmd_bytes) + b"\n"
        print(f"SENDING B64: {b64_cmd_bytes}")
        await self.send_bytes(b64_cmd_bytes)

    async def monitor_for_pb_message(self, pb_message_instance, callback, timeout: float):
        give_up_time = time.time() + timeout

        response_bytes = b''
        while time.time() < give_up_time:
            time_remaining = give_up_time - time.time()
            line = await self.read_until_base64_newline_pb_parsed(pb_message_instance, time_remaining)
            if line:
                try:
                    pb_message_instance.ParseFromString(response_bytes)
                    callback(pb_message_instance)
                except:
                    print(f"MONITOR FOR MESSAGE FAILED: {line}")
                    pass

        return None

    async def read_bytes_until_timeout(self, timeout: float) -> bytes:
        now = time.time()
        give_up_time = now + timeout

        data = bytearray()
        while time.time() < give_up_time:
            # b = await self.read_next_byte(0.1)
            b = await self.read_n_bytes(100, 0.1)
            data += b

        return data

    async def send_fs_command(self, fs_command):
        qroma_comm_command = qroma_comm_pb2.QromaCommCommand()
        qroma_comm_command.fsCommand.CopyFrom(fs_command)

        msg_bytes = qroma_comm_command.SerializeToString()
        await self.send_bytes_base64_with_newline(msg_bytes)

    async def send_qroma_config_command(self, qroma_config_command):
        qroma_comm_command = qroma_comm_pb2.QromaCommCommand()

        print("MODULE")
        print(qroma_comm_pb2)
        print("LOCAL COMM COMMAND")
        print(qroma_comm_command.commConfigCommand.__class__)
        print("INPUT")
        print(qroma_config_command.__class__)

        qroma_comm_command.commConfigCommand.CopyFrom(qroma_config_command)
        msg_bytes = qroma_comm_command.SerializeToString()
        await self.send_bytes_base64_with_newline(msg_bytes)

    async def send_app_command_bytes(self, app_command_bytes):
        print("APP COMMAND BYTES")
        print(app_command_bytes)
        qroma_comm_command = qroma_comm_pb2.QromaCommCommand()
        qroma_comm_command.appCommandBytes = app_command_bytes

        msg_bytes = qroma_comm_command.SerializeToString()
        await self.send_bytes_base64_with_newline(msg_bytes)

    async def get_file_data(self, file_name):
        qcc = qroma_comm_pb2.QromaCommCommand()

        command = file_system_commands_pb2.ReportFileDataCommand()
        command.filename = file_name

        qcc.fsCommand.reportFileDataCommand.CopyFrom(command)

        cmd_bytes = qcc.SerializeToString()
        await self.send_bytes_base64_with_newline(cmd_bytes)

        qc_response = qroma_comm_pb2.QromaCommResponse()
        response = await self.read_until_base64_newline_pb_parsed(qc_response, 5)

        return response

    async def get_file_contents(self, file_path):
        qcc = qroma_comm_pb2.QromaCommCommand()

        command = file_system_commands_pb2.GetFileContentsCommand()
        command.filePath = file_path

        qcc.fsCommand.getFileContentsCommand.CopyFrom(command)

        cmd_bytes = qcc.SerializeToString()
        await self.send_bytes_base64_with_newline(cmd_bytes)

        qc_response = qroma_comm_pb2.QromaCommResponse()
        response = await self.read_until_base64_newline_pb_parsed(qc_response, 5)

        return response