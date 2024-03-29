#!/usr/bin/env python
#encoding:utf-8
import tornado.httpserver
import tornado.ioloop
import tornado.web
import tornado.options
from apps import Application
from tornado.options import define, options


define("port", default=8888, help="run on the given port",type=int)

def main():
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()


if __name__ == '__main__':
    main()

