# command_error_handler.py
from app.message_sender import Msg_struct, send_message

def command_error_handler(gid=None, qid=None):
    msg_struct = Msg_struct(gid=gid, qid=qid, at=True, msg='命令错误！')
    send_message(msg_struct)