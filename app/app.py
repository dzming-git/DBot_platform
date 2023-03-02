from flask import Flask

from api.api_gateway_routes import api_gateway_route_registration
from utils.service_discovery.consul_utils import api_gateway_deregister_service
from utils.service_discovery.consul_utils import api_gateway_register_consul

from api.message_broker_routes import message_broker_route_registration
from utils.service_discovery.consul_utils import message_broker_deregister_service
from utils.service_discovery.consul_utils import message_broker_register_consul, message_broker_endpoints_upload

def create_api_gateway_app():
    api_gateway_app = Flask(__name__)
    config = {
        **api_gateway_register_consul(api_gateway_app)
    }
    api_gateway_app.config.update(config)
    api_gateway_route_registration(api_gateway_app)
    return api_gateway_app

def destory_api_gateway_app(app):
    api_gateway_deregister_service(app)

def craete_message_broker_app():
    message_broker_app = Flask(__name__)
    config = {
        **message_broker_register_consul(message_broker_app)
    }
    message_broker_endpoints_upload()
    message_broker_app.config.update(config)
    message_broker_route_registration(message_broker_app)
    return message_broker_app

def destory_message_broker_app(app):
    message_broker_deregister_service(app)

