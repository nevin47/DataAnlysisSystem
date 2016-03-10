# coding:utf-8
__author__ = 'nevin47'

import numpy as np
import basefunc.basefunc as basef
import entropy.entropy as en
import HVS.HVS as Hyper
import svm.SVM_Core as HSVM
import random
from scipy.optimize import minimize
import matplotlib.pyplot as pl


def main(filename, testfilename, scaler, MAXFEATURENUM, **svmParameter):
    kernel = svmParameter['kernel']
    C = svmParameter['C']
    gamma = svmParameter['gamma']

    dataSet1, labels1, dataSet2, labels2 = basef.readData(filename, scaler)

    initArray = en.featureSample(dataSet1, labels1, dataSet2, labels2, MAXFEATURENUM)
    print "初始化指标:",initArray

    '''
    preTestX = np.vstack([dataSet1,dataSet2])
    preLabels = np.hstack([labels1,labels2])
    '''


    # Todo:此处可以直接调用遗传算法模块了 -- By nevin47
    data = (dataSet1, labels1, dataSet2, labels2, initArray)
    arrayValue = [0.6, 0.5, 0.4, 0.3, 0.2, 0.1, 1]
    train_X, train_label = Hyper.balanceDataforGA(arrayValue,*data)

    clf = HSVM.trainSVM(train_X, train_label, kernel=kernel, C=C, gamma= gamma)

    pre = HSVM.testSVM(preTestX , clf)
    proba = HSVM.testSVMwithProb(preTestX, clf)

    return proba, pre, initArray

if __name__ == "__main__":
    # demo
    filename1 = '/Users/nevin47/Desktop/Project/Academic/Code/Python/SVM/UnbalancedDataSVM/DataSet/test/wpbc.csv' # 设置读取文件
    filename = '/Users/nevin47/Desktop/Project/Academic/Code/Python/SVM/UnbalancedDataSVM/DataSet/CreditOriginData2.csv'
    # filename = '/Users/nevin47/Desktop/Project/Academic/Code/Python/SVM/UnbalancedDataSVM/DataSet/Heart2.csv'
    scaler = 1 # 决定是否归一化数据
    MAXFEATURENUM = 5 # 设置指标离散最大值
    SUMG = []
    SUMF = []
    for i in range(30):
        tempG,tempF = main(filename, scaler, MAXFEATURENUM, kernel='rbf', C=15.0, gamma= 1)
        SUMG.append(tempG)
        SUMF.append(tempF)
    print "AVG-G: %f,AVG-F %f",sum(SUMG)/30.0,sum(SUMF)/30.0

# test

# print dataSet1