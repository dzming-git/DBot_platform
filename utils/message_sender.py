import requests

class Msg_struct:
    def __init__(self, gid=None, qid=None, at=False, msg=''):
        self.gid = gid
        self.qid = qid
        self.at = at
        self.msg = msg

def send_message(msg_struct: Msg_struct):
    if msg_struct.gid is None:
        requests.get(f'http://127.0.0.1:5700/send_private_msg?user_id={msg_struct.qid}&message={msg_struct.msg}')
    else:
        if msg_struct.at:
            msg_struct.msg = f'[CQ:at,qq={msg_struct.qid}] {msg_struct.msg}'      
        requests.get(f'http://127.0.0.1:5700/send_group_msg?group_id={msg_struct.gid}&message={msg_struct.msg}')