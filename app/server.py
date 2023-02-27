# server.py
import threading
import time
from conf.conf import Conf
from app.route.bot_routes import create_bot_app
from app.route.message_broker_routes import craete_message_broker_app

CONF_PATH = './conf/conf.yaml'

if __name__ == '__main__': 
    Conf._load_config(CONF_PATH)

    bot_app = create_bot_app()
    message_broker_app = craete_message_broker_app()
    
    ip = Conf.get_bot_ip()
    bot_port = Conf.get_bot_port()
    message_broker_port = Conf.get_message_broker_port()
    threads = [
        threading.Thread(target=bot_app.run, kwargs={'host': ip, 'port': bot_port}),
        threading.Thread(target=message_broker_app.run, kwargs={'host': ip, 'port': message_broker_port})]
    for t in threads:
        t.start()
    while(1):
        time.sleep(100)
