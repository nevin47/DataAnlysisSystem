# coding:utf-8

import web
import imp
import UBSVM.train as UBSVMtrain

def mainController(dataget):
    subsys = dataget.subsys
    func = dataget.func
    if(subsys == "UBSVM"):
        filename = '/Users/nevin47/Desktop/Project/Academic/Code/Python/DataAnlysisSystem/DataAnlysisSystem/static/csv/HeartTrain.csv' # 设置读取文件
        filename1 = '/Users/nevin47/Desktop/Project/Academic/Code/Python/DataAnlysisSystem/DataAnlysisSystem/static/csv/HeartTest.csv'
        proba, pre, initArray = UBSVMtrain.train(filename, filename1)
        #print proba, pre, initArray
        show = web.template.render("templates/analysisTemplates/"+subsys, base='../base')
        return getattr(show, func)(proba, pre, initArray)
