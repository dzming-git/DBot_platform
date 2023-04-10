# service.py
from dbot import DBot

if __name__ == '__main__': 
    dbot = DBot(True)
    dbot.set_route_info_config('conf/route_info/route_info.yaml')
    dbot.set_consul_info_config('conf/consul_info/consul_info.yaml')
    dbot.set_mq_info_config('conf/mq_info/mq_info.yaml')
    dbot.start_bot()
