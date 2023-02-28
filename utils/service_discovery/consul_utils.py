from utils.service_discovery.consul_client import consul_client
from conf.route_info.route_info import RouteInfo

def bot_register_consul(app):
    '''
    服务开启前,注册consul
    '''
    service_name = RouteInfo.get_bot_name()
    port = RouteInfo.get_bot_port()
    tags = RouteInfo.get_bot_tags()
    bot_id = consul_client.register_service(service_name, port, tags)
    config = {
        'bot_id': bot_id
    }
    return config

def bot_deregister_service(app):
    '''
    服务结束后,注销consul
    '''
    bot_id = app.config['bot_id']
    consul_client.deregister_service(bot_id)

def message_broker_register_consul(app):
    '''
    服务开启前,注册consul
    '''
    service_name = RouteInfo.get_message_broker_name()
    port = RouteInfo.get_message_broker_port()
    service_tags = RouteInfo.get_bot_tags()
    message_broker_id = consul_client.register_service(service_name, port, service_tags)
    config = {
        'message_broker_id': message_broker_id
    }
    return config

def message_broker_deregister_service(app):
    '''
    服务结束后,注销consul
    '''
    message_broker_id = app.config['message_broker_id']
    consul_client.deregister_service(message_broker_id)
