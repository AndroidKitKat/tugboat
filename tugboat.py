#!/usr/bin/env python3

import tornado.ioloop
import tornado.web
import logging
import json
import toml
import os

class MainHandler(tornado.web.RequestHandler):
    def initialize(self):
        self.logger = logging.getLogger('tugboat')
        self.logger.setLevel(logging.INFO)

    def post(self):
        self.logger.info('test')
        self.write("hi!")

def set_sail():
    return tornado.web.Application([
        (r"/", MainHandler),
        ])

def load_config(config_name='config.toml'):
    config = {}
    if not os.path.isfile(config_name):
        print('Missing config.toml!\nDid you make sure to rename config.toml.default?')
        exit(1)
    with open(config_name, 'r', encoding='utf-8') as fp:
        config.update(toml.load(fp))
    
    return config


if __name__ == "__main__":
    config = load_config()
    print(config)
    # boat = set_sail()
    # boat.listen(8888)
    # tornado.ioloop.IOLoop.current().start()
