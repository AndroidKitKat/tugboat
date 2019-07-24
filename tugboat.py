#!/usr/bin/env python3

import tornado.ioloop
import tornado.web
import logging
import json

class MainHandler(tornado.web.RequestHandler):
    def initialize(self):
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.INFO)

    def post(self):
        self.logger.info('test')
        self.write("hi!")

def set_sail():
    return tornado.web.Application([
        (r"/", MainHandler),
        ])

if __name__ == "__main__":
    boat = set_sail()
    boat.listen(8888)
    tornado.ioloop.IOLoop.current().start()
