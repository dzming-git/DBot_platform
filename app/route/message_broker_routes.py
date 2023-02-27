# message_broker_routes.py
from flask import Flask, request, jsonify
from app.message_handler.bot_commands import bot_commands
from api.consul_client import consul_client
from conf.conf import Conf

def register_consul(app):
    '''
    服务开启前,注册consul
    '''
    server_name = Conf.get_message_broker_name()
    port = Conf.get_message_broker_port()
    server_tags = Conf.get_bot_tags()
    message_broker_id = consul_client.register_server(server_name, port, server_tags)
    config = {
        'message_broker_id': message_broker_id
    }
    return config

def deregister_server(app):
    '''
    服务结束后,注销consul
    '''
    message_broker_id = app.config['message_broker_id']
    consul_client.deregister_server(message_broker_id)

def craete_message_broker_app():
    message_broker_app = Flask(__name__)
    config = {
        **register_consul(message_broker_app)
    }
    message_broker_app.config.update(config)

    @message_broker_app.route('/server_commands', methods=['POST'])
    def register_server_commands():
        data = request.get_json()
        server_name = data.get('server_name')
        commands = data.get('commands')
        if server_name and commands:
            bot_commands[server_name] = commands
            print(bot_commands)
            return jsonify({'message': 'Bot commands registered successfully'}), 200
        else:
            return jsonify({'message': 'Invalid request'}), 400
    
    @message_broker_app.route('/health')
    def health_check():
        return 'OK'
    return message_broker_app
