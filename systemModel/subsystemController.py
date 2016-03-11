# coding:utf-8

import web

def mainController(subsys, func, db, *keyword):
    subsysrender = web.template.render("templates/analysisTemplates/"+subsys, base='../base')
    if func == "train":
        # todo:坑!
        filename = db.select('CSVFile', what = "filename, type", where="subName='"+subsys+"'")
        filename2 = db.select('CSVFile', what = "filename, type", where="subName='"+subsys+"'")
        filename3 = db.select('CSVFile', what = "filename, type", where="subName='"+subsys+"'")
        return getattr(subsysrender,func)(filename,filename2,filename3)
    else:
        return getattr(subsysrender,func)()