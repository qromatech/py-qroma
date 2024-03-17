import asyncio
from py_qroma.qroma_comm.qroma_monitor import monitor_for_messages

from py_qroma.test_resources import dev_settings


rx_buffer = bytearray()


def on_data(new_bytes: bytes):
    rx_buffer.extend(new_bytes)


async def send_junk_then_wait_for_buffer_reset_message():
    serial = dev_settings.create_test_serial_instance()

    await asyncio.gather(
        serial.write_async(b"blurgle"),
        monitor_for_messages(5.0, serial, on_data),
    )

    print(rx_buffer)
    assert b"processCommBuffer EXPIRED" in rx_buffer
    assert b"RESETTING QromaCommProcessor" in rx_buffer


if __name__ == "__main__":
    asyncio.run(send_junk_then_wait_for_buffer_reset_message())
