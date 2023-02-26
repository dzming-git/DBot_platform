# gocqhttp_routes.py
from flask import Flask, request
from app.message_handler.message_handler import message_handler
from api.consul_client import consul_client
from conf.conf import Conf

def create_gocqhttp_app():
    gocqhttp_app = Flask(__name__)

    @gocqhttp_app.before_first_request
    def register_consul():
        '''
        服务开启前,注册consul
        '''
        server_name = Conf.get_rob_name()
        port = Conf.get_gocqhttp_port()
        service_tags = Conf.get_gocqhttp_tags()
        bot_id = consul_client.register_service(server_name, port, service_tags)
        gocqhttp_app.config['bot_id'] = bot_id

    @gocqhttp_app.teardown_appcontext
    def deregister_service(error):
        '''
        服务结束后,注销consul
        '''
        bot_id = gocqhttp_app.config['bot_id']
        consul_client.deregister_service(bot_id)

    @gocqhttp_app.route('/', methods=['POST'])
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

    @gocqhttp_app.route('/health')
    def health_check():
        return 'OK'
    
    return gocqhttp_app