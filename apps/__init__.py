#!/usr/bin/env python
#encoding:utf-8
import tornado.web
import main.views
import os
import motor


class Application(tornado.web.Application):
    def __init__(self):
        handlers=[
            (r'/',main.views.MainHandler),
            ]
        settings = dict(
            static_path = os.path.join(os.path.dirname(__file__),'..','static'),
            template_path = os.path.join(os.path.dirname(__file__),'..','templates'),
            debug=True,
           ) 
        tornado.web.Application.__init__(self,handlers,**settings)
        self.db = motor.MotorClient('localhost',27017)['zamax']

