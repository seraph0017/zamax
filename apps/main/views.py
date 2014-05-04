#!/usr/bin/env python
#encoding:utf-8
from tornado import gen
from tornado.web import asynchronous
from tools.utils import BaseHandler


class MainHandler(BaseHandler):

    @asynchronous
    @gen.coroutine
    def get(self):
        feature_dict = {}
        features = []
        module_dict = {}
        modules = []

        cursor = self.db.feature.find()
        for feature in (yield cursor.to_list(10)):
            features.append(feature)
        for feature in features:
            scenarios = []
            for scenario in feature['scenarios']:
                cursor = self.db.scenario.find({"_id":scenario})
                for scenario in (yield cursor.to_list(10)):
                    scenarios.append((scenario['_id'],scenario['name']))
            feature_dict[(feature['_id'],feature['name'])] = scenarios

        cursor = self.db.module.find()
        for module in (yield cursor.to_list(10)):
            modules.append(module)
        for module in modules:
            steps = []
            for step in module['steps']:
                cursor = self.db.step.find({"_id":step})
                for step in (yield cursor.to_list(10)):
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
        for feature in (yield cursor.to_list(10)):
            features.append(feature)
        for feature in features:
            scenarios = []
            for scenario in feature['scenarios']:
                cursor = self.db.scenario.find({"_id":scenario})
                for scenario in (yield cursor.to_list(10)):
                    scenarios.append((scenario['_id'],scenario['name']))
            feature_dict[(feature['_id'],feature['name'])] = scenarios

        cursor = self.db.module.find()
        for module in (yield cursor.to_list(10)):
            modules.append(module)
        for module in modules:
            steps = []
            for step in module['steps']:
                cursor = self.db.step.find({"_id":step})
                for step in (yield cursor.to_list(10)):
                    steps.append((step['_id'],step['name']))
            module_dict[(module['_id'],module['name'])] = steps

        scenario_board = yield self.db.scenario.find_one({"_id":scenario_id})
        steps_list = []
        for step in scenario_board['steps']:
            cursor = self.db.step.find({"_id":step})
            for step in (yield cursor.to_list(50)):
                steps_list.append((step['_id'],step['name']))

        self.render('admin/details.html',
                scenario_title=scenario_board['name'],
                steps_list=steps_list,
                features=feature_dict,
                modules=module_dict)




class FeatureHandler(BaseHandler):

    @asynchronous
    @gen.coroutine
    def post(self):
        id = self.get_argument(self.get_id)
        name = self.get_argument("name") 
        resp = yield self.db.feature.insert({
            "_id":id,
            "name":name})
        return
        






















        

        


    

