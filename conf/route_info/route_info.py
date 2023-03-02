# route_info.py
import yaml

class RouteInfo:
    _api_gateway_conf = {}
    _message_broker_conf = {}

    @classmethod
    def _load_config(cls, config_path):
        with open(config_path, 'r', encoding='utf-8') as f:
            config = yaml.safe_load(f)
            cls._api_gateway_conf = config.get('api_gateway', {})
            cls._message_broker_conf = config.get('message_broker', {})

    # API网关配置方法
    @classmethod
    def get_api_gateway_name(cls):
        return cls._api_gateway_conf.get('name')

    @classmethod
    def get_api_gateway_ip(cls):
        return cls._api_gateway_conf.get('ip')

    @classmethod
    def get_api_gateway_port(cls):
        return cls._api_gateway_conf.get('port')

    @classmethod
    def get_api_gateway_tags(cls):
        return cls._api_gateway_conf.get('tags')

    # 消息代理配置方法
    @classmethod
    def get_message_broker_name(cls):
        return cls._message_broker_conf.get('name')

    @classmethod
    def get_message_broker_ip(cls):
        return cls._message_broker_conf.get('ip')

    @classmethod
    def get_message_broker_port(cls):
        return cls._message_broker_conf.get('port')

    @classmethod
    def get_message_broker_tags(cls):
        return cls._message_broker_conf.get('tags')
    
    @classmethod
    def get_service_endpoints_info(cls) -> dict:
        return cls._message_broker_conf.get('endpoints')
    
    @classmethod
    def get_service_endpoint(cls, usage):
        return cls._message_broker_conf.get('endpoints')[usage]
    
    @classmethod
    def get_message_broker_consul_key(cls, usage):
        return cls._message_broker_conf.get('consul_key')[usage]
