#!/usr/bin/env python
#encoding:utf-8
import tornado.web
import main.views

app = tornado.web.Application(
        handlers=[
            (r'/',main.views.MainHandler),
            
            ]
        )
