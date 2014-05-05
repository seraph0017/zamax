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
            (r'/feature/',main.views.FeatureHandler),
            (r'/(.*?)',main.views.ScenarioDetailsHandler),
            ]
        settings = dict(
            static_path = os.path.join(os.path.dirname(__file__),'..','static'),
            template_path = os.path.join(os.path.dirname(__file__),'..','templates'),
            cookie_secret="1231jfijaosjdfijasojdfijaosjdg123",
            xsrf_cookies=True,
            debug=True,
           ) 
        tornado.web.Application.__init__(self,handlers,**settings)
        self.db = motor.MotorClient('localhost',27017)['zamax']

