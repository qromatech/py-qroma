from py_qroma.qroma_comm_proto import qroma_comm_pb2, file_system_commands_pb2, qroma_types_pb2, qroma_streams_pb2


def create_get_list_dir_bytes(dir_path: str) -> bytes:
    command = file_system_commands_pb2.ListDirContentsCommand()
    command.dirPath = dir_path

    fs_command = file_system_commands_pb2.FileSystemCommand()
    fs_command.listDirContentsCommand.CopyFrom(command)

    qroma_message = qroma_comm_pb2.QromaCommCommand()
    qroma_message.fsCommand.CopyFrom(fs_command)

    msg_bytes = qroma_message.SerializeToString()
    return msg_bytes


def create_get_report_filedata_bytes(file_path: str) -> bytes:
    command = file_system_commands_pb2.ReportFileDataCommand()
    command.filePath = file_path

    fs_command = file_system_commands_pb2.FileSystemCommand()
    fs_command.reportFileDataCommand.CopyFrom(command)

    qroma_message = qroma_comm_pb2.QromaCommCommand()
    qroma_message.fsCommand.CopyFrom(fs_command)

    msg_bytes = qroma_message.SerializeToString()
    return msg_bytes


def create_stream_file_contents_bytes(upload_path: str, filesize: int, checksum: int, file_stream_id):
    file_data = qroma_types_pb2.FileData()
    file_data.filename = upload_path
    file_data.filesize = filesize
    file_data.checksum = checksum

    write_stream_command = qroma_streams_pb2.InitWriteFileStreamCommand()
    write_stream_command.fileStreamId = file_stream_id
    write_stream_command.fileData.CopyFrom(file_data)

    qs_command = qroma_streams_pb2.QromaStreamCommand()
    qs_command.initWriteFileStreamCommand.CopyFrom(write_stream_command)

    qroma_message = qroma_comm_pb2.QromaCommCommand()
    qroma_message.streamCommand.CopyFrom(qs_command)

    msg_bytes = qroma_message.SerializeToString()
    return msg_bytes
