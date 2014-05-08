#!/usr/bin/env python
#encoding:utf-8
from pymongo import MongoClient
from bson.objectid import ObjectId

def get_id():
    return str(ObjectId())
client = MongoClient()
db = client['zamax']

def init_db():
    step1_id = get_id()
    step2_id = get_id()
    step3_id = get_id()
    step4_id = get_id()
    scenario1_id = get_id()
    scenario2_id = get_id()
    scenario3_id = get_id()
    scenario4_id = get_id()
    feature1_id = get_id()
    feature2_id = get_id()
    feature3_id = get_id()
    feature4_id = get_id()
    module1_id = get_id()
    module2_id = get_id()
    module3_id = get_id()
    module4_id = get_id()
    db.step.drop()
    db.step.insert({
        "_id":step1_id,
        "name":"login",
        })
    db.step.insert({
        "_id":step2_id,
        "name":"logout",
        })
    db.step.insert({
        "_id":step3_id,
        "name":"verify",
        })
    db.step.insert({
        "_id":step4_id,
        "name":"kill",
        })
    db.scenario.drop()
    db.scenario.insert({
        "_id":scenario1_id,
        "name":"admin",
        "steps":[
            "login","logout","verify","kill"
            ]
        })
    db.scenario.insert({
        "_id":scenario2_id,
        "name":"account",
        "steps":[
            "login","logout","verify","kill"
            ]
        })
    db.scenario.insert({
        "_id":scenario3_id,
        "name":"normal",
        "steps":[
            "login","logout","verify","kill"
            ]
        })
    db.scenario.insert({
        "_id":scenario4_id,
        "name":"lower",
        "steps":[
            "login","logout","verify","kill"
            ]
        })
    db.feature.drop()
    db.feature.insert({
        "_id":feature1_id,
        "name":"test1",
        "scenarios":[
            scenario1_id,scenario2_id,scenario3_id,scenario4_id
            ]
        })
    db.feature.insert({
        "_id":feature2_id,
        "name":"test2",
        "scenarios":[
            scenario1_id,scenario2_id,scenario3_id,scenario4_id
            ]
        })
    db.feature.insert({
        "_id":feature3_id,
        "name":"test3",
        "scenarios":[
            scenario1_id,scenario2_id,scenario3_id,scenario4_id
            ]
        })
    db.feature.insert({
        "_id":feature4_id,
        "name":"test4",
        "scenarios":[
            scenario1_id,scenario2_id,scenario3_id,scenario4_id
            ]
        })
    db.module.drop()
    db.module.insert({
        "_id":module1_id,
        "name":"module1",
        "steps":[
            step1_id 
            ]
        })
    db.module.insert({
        "_id":module2_id,
        "name":"module2",
        "steps":[
            step2_id 
            ]
        })
    db.module.insert({
        "_id":module3_id,
        "name":"module3",
        "steps":[
            step3_id 
            ]
        })
    db.module.insert({
        "_id":module4_id,
        "name":"module4",
        "steps":[
            step4_id 
            ]
        })

if __name__ == "__main__":
    init_db()

