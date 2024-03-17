import asyncio
import time

from py_qroma.qc_file_system.upload_file import UploadFileDetails, UploadDetails, do_upload, \
    create_upload_file_details_from_bytes, create_default_upload_rate_parameters
from py_qroma.qc_file_system.show_filedetails import show_filedetails
from py_qroma.test_resources import dev_settings

event = asyncio.Event()


async def upload_largeish_file_at_reasonable_rate_and_check_for_success():
    FILE_STREAM_ID = int(time.time())
    UPLOAD_PATH = f"/upload_{FILE_STREAM_ID}.txt"
    file_bytes = b"1234567890\n" * 5000
    print(f"FILE SIZE: {len(file_bytes)}")

    upload_file_details: UploadFileDetails = create_upload_file_details_from_bytes(file_bytes, UPLOAD_PATH)

    serial = dev_settings.create_test_serial_instance()

    upload_rate_parameters = create_default_upload_rate_parameters()
    upload_rate_parameters.num_bytes_per_chunk = 100
    upload_rate_parameters.delay_between_chunks = 0.1

    upload_details = UploadDetails()
    upload_details.file_details = upload_file_details
    upload_details.serial = serial
    upload_details.file_stream_id = FILE_STREAM_ID
    upload_details.upload_rate_parameters = upload_rate_parameters

    upload_result = await do_upload(upload_details)
    print("HAS UPLOAD RESULT")
    print(upload_result)

    file_details = await show_filedetails(upload_details.file_details.upload_path, upload_details.serial)
    print("DONE HERE...")
    print(file_details)

    assert upload_result.fileData.checksum == file_details.fsResponse.reportFileDataResponse.fileData.checksum


if __name__ == "__main__":
    asyncio.run(upload_largeish_file_at_reasonable_rate_and_check_for_success())
