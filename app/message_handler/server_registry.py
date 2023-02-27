import threading
from api.consul_client import consul_client
from datetime import datetime

class ServerRegistry:
    _servers = {}
    _lock = threading.Lock()

    @classmethod
    def add_server(cls, server_name, ip, port):
        # with cls._lock:
        cls._servers[server_name] = {
            'ip': ip,
            'port': port,
            'endpoints': {},
            'last_update_time': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        print(f"Registered server {server_name} at {ip}:{port}")

    @classmethod
    def remove_server(cls, server_name):
        # with cls._lock:
        cls._servers.pop(server_name, None)
        print(f"Removed server {server_name}")

    @classmethod
    def add_server_from_consul(cls, server_name):
        servers = consul_client.discover_servers(server_name)
        if servers:
            server_ip = servers[0][0]
            server_port = servers[0][1]
            cls.add_server(server_name, server_ip, server_port)
            return True
        return False

    @classmethod
    def get_server(cls, server_name):
        # with cls._lock:
        server_info = cls._servers.get(server_name)
        if server_info is None:
            if cls.add_server_from_consul(server_name):
                # with cls._lock:
                server_info = cls._servers.get(server_name)
        return server_info
    
    @classmethod
    def add_server_endpoint(cls, server_name, usage, endpoint):
        # with cls._lock:
        if server_name in list(cls._servers.keys()):
            cls._servers[server_name]['endpoints'][usage] = endpoint
        else:
            if cls.add_server_from_consul(server_name):
                cls._servers[server_name]['endpoints'][usage] = endpoint

    @classmethod
    def get_server_endpoint(cls, server_name, usage):
        # with cls._lock:
        try:
            return cls._servers[server_name]['endpoints'][usage]
        except KeyError:
            return None

    @classmethod
    def update_servers(cls):
        # do something to update servers

        # call this method again after a delay of 60 seconds
        threading.Timer(60, cls.update_servers).start()
