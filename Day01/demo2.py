
## read config file: demo_config.ini

from configparser import ConfigParser
import os

HERE = os.path.abspath(os.path.dirname(__file__))
CONFIG_FILE = os.path.join(HERE, "demo_config.ini")


def main(cfg):
    
    print(cfg.sections())
    print(cfg['thingworx'].get("server_name"))
    print(cfg.get('server','signature'))


if __name__ == '__main__':
    cfg = ConfigParser()
    cfg.read(CONFIG_FILE)
    main(cfg)