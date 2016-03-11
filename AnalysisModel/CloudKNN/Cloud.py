#coding:utf8

import numpy as np
from sklearn import neighbors
import csv

def CloudKNN(trainSample,cloud,predict,k):
    """Function which reads from the file and yields a generator"""
    #read cloud
    originReader = csv.reader(file(cloud,'rb'))
    List2 = []
    for line2 in originReader:
        List2.append(line2)

    # read test
    cloudReader =  csv.reader(file(trainSample,'rb'))
    numofMovie = 0
    numofPerson = 0
    for line in cloudReader:
        if (numofMovie == 0):
          numofMovie=len(line)
        numofPerson += 1
    print numofMovie,numofPerson

    preReader = csv.reader(file(predict,'rb'))

    List10 = []
    numofPre = 0
    for line3 in preReader:

           List10.append(line3)

           numofPre +=1

    List10 = np.matrix(List10)

    a = []
    for i in range(numofPre):
          a.append(-1)



       #errorValue = 0.0
       #testofnum  = 0
       #countofRight = 0

    predictScore = []
    for j in range(numofMovie):
          List1 = []  # train Array
          originReader =  csv.reader(file(trainSample,'rb'))
          for line in originReader:
             List1.append(line[j])
          L1 = []
          L2 = []
          for index,value in enumerate(List1):
                if value != '0':
                  L1.append(List1[index])      #score
                  L2.append(List2[index])      #cloud
          L1 = np.matrix(L1,dtype='float64')
          L2 = np.matrix(L2,dtype='float64')
          try:
            NewArray = np.hstack([L1.T,L2])
            X = NewArray[:, 1:4]
            label =NewArray[:, :1]
            y = np.ravel(label)
            try:
                n_neighbors = 15
                # we create an instance of Neighbours Classifier and fit the data.
                clf = neighbors.KNeighborsClassifier(n_neighbors, 'uniform')
                clf.fit(X, y)
                Z = clf.predict(List10)
                predictScore.append(Z)
            except ValueError,e:
                print e
                print j
                predictScore.append(a)
          except ValueError,e:
            print 'L1=',L1,'L2=',L2
            print j
            pass

    predictScore = np.array(predictScore)
    return predictScore

# trainSample = "/Users/nevin47/downloads/movie1.csv"           #读取训练文件
#
# cloud  = "/Users/nevin47/downloads/u2.csv"           #读取云模型
#
# predict  = "/Users/nevin47/downloads/u1.csv"           #读取测试文件
#
# k = 15                                                 #设置k值
#
# pre = CloudKNN(trainSample,cloud,predict,k)
#
# for i in pre:
#     for j in i:
#         print j
