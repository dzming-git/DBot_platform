# permission_denied_handler.py
from app.message_sender import Msg_struct, send_message

def permission_denied(gid=None, qid=None):
    msg_struct = Msg_struct(gid=gid, qid=qid, at=True, msg='权限不足！')
    send_message(msg_struct)