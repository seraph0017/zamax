#!/usr/bin/env python
#encoding:utf-8
import tornado.httpserver
import tornado.ioloop
import tornado.web
from apps import app



if __name__ == '__main__':
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(8888)
    tornado.ioloop.IOLoop.instance().start()

