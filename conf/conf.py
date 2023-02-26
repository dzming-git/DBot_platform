import yaml

class Conf:
    _conf = {}

    @classmethod
    def _load_config(cls, config_path):
        with open(config_path) as f:
            cls._conf = yaml.safe_load(f)

    @classmethod
    def get_server_name(cls):
        return cls._conf.get('server', {}).get('name')

    @classmethod
    def get_server_ip(cls):
        return cls._conf.get('server', {}).get('ip')

    @classmethod
    def get_server_port(cls):
        return cls._conf.get('server', {}).get('port')

    @classmethod
    def get_server_tags(cls):
        return cls._conf.get('server', {}).get('tags')
