# message_broker_routes.py
from flask import Flask, request, jsonify
from app.message_handler.bot_commands import BotCommands
from app.message_handler.server_registry import ServerRegistry
from api.consul_client import consul_client
from conf.conf import Conf
from app.message_sender import Msg_struct, send_message


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

def route_registration(app):
    @app.route('/server_commands', methods=['POST'])
    def register_server_commands():
        data = request.get_json()
        server_name = data.get('server_name')
        commands = data.get('commands')
        if server_name and commands:
            for command in commands:
                BotCommands.add_commands(command, server_name)            
            return jsonify({'message': 'Bot commands registered successfully'}), 200
        else:
            return jsonify({'message': 'Invalid request'}), 400
    
    @app.route('/server_results', methods=['POST'])
    def register_server_results():
        data = request.get_json()
        message = data.get('message')
        gid = data.get('gid')
        qid = data.get('qid')
        at = data.get('at')
        msg_struct = Msg_struct(gid=gid, qid=qid, at=at, msg=message)
        send_message(msg_struct)
        return jsonify({'message': 'OK'}), 200
    
    @app.route('/server_endpoints', methods=['POST'])
    def register_server_endpoints():
        data = request.get_json()
        server_name = data.get('server_name')
        endpoints_info = data.get('endpoints_info')
        if server_name and endpoints_info:
            usages = list(endpoints_info.keys())
            for usage in usages:
                endpoint = endpoints_info[usage]
                ServerRegistry.add_server_endpoint(server_name, usage, endpoint)
            return jsonify({'message': 'Bot commands registered successfully'}), 200
        else:
            return jsonify({'message': 'Invalid request'}), 400
    
    @app.route('/health')
    def health_check():
        return 'OK'

def craete_message_broker_app():
    message_broker_app = Flask(__name__)
    config = {
        **register_consul(message_broker_app)
    }
    message_broker_app.config.update(config)
    route_registration(message_broker_app)
    return message_broker_app
