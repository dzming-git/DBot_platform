# bot_routes.py
from flask import request
from app.message_handler.message_handler import message_handler

def bot_route_registration(app):
    @app.route('/', methods=['POST'])
    def handle_message():
        # 获取消息体
        message = request.json
        print(message)
        # 获取消息类型
        message_type = message.get('message_type')
        # 获取发送者id
        sender_id = message.get('sender', {}).get('user_id')
        # 获取群id
        group_id = message.get('group_id')
        # 获取原始消息内容
        raw_message = message.get('raw_message')
        # 处理私聊消息
        if message_type == 'private':
            message_handler(raw_message, sender_id)
        # 处理群聊消息
        elif message_type == 'group':
            message_handler(raw_message, group_id, sender_id)
        # 返回响应
        return 'OK'

    @app.route('/health')
    def health_check():
        return 'OK'
    

