from flask import Flask
import threading
from werkzeug.serving import make_server

from conf.route_info.route_info import RouteInfo

from api.api_gateway_routes import api_gateway_route_registration
from utils.service_discovery.consul_utils import api_gateway_deregister_service
from utils.service_discovery.consul_utils import api_gateway_register_consul

from api.message_broker_routes import message_broker_route_registration
from utils.service_discovery.consul_utils import message_broker_deregister_service
from utils.service_discovery.consul_utils import message_broker_register_consul, message_broker_endpoints_upload

class ApiGatewayServerThread(threading.Thread):
    def __init__(self):
        super().__init__(name='ApiGatewayServerThread')

    def init(self):
        self._server_name = 'DBot_api_gateway'
        self._app = Flask(__name__)
        config = {
            **api_gateway_register_consul(self._app)
        }
        self._app.config.update(config)
        api_gateway_route_registration(self._app)
        ip = RouteInfo.get_api_gateway_ip()
        port = RouteInfo.get_api_gateway_port()
        self._server = make_server(host=ip, port=port, app=self._app)
    
    def destory(self):
        api_gateway_deregister_service(self._app)
    
    def run(self):
        print(f'{self._server_name}已运行')
        self._server.serve_forever()
        print(f'{self._server_name}已结束')
    
    def stop(self):
        self._server.shutdown()
    
    def restart(self):
        print(f'{self._server_name}正在重启')
        self.stop()
        self.init()
        self.start()

class MessageBrokerServerThread(threading.Thread):
    def __init__(self):
        super().__init__(name='MessageBrokerServerThread')

    def init(self):
        self._server_name = 'DBot_message_broker'
        self._app = Flask(__name__)
        config = {
            **message_broker_register_consul(self._app)
        }
        message_broker_endpoints_upload()
        self._app.config.update(config)
        message_broker_route_registration(self._app)
        ip = RouteInfo.get_message_broker_ip()
        port = RouteInfo.get_message_broker_port()
        self._server = make_server(host=ip, port=port, app=self._app)
    
    def destory(self):
        message_broker_deregister_service(self._app)
    
    def run(self):
        print(f'{self._server_name}已运行')
        self._server.serve_forever()
        print(f'{self._server_name}已结束')
    
    def stop(self):
        self._server.shutdown()
    
    def restart(self):
        print(f'{self._server_name}正在重启')
        self.stop()
        self.init()
        self.start()

api_gateway_server_thread = ApiGatewayServerThread()
message_broker_server_thread = MessageBrokerServerThread()