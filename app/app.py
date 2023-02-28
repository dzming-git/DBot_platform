from flask import Flask

from api.bot_routes import bot_route_registration
from utils.service_discovery.consul_utils import bot_deregister_service
from utils.service_discovery.consul_utils import bot_register_consul

from api.message_broker_routes import message_broker_route_registration
from utils.service_discovery.consul_utils import message_broker_deregister_service
from utils.service_discovery.consul_utils import message_broker_register_consul

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

