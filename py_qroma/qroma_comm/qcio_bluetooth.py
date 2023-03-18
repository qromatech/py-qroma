import asyncio
from bleak import BleakClient
import time
from qroma_comm import qcio_base
import settings


def check_comm_connection(svc_uuid, char_uuid):
    return settings.QROMA_COMM_SERVICE_UUID == svc_uuid and settings.QROMA_COMM_RECEIVE_CHARACTERISTIC_UUID == char_uuid


class QcioBluetooth(qcio_base.QcioBase):
    bt: BleakClient

    def __init__(self, address: str, check_connected_callback=None):
        self._client = BleakClient(address)
        self._address = address
        self._is_connected = False
        self._keep_running = True

        self._registered_qroma_bt_notifications = []
        self._active_notification_handles = []
        self._check_connected_callback = check_connected_callback
        self._rx_buffer = bytearray()

        STD_QCIO_SVC_CHARACTERISTIC_CALLBACKS = (
            (settings.QROMA_COMM_SERVICE_UUID, settings.QROMA_COMM_RECEIVE_CHARACTERISTIC_UUID, self.on_qroma_comm_rx_notify),
        )

        for svc_uuid, char_uuid, cb in STD_QCIO_SVC_CHARACTERISTIC_CALLBACKS:
            self.register_qroma_bt_notification(svc_uuid, char_uuid, cb)

    def register_qroma_bt_notification(self, svc_uuid, char_uuid, sender_data_callback):
        print(f"REGISTERING QROMA BT NOTIFICATION {svc_uuid} -> {char_uuid}")
        self._registered_qroma_bt_notifications.append((svc_uuid, char_uuid, sender_data_callback))

    def on_qroma_comm_rx_notify(self, sender, data):
        print("on_qroma_comm_rx_notify")
        self._rx_buffer += data
        print(data)

    def check_connected(self, svc_uuid, char_uuid):
        if self._check_connected_callback is not None:
            return self._check_connected_callback(svc_uuid, char_uuid)

        print("NO CONNECTION CHECK CALLBACK REGISTERED - USING QROMA COMM DEFAULT CHECK")
        return check_comm_connection(svc_uuid, char_uuid)

    async def run(self):
        print("START BT RUN")
        while self._keep_running:
            try:
                print("CONNECTING")
                await self._client.connect()
                print("CONNECTED")
                services = await self._client.get_services()
                is_connected = False
                for service in services:
                    # print("SERVICE: " + str(service))
                    for c in service.characteristics:
                        # print(c.uuid)
                        if self.check_connected(service.uuid, c.uuid):
                            is_connected = True

                        for svc_uuid, char_uuid, cb in self._registered_qroma_bt_notifications:
                            if service.uuid == svc_uuid and c.uuid == char_uuid:
                                def create_notification_handler(the_cb):
                                    def notification_handler(sender, data):
                                        the_cb(sender, data)
                                    return notification_handler

                                nh = create_notification_handler(cb)

                                print(f"MONITORING: {svc_uuid} -> {char_uuid}")
                                await self._client.start_notify(c.handle, nh)
                                self._active_notification_handles.append(c.handle)

                self._is_connected = is_connected

                while self._keep_running:
                    # print("SLEEP")
                    await asyncio.sleep(1)

                for h in self._active_notification_handles:
                    await self._client.stop_notify(h)

            except Exception as e:
                print("EXCEPTION WHILE BT RUNNING")
                print(e)
            finally:
                if self._is_connected:
                    await self._client.disconnect()
                    self._is_connected = False

    async def wait_until_ready(self):
        while not self._is_connected:
            await asyncio.sleep(0.1)

    def is_ready(self):
        return self._is_connected

    async def stop(self, wait_until_disconnected=True):
        self._keep_running = False
        if wait_until_disconnected:
            while self._is_connected:
                await asyncio.sleep(0.1)

    async def bt_send_bytes(self, the_bytes: bytearray):
        if self._is_connected:
            # print(cmd)
            await self._client.write_gatt_char(settings.TX_CHARACTERISTIC_UUID, the_bytes, True)
            print(f"{len(the_bytes)} BYTES SENT")
        else:
            print("CAN'T SEND BYTES - NOT CONNECTED")

    async def send_bytes(self, cmd_bytes):

        send_count = 500
        sleep_duration = 0.03

        bytes_to_send = cmd_bytes[:]
        while len(bytes_to_send) > send_count:
            the_bytes = bytes_to_send[0:send_count]
            await self.bt_send_bytes(the_bytes)
            bytes_to_send = bytes_to_send[send_count:]
            await asyncio.sleep(sleep_duration)

        if len(bytes_to_send) > 0:
            await self.bt_send_bytes(bytes_to_send)

    async def readnext(self, timeout=2.0) -> bytes:
        now = time.time()
        give_up_time = now + timeout

        while time.time() < give_up_time:
            if len(self._rx_buffer) > 0:
                retval = bytes(self._rx_buffer[0:1])
                self._rx_buffer = self._rx_buffer[1:]
                return retval
            else:
                # print("BT readnext() - nothing to read")
                await asyncio.sleep(0.01)

        print("READNEXT FAILED")
        return b''

    async def readbytes(self, byte_count, timeout=5.0) -> bytes:
        now = time.time()
        give_up_time = now + timeout

        while time.time() < give_up_time:
            if len(self._rx_buffer) >= byte_count:
                retval = bytes(self._rx_buffer[0:byte_count])
                self._rx_buffer = self._rx_buffer[byte_count:]
                return retval
            else:
                await asyncio.sleep(0.01)

        return b''
