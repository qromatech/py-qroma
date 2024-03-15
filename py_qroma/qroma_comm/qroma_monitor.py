import asyncio
import datetime
from asyncio import Task

import aioserial

from py_qroma.test_resources.dev_settings import QROMA_ACTIVE_COM_PORT


async def timeout_after(duration: float, timeout_event: asyncio.Event):
    print("START SLEEP")
    await asyncio.sleep(duration)
    print(f"SLEEP COMPLETE - {datetime.datetime.now()}")
    timeout_event.set()


class MessageDetails:
    data_event: asyncio.Event

    def __init__(self, on_data):
        self.on_data = on_data
        self.data_event = asyncio.Event()


async def read_async_coroutine(serial: aioserial.AioSerial, md: MessageDetails, timeout_event: asyncio.Event):
    while not timeout_event.is_set():
        # print("WAITING FOR DATA")
        data: bytes = await serial.read_async()
        if md.on_data:
            md.on_data(data)


async def wait_for_timeout(read_task: Task, timeout_event: asyncio.Event):
    print("STARTING MESSAGE MONITOR")

    # read_task = asyncio.create_task(read_async_coroutine(serial, md))
    start_time = datetime.datetime.now()
    print(f"WAITING FOR CANCEL: {start_time}")

    while timeout_event.is_set():
        print("READ TASK CANCEL")
        read_task.cancel()
        end_time = datetime.datetime.now()
        print(f"CANCEL DONE - {end_time}")
        # print(f"MONITOR DURATION: {end_time - start_time}")
        return


async def monitor_for_messages(duration: float, serial: aioserial.AioSerial, on_data=None):
    md = MessageDetails(on_data)
    timeout_event = asyncio.Event()
    read_task = asyncio.create_task(read_async_coroutine(serial, md, timeout_event))
    print(f"TIME OUT IS SET: {timeout_event.is_set()}")

    await asyncio.gather(
        timeout_after(duration, timeout_event),
        wait_for_timeout(read_task, timeout_event),
        read_task,
    )
    print("monitor_for_messages COMPLETE")


if __name__ == "__main__":
    aioserialInstance: aioserial.AioSerial = aioserial.AioSerial(
        port=QROMA_ACTIVE_COM_PORT,
        baudrate=115200,
    )

    asyncio.run(monitor_for_messages(2.0, aioserialInstance))
