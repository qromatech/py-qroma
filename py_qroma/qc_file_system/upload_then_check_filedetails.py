import asyncio
import time

import aioserial

from upload_file import UploadFileDetails, UploadDetails, do_upload, create_upload_file_details_from_local_file
from show_filedetails import show_filedetails
from py_qroma.test_resources.dev_settings import QROMA_ACTIVE_COM_PORT, TEST_FILE

event = asyncio.Event()


async def main(upload_details: UploadDetails):
    upload_result = await do_upload(upload_details)
    print("HAS UPLOAD RESULT")
    print(upload_result)

    file_details = await show_filedetails(upload_details.file_details.upload_path, upload_details.serial)
    print("DONE HERE...")
    print(file_details)

    if upload_result.fileData.checksum == file_details.fsResponse.reportFileDataResponse.fileData.checksum:
        print("YAY!!!!!")
    else:
        print(":(")


if __name__ == "__main__":
    FILE_STREAM_ID = int(time.time())
    # UPLOAD_PATH = f"/upload_{FILE_STREAM_ID}.txt"
    UPLOAD_PATH = "/qroma_hat.dgsr"

    uploadFileDetails: UploadFileDetails = create_upload_file_details_from_local_file(TEST_FILE, UPLOAD_PATH)

    aioserialInstance: aioserial.AioSerial = aioserial.AioSerial(
        port=QROMA_ACTIVE_COM_PORT,
        baudrate=115200,
    )

    uploadDetails = UploadDetails()
    uploadDetails.file_details = uploadFileDetails
    uploadDetails.serial = aioserialInstance
    uploadDetails.file_stream_id = FILE_STREAM_ID

    asyncio.run(main(uploadDetails))
