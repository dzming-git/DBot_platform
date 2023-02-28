# message_broker_routes.py
from flask import request, jsonify
from app.message_handler.bot_commands import BotCommands
from app.message_handler.service_registry import serviceRegistry
from utils.message_sender import Msg_struct, send_message

def message_broker_route_registration(app):
    @app.route('/service_commands', methods=['POST'])
    def register_service_commands():
        data = request.get_json()
        service_name = data.get('service_name')
        commands = data.get('commands')
        if service_name and commands:
            for command in commands:
                BotCommands.add_commands(command, service_name)            
            return jsonify({'message': 'Bot commands registered successfully'}), 200
        else:
            return jsonify({'message': 'Invalid request'}), 400
    
    @app.route('/service_results', methods=['POST'])
    def register_service_results():
        data = request.get_json()
        message = data.get('message')
        gid = data.get('gid')
        qid = data.get('qid')
        at = data.get('at')
        msg_struct = Msg_struct(gid=gid, qid=qid, at=at, msg=message)
        send_message(msg_struct)
        return jsonify({'message': 'OK'}), 200
    
    @app.route('/service_endpoints', methods=['POST'])
    def register_service_endpoints():
        data = request.get_json()
        service_name = data.get('service_name')
        endpoints_info = data.get('endpoints_info')
        if service_name and endpoints_info:
            usages = list(endpoints_info.keys())
            for usage in usages:
                endpoint = endpoints_info[usage]
                serviceRegistry.add_service_endpoint(service_name, usage, endpoint)
            return jsonify({'message': 'Bot commands registered successfully'}), 200
        else:
            return jsonify({'message': 'Invalid request'}), 400
    
    @app.route('/health')
    def health_check():
        return 'OK'
