#!/usr/bin/env python
#encoding:utf-8
import tornado.web

class MainHandler(tornado.web.RequestHandler):

    @tornado.web.asynchronous
    def get(self):
        self.write('hello world')
        self.finish()
