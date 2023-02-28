from flask import Flask

from api.bot_routes import route_registration as bot_route_registration
from api.bot_routes import deregister_service as bot_deregister_service
from api.bot_routes import register_consul as bot_register_consul

from api.message_broker_routes import route_registration as message_broker_route_registration
from api.message_broker_routes import deregister_service as message_broker_deregister_service
from api.message_broker_routes import register_consul as message_broker_register_consul

def create_bot_app():
    bot_app = Flask(__name__)
    config = {
        **bot_register_consul(bot_app)
    }
    bot_app.config.update(config)
    bot_route_registration(bot_app)
    return bot_app

def destory_bot_app(app):
    bot_deregister_service(app)

def craete_message_broker_app():
    message_broker_app = Flask(__name__)
    config = {
        **message_broker_register_consul(message_broker_app)
    }
    message_broker_app.config.update(config)
    message_broker_route_registration(message_broker_app)
    return message_broker_app

def destory_message_broker_app(app):
    message_broker_deregister_service(app)

