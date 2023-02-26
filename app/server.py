# server.py
import threading
import time
from conf.conf import Conf
from app.route.gocqhttp_routes import create_gocqhttp_app
from app.route.service_routes import craete_service_app

CONF_PATH = './conf/conf.yaml'

if __name__ == '__main__': 
    Conf._load_config(CONF_PATH)

    gocqhttp_app = create_gocqhttp_app()
    service_app = craete_service_app()
    
    ip = Conf.get_server_ip()
    gocqhttp_port = Conf.get_gocqhttp_port()
    service_port = Conf.get_service_port()
    threads = [
        threading.Thread(target=gocqhttp_app.run, kwargs={'host': ip, 'port': gocqhttp_port}),
        threading.Thread(target=service_app.run, kwargs={'host': ip, 'port': service_port})]
    for t in threads:
        t.start()
    while(1):
        time.sleep(100)