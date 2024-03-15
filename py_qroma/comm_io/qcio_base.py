import asyncio
import time


EXPECTED_LINE_COUNT_MAX = 1000


class QcioBase:

    def send_bytes(self, cmd_bytes: bytearray) -> None:
        pass

    async def read_next_byte(self, timeout: float):
        pass
        # return self.read_n_bytes(1)

    async def read_n_bytes(self, byte_count: int, timeout: float) -> bytes:
        pass

    # async def read_until_byte_count(self, byte_count: int, timeout: float) -> bytes:
    #     now = time.time()
    #     give_up_time = now + timeout
    #
    #     line = bytearray()
    #     while time.time() < give_up_time:
    #         b = await self.read_next_byte()
    #         if len(b) > 0:
    #             if b[0] == bytes(b'\n')[0]:
    #                 return bytes(line)
    #             line += b
    #         else:
    #             await asyncio.sleep(0.01)

    async def read_bytes_until_timeout(self, timeout: float) -> bytes:
        now = time.time()
        give_up_time = now + timeout

        data = bytearray()
        while time.time() < give_up_time:
            # b = await self.read_next_byte(0.1)
            b = await self.read_n_bytes(100, 0.1)
            data += b

        return data

    def run(self):
        pass

    def is_ready(self):
        pass

    def stop(self):
        pass

    async def read_line(self, timeout=5.0):
        done = False
        line = bytearray()

        now = time.time()
        give_up_time = now + timeout

        while time.time() < give_up_time and not done:
            b = await self.read_next_byte()
            if len(b) > 0:
                if b[0] == bytes(b'\n')[0]:
                    return bytes(line)
                line += b
            else:
                await asyncio.sleep(0.01)

        print("READLINE FAILED")
        return bytes(line)

    async def read_lines(self,
                         expected_line_count=EXPECTED_LINE_COUNT_MAX,
                         allowed_max_wait_for_response=10.0,
                         allowed_max_read_count=1000):
        now = time.time()
        give_up_time = now + allowed_max_wait_for_response

        response_bytes = b''

        the_lines = []

        while len(response_bytes) < allowed_max_read_count and \
                time.time() < give_up_time and \
                len(the_lines) < expected_line_count:
            # x = self.ser.readline()
            x = await self.read_line()
            # print(x)
            the_lines.append(x)

        # print("THE LINES")
        # print(the_lines)
        return the_lines

    # async def read_until_pb_parsed(self, pb_message_instance, timeout: float):
    #     now = time.time()
    #     give_up_time = now + timeout
    #
    #     response_bytes = b''
    #     while time.time() < give_up_time:
    #         # b = await qcio.read_next_byte(0.1)
    #         b = await self.read_n_bytes(100, 0.3)
    #         if b:
    #             response_bytes += b
    #             print("RECEIVEDxx... ")
    #             print(response_bytes)
    #
    #             try:
    #                 pb_message_instance.ParseFromString(response_bytes)
    #                 print(pb_message_instance)
    #                 return pb_message_instance
    #             except:
    #                 print(f"PARSE FAILURE: {response_bytes}")
    #                 pass
    #
    #     return None
    #
    # async def read_until_base64_newline_pb_parsed(self, pb_message_instance, timeout: float):
    #     now = time.time()
    #     give_up_time = now + timeout
    #
    #     response_bytes = b''
    #     while time.time() < give_up_time:
    #         b = await self.read_n_bytes(100, 0.3)
    #         if b:
    #             response_bytes += b
    #             print("RECEIVEDyy... ")
    #             print(response_bytes)
    #
    #             try:
    #                 print(response_bytes[-1])
    #                 if response_bytes[-1] == 10:
    #                     to_parse = response_bytes[:-1]
    #                     print("TO PARSE")
    #                     print(to_parse)
    #                     b = base64.b64decode(to_parse)
    #                     pb_message_instance.ParseFromString(b)
    #                     print(pb_message_instance)
    #                     return pb_message_instance
    #             except:
    #                 print(f"PARSE FAILURE: {response_bytes}")
    #                 pass
    #
    #     return None
