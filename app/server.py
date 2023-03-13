# service.py
import time

from DBot_SDK import ConfigFromUser
ConfigFromUser.is_message_broker(True)

from DBot_SDK import server_thread

def load_conf():
    ConfigFromUser.RouteInfo_load_config('conf/route_info/route_info.yaml')

if __name__ == '__main__': 
    load_conf()
    server_thread.set_safe_start(True)
    if server_thread.start():
        while True:
            time.sleep(10)
