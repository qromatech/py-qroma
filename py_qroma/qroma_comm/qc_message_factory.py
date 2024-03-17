from py_qroma.qroma_comm_proto import qroma_comm_pb2, file_system_commands_pb2, qroma_types_pb2, qroma_streams_pb2


def create_get_reset_device_command_bytes(dir_path: str) -> bytes:
    command = file_system_commands_pb2.ListDirContentsCommand()
    command.dirPath = dir_path

    fs_command = file_system_commands_pb2.FileSystemCommand()
    fs_command.listDirContentsCommand.CopyFrom(command)

    qroma_message = qroma_comm_pb2.QromaCommCommand()
    qroma_message.fsCommand.CopyFrom(fs_command)

    msg_bytes = qroma_message.SerializeToString()
    return msg_bytes

