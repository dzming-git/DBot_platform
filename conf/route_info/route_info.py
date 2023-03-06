# route_info.py
import yaml
from utils.watch_config import watch_config
import copy
from utils.compare_dicts import compare_dicts

class RouteInfo:
    _config_path = ''
    _config = {}
    _api_gateway_conf_from_file = {}
    _message_broker_conf_from_file = {}

    @classmethod
    def load_config(cls, config_path, reload_flag=False):
        with open(config_path, 'r', encoding='utf-8') as f:
            config = yaml.safe_load(f)
            cls._api_gateway_conf_from_file = config.get('api_gateway', {})
            cls._message_broker_conf_from_file = config.get('message_broker', {})
            if not reload_flag:
                cls._config_path = config_path
                watch_config(config_path, cls.reload_config)

    @classmethod
    def reload_config(cls):
        config_old = copy.deepcopy(cls._config)
        cls.load_config(config_path=cls._config_path, reload_flag=True)
        config_new = copy.deepcopy(cls._config)
        added_dict, deleted_dict, modified_dict = compare_dicts(config_old, config_new)
        if added_dict or deleted_dict or modified_dict:
            from app.app import monitor_server_thread
            monitor_server_thread.restart()

    # API网关配置方法
    @classmethod
    def get_api_gateway_name(cls):
        return cls._api_gateway_conf_from_file.get('name')

    @classmethod
    def get_api_gateway_ip(cls):
        return cls._api_gateway_conf_from_file.get('ip')

    @classmethod
    def get_api_gateway_port(cls):
        return cls._api_gateway_conf_from_file.get('port')

    @classmethod
    def get_api_gateway_tags(cls):
        return cls._api_gateway_conf_from_file.get('tags')

    # 消息代理配置方法
    @classmethod
    def get_message_broker_name(cls):
        return cls._message_broker_conf_from_file.get('name')

    @classmethod
    def get_message_broker_ip(cls):
        return cls._message_broker_conf_from_file.get('ip')

    @classmethod
    def get_message_broker_port(cls):
        return cls._message_broker_conf_from_file.get('port')

    @classmethod
    def get_message_broker_tags(cls):
        return cls._message_broker_conf_from_file.get('tags')
    
    @classmethod
    def get_service_endpoints_info(cls) -> dict:
        return cls._message_broker_conf_from_file.get('endpoints')
    
    @classmethod
    def get_service_endpoint(cls, usage):
        return cls._message_broker_conf_from_file.get('endpoints')[usage]
    
    @classmethod
    def get_message_broker_consul_key(cls, usage):
        return cls._message_broker_conf_from_file.get('consul_key')[usage]
