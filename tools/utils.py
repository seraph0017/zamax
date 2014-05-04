#!/usr/bin/env python
#encoding:utf-8
import tornado.web
from bson.objectid import ObjectId

class BaseHandler(tornado.web.RequestHandler):

    @property
    def db(self):
        return self.application.db

    def get_current_user(self):
        user_id = self.get_secure_cookie("user")
        if not user_id:return None
        # todo db return didn't finish

    @property
    def get_id():
        return str(ObjectId())
