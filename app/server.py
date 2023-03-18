# service.py
import time

from DBot_SDK import ConfigFromUser
ConfigFromUser.is_message_broker(True)
ConfigFromUser.RouteInfo_load_config('conf/route_info/route_info.yaml')
ConfigFromUser.ConsulInfo_load_config('conf/consul_info/consul_info.yaml')

from DBot_SDK import server_thread

if __name__ == '__main__': 
    server_thread.set_safe_start(True)
    if server_thread.start():
        while True:
            time.sleep(10)
