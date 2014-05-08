#!/usr/bin/env python
#encoding:utf-8
from tornado import gen
from tornado.web import asynchronous
from tools.utils import BaseHandler

import json

class MainHandler(BaseHandler):

    @asynchronous
    @gen.coroutine
    def get(self):
        feature_dict = {}
        features = []
        module_dict = {}
        modules = []

        cursor = self.db.feature.find()
        for feature in (yield cursor.to_list(50)):
            features.append(feature)
        for feature in features:
            scenarios = []
            for scenario in feature['scenarios']:
                cursor = self.db.scenario.find({"_id":scenario})
                for scenario in (yield cursor.to_list(50)):
                    scenarios.append((scenario['_id'],scenario['name']))
            feature_dict[(feature['_id'],feature['name'])] = scenarios

        cursor = self.db.module.find()
        for module in (yield cursor.to_list(50)):
            modules.append(module)
        for module in modules:
            steps = []
            for step in module['steps']:
                cursor = self.db.step.find({"_id":step})
                for step in (yield cursor.to_list(50)):
                    steps.append((step['_id'],step['name']))
            module_dict[(module['_id'],module['name'])] = steps

        self.render('admin/index.html',features=feature_dict,modules=module_dict)


class ScenarioDetailsHandler(BaseHandler):

    @asynchronous
    @gen.coroutine
    def get(self,scenario_id):

        feature_dict = {}
        features = []
        module_dict = {}
        modules = []

        cursor = self.db.feature.find()
        for feature in (yield cursor.to_list(50)):
            features.append(feature)
        for feature in features:
            scenarios = []
            for scenario in feature['scenarios']:
                cursor = self.db.scenario.find({"_id":scenario})
                for scenario in (yield cursor.to_list(50)):
                    scenarios.append((scenario['_id'],scenario['name']))
            feature_dict[(feature['_id'],feature['name'])] = scenarios

        cursor = self.db.module.find()
        for module in (yield cursor.to_list(50)):
            modules.append(module)
        for module in modules:
            steps = []
            for step in module['steps']:
                cursor = self.db.step.find({"_id":step})
                for step in (yield cursor.to_list(50)):
                    steps.append((step['_id'],step['name']))
            module_dict[(module['_id'],module['name'])] = steps

        scenario_board = yield self.db.scenario.find_one({"_id":scenario_id})

        self.render('admin/details.html',
                scenario_title=scenario_board,
                steps_list=scenario_board['steps'],
                features=feature_dict,
                modules=module_dict)



    @asynchronous
    @gen.coroutine
    def post(self,scenario_id):
        value_list = self.get_arguments("value_list[]")
        scenario = yield self.db.scenario.find_one({"_id":scenario_id})
        scenario['steps'].extend(value_list)
        result = yield self.db.scenario.update({"_id":scenario_id},scenario)

        resp = {
                'status':200,
                'scenario_id':result,
                }
        self.set_header("content-type","application/json")
        self.write(json.dumps(resp))


class FeatureHandler(BaseHandler):

    @asynchronous
    @gen.coroutine
    def post(self):
        name = self.get_argument("feature_name") 
        result = yield self.db.feature.insert({
            "_id":self.get_id,
            "name":name,         
            "scenarios":[],
            })
        resp = {
                'status':200,
                'feature_id':result,
                }
        self.set_header("content-type","application/json")
        self.write(json.dumps(resp))


class ScenarioHandler(BaseHandler):

    @asynchronous
    @gen.coroutine
    def post(self):
        name = self.get_argument("scenario_name")
        feature_id = self.get_argument("feature_id")
        scenario_id = yield self.db.scenario.insert({
            "_id":self.get_id,
            "name":name,
            "steps":[],
            })
        feature = yield self.db.feature.find_one({"_id":feature_id})
        feature['scenarios'].append(scenario_id)
        result = yield self.db.feature.update({"_id":feature_id},feature)
        resp = {
                'status':200,
                'feature_id':result,
                'scenario_id':scenario_id,
                }
        self.set_header("content-type","application/json")
        self.write(json.dumps(resp))



















        

        


    

