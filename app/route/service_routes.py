# server_routes.py
from flask import Flask, request
from app.message_handler import message_handler
from app.message_handler.func_dict import func_dict

def craete_server_app():
    server_app = Flask(__name__)

    @server_app.route('/func_dict', methods=['POST'])
    def func_dict_recv():
        if request.method == 'POST':
            message = request.json
            func_dict = {**func_dict, **message.get('func_dict')}
            print(func_dict)
            return 'OK'
        else:
            return 'Method Not Allowed', 405
    
    return server_app