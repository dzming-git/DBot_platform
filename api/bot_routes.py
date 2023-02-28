# bot_routes.py
from flask import Flask, request
from app.message_handler.message_handler import message_handler
from utils.service_discovery.consul_client import consul_client
from conf.route_info.route_info import RouteInfo

def register_consul(app):
    '''
    服务开启前,注册consul
    '''
    service_name = RouteInfo.get_bot_name()
    port = RouteInfo.get_bot_port()
    tags = RouteInfo.get_bot_tags()
    bot_id = consul_client.register_service(service_name, port, tags)
    config = {
        'bot_id': bot_id
    }
    return config

def deregister_service(app):
    '''
    服务结束后,注销consul
    '''
    bot_id = app.config['bot_id']
    consul_client.deregister_service(bot_id)

def route_registration(app):
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
    


