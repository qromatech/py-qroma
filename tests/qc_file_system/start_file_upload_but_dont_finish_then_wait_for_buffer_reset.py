import asyncio
import base64
import time

import aioserial

from py_qroma.qc_file_system import qfs_message_factory
from py_qroma.qroma_comm.qroma_monitor import monitor_for_messages

from py_qroma.test_resources import dev_settings


rx_buffer = bytearray()
ok_to_tx_event = asyncio.Event()


def on_data(new_bytes: bytes):
    rx_buffer.extend(new_bytes)


async def do_partial_file_upload(serial: aioserial.AioSerial):
    test_id = int(time.time())
    upload_init_message_bytes = qfs_message_factory.create_stream_file_contents_bytes(
        upload_path=f"/partial_{test_id}.abc",
        filesize=9999,
        checksum=123,
        file_stream_id=test_id,
    )
    upload_init_message_b64 = base64.b64encode(upload_init_message_bytes) + b"\n"
    await asyncio.sleep(1.0)
    await serial.write_async(upload_init_message_b64)


async def start_file_upload_but_dont_finish_then_wait_for_buffer_reset():
    serial = dev_settings.create_test_serial_instance()

    await asyncio.gather(
        do_partial_file_upload(serial),
        monitor_for_messages(8.0, serial, on_data),
    )

    print(rx_buffer)
    assert b"processCommBuffer EXPIRED" in rx_buffer
    assert b"QromaCommStreamHandler::reset()" in rx_buffer


if __name__ == "__main__":
    asyncio.run(start_file_upload_but_dont_finish_then_wait_for_buffer_reset())
