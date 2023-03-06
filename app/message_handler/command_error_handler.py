# command_error_handler.py
from utils.message_sender import Msg_struct, send_message

def command_error_handler(gid=None, qid=None):
    message = '命令错误'
    if gid:
        message = f'[CQ:at,qq={qid}]' + message
    msg_struct = Msg_struct(gid=gid, qid=qid, msg=message)
    send_message(msg_struct)