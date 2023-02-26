# main_routes.py
from flask import Flask, request
from app.message_handler.message_handler import message_handler
from api.consul_client import consul_client
from conf.conf import Conf

def register_consul(app):
    '''
    服务开启前,注册consul
    '''
    server_name = Conf.get_rob_name()
    port = Conf.get_main_port()
    server_tags = Conf.get_main_tags()
    main_server_id = consul_client.register_server(server_name, port, server_tags)
    config = {
        'main_server_id': main_server_id
    }
    return config

def deregister_server(app):
    '''
    服务结束后,注销consul
    '''
    main_server_id = app.config['main_server_id']
    consul_client.deregister_server(main_server_id)

def create_main_app():
    main_app = Flask(__name__)
    config = {
        **register_consul(main_app)
    }
    main_app.config.update(config)

    @main_app.route('/', methods=['POST'])
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

    @main_app.route('/health')
    def health_check():
        return 'OK'
    
    return main_app

def destory_main_app(app):
    deregister_server(app)
