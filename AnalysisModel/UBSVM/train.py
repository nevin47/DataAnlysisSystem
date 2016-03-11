# coding:utf-8
import HVS_EGM_SVM as HS
import web

def train(trainfile, testfile):
    scaler = 0 # 决定是否归一化数据
    MAXFEATURENUM = 5 # 设置指标离散最大值
    fpro = []
    proba, pre, initArray = HS.main(trainfile, testfile, scaler, MAXFEATURENUM, kernel='rbf', C=10.0, gamma= 1)
    for i in proba:
        fpro.append(i.max())
    return fpro, pre, initArray