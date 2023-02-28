# service.py
import threading
import time
from conf.route_info.route_info import RouteInfo
from app.app import create_bot_app
from app.app import craete_message_broker_app
from app.message_handler.message_handler import message_forwarding

def load_conf():
    RouteInfo._load_config('conf/route_info/route_info.yaml')

if __name__ == '__main__': 
    load_conf()

    bot_app = create_bot_app()
    message_broker_app = craete_message_broker_app()
    
    ip = RouteInfo.get_bot_ip()
    bot_port = RouteInfo.get_bot_port()
    message_broker_port = RouteInfo.get_message_broker_port()
    threads = [
        threading.Thread(target=message_forwarding),
        threading.Thread(target=bot_app.run, kwargs={'host': ip, 'port': bot_port}),
        threading.Thread(target=message_broker_app.run, kwargs={'host': ip, 'port': message_broker_port})]
    for t in threads:
        t.start()
    while(1):
        time.sleep(100)
