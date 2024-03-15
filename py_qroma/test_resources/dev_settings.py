QROMA_ACTIVE_COM_PORT = "COM6"
# TEST_FILE = "test_resources/240bytes.txt"
TEST_FILE = "test_resources/qroma_hat.dgsr"


def create_test_serial_instance():
    import aioserial
    serial_instance: aioserial.AioSerial = aioserial.AioSerial(
        port=QROMA_ACTIVE_COM_PORT,
        baudrate=115200,
    )
    return serial_instance
