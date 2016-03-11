# coding:utf-8

import web
import UBSVM.train as UBSVMtrain
import CloudKNN.Cloud as CKNN

def mainController(dataget):
    subsys = dataget.subsys
    func = dataget.func
    if(subsys == "UBSVM"):
        # filename = '/Users/nevin47/Desktop/Project/Academic/Code/Python/DataAnlysisSystem/DataAnlysisSystem/static/csv/HeartTrain.csv' # 设置读取文件
        # filename1 = '/Users/nevin47/Desktop/Project/Academic/Code/Python/DataAnlysisSystem/DataAnlysisSystem/static/csv/HeartTest.csv'
        filename = '/Users/nevin47/Desktop/Project/Academic/Code/Python/DataAnlysisSystem/DataAnlysisSystem/static/csv/' + dataget.trainfilename
        filename1 = '/Users/nevin47/Desktop/Project/Academic/Code/Python/DataAnlysisSystem/DataAnlysisSystem/static/csv/' + dataget.testfilename
        proba, pre, initArray = UBSVMtrain.train(filename, filename1)
        show = web.template.render("templates/analysisTemplates/"+subsys, base='../base')
        return getattr(show, func)(proba, pre, initArray)
    elif subsys == "CloudKNN":
        filename = '/Users/nevin47/Desktop/Project/Academic/Code/Python/DataAnlysisSystem/DataAnlysisSystem/static/csv/' + dataget.traincloudfilename
        filename1 = '/Users/nevin47/Desktop/Project/Academic/Code/Python/DataAnlysisSystem/DataAnlysisSystem/static/csv/' + dataget.scorefilename
        filename2 = '/Users/nevin47/Desktop/Project/Academic/Code/Python/DataAnlysisSystem/DataAnlysisSystem/static/csv/' + dataget.testfilename
        k = dataget.kvalue
        prea = CKNN.CloudKNN(filename1, filename, filename2, k)
        show = web.template.render("templates/analysisTemplates/"+subsys, base='../base')
        return getattr(show, func)(prea)
