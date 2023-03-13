# service.py
import time
from conf.route_info.route_info import RouteInfo
from app.app import message_broker_server_thread
from app.message_handler.message_handler import message_handler_thread

def load_conf():
    RouteInfo.load_config('conf/route_info/route_info.yaml')

if __name__ == '__main__': 
    load_conf()
    message_broker_server_thread.init()
    message_broker_server_thread.start()
    message_handler_thread.start()

    while(1):
        time.sleep(100)
