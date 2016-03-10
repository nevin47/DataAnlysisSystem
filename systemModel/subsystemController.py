# coding:utf-8

import web

def mainController(subsys, func, *keyword):
    subsys = web.template.render("templates/analysisTemplates/"+subsys, base='../base')
    return getattr(subsys,func)()