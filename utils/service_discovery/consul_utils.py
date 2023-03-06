from utils.service_discovery.consul_client import consul_client
from conf.route_info.route_info import RouteInfo

def api_gateway_register_consul(app):
    '''
    服务开启前,注册consul
    '''
    service_name = RouteInfo.get_api_gateway_name()
    port = RouteInfo.get_api_gateway_port()
    tags = RouteInfo.get_api_gateway_tags()
    api_gateway_id = consul_client.register_service(service_name, port, tags)
    config = {
        'api_gateway_id': api_gateway_id
    }
    return config

def api_gateway_deregister_service(app):
    '''
    服务结束后,注销consul
    '''
    api_gateway_id = app.config['api_gateway_id']
    consul_client.deregister_service(api_gateway_id)

def message_broker_register_consul(app):
    '''
    服务开启前,注册consul
    '''
    service_name = RouteInfo.get_message_broker_name()
    port = RouteInfo.get_message_broker_port()
    service_tags = RouteInfo.get_api_gateway_tags()
    message_broker_id = consul_client.register_service(service_name, port, service_tags)
    config = {
        'message_broker_id': message_broker_id
    }
    return config

def message_broker_endpoints_upload():
    service_endpoints_info = RouteInfo.get_service_endpoints_info()
    message_broker_consul_key = RouteInfo.get_message_broker_consul_key('message_broker_endpoints')
    message_broker_endpoints_dict = {
        message_broker_consul_key: service_endpoints_info
    }
    consul_client.update_key_value(message_broker_endpoints_dict)

def message_broker_deregister_service(app):
    '''
    服务结束后,注销consul
    '''
    message_broker_id = app.config['message_broker_id']
    consul_client.deregister_service(message_broker_id)
