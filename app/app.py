from flask import Flask
import threading
from werkzeug.serving import make_server

from conf.route_info.route_info import RouteInfo

from api.message_broker_routes import message_broker_route_registration
from utils.service_discovery.consul_utils import message_broker_deregister_service
from utils.service_discovery.consul_utils import message_broker_register_consul, message_broker_endpoints_upload

class MessageBrokerServerThread(threading.Thread):
    def __init__(self):
        super().__init__(name='MessageBrokerServerThread')

    def init(self):
        self._server_name = 'DBot_message_broker'
        self._app = Flask(__name__)
        config = {
            **message_broker_register_consul(self._app)
        }
        message_broker_endpoints_upload()  # TODO
        self._app.config.update(config)
        message_broker_route_registration(self._app)  # TODO
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

message_broker_server_thread = MessageBrokerServerThread()