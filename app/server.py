# server.py
from conf.conf import Conf
from app.route.main_routes import create_main_app, destory_main_app

CONF_PATH = './conf/conf.yaml'

if __name__ == '__main__': 
    Conf._load_config(CONF_PATH)

    main_app = create_main_app()
    ip = Conf.get_server_ip()
    port = Conf.get_server_port()
    main_app.run(host=ip, port=port, debug=True)
    destory_main_app(main_app)
