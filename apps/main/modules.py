#!/usr/bin/env python
#encoding:utf-8
import tornado.web

class ScenarioStepModule(tornado.web.UIModule):
    def render(self,step):
        return self.render_string('modules/scenario_step.html',step=step)

