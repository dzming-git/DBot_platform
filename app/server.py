# service.py
import time
from dbot import DBot

if __name__ == '__main__': 
    dbot = DBot()
    dbot.is_platform(True)
    dbot.set_routeInfo_config('conf/route_info/route_info.yaml')
    dbot.set_consulInfo_config('conf/consul_info/consul_info.yaml')
    dbot.start()
