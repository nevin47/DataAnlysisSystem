#coding:utf8

import numpy as np
from sklearn import neighbors
import csv


def knn(originFile,cloudFile,testFile,k):

   """Function which reads from the file and yields a generator"""
   #read cloud
   originReader = csv.reader(file(cloudFile,'rb'))
   List2 = []
   for line2 in originReader:
	List2.append(line2)

   # read test
   cloudReader =  csv.reader(file(originFile,'rb'))
   MaxColumn = 0
   MaxLine = 0
   for line in cloudReader:
      if (MaxColumn == 0):

        MaxColumn=len(line)
      MaxLine += 1

   print MaxColumn,MaxLine
   MovieMatrix = np.zeros([MaxLine,MaxColumn])

   test = csv.reader(file(testFile, 'rb'))
   for j in test:
       MovieMatrix[(int(j[0])-1)][(int(j[1])-1)] = int(j[2])

   cloudReader =  csv.reader(file(originFile,'rb'))
   numofMovie = 0
   errorValue = 0.0
   testofnum  = 0
   countofRight = 0
   for line in cloudReader:
      if (numofMovie == 0):
         numofMovie=len(line)
        
   for j in range(numofMovie):
      List1 = []  # train Array
      cloudReader =  csv.reader(file(originFile,'rb'))
      for line in cloudReader:
         List1.append(line[j])
      L1 = []
      L2 = []
      L3 = MovieMatrix[:,j]  # Test Movie
      for index,value in enumerate(List1):
            if  value != '0' :
              L1.append(List1[index])      #score
              L2.append(List2[index])      #cloud
            
      L1 = np.matrix(L1,dtype='float64')
      L2 = np.matrix(L2,dtype='float64')
      try:
         NewArray = np.hstack([L1.T,L2])
      except ValueError,e:
        print 'L1=',L1,'L2=',L2
        print j
        pass
            
      X =NewArray[:,1 :4]

      label =NewArray[:, :1]

      y = np.ravel(label)
    
    
      L4 = []
      L5 = []
      for index,value in enumerate(L3):
       
        if value != 0 :
            L4.append(L3[index])         #testscore
            L5.append(List2[index])      # cloud    
    
    
      L4 = np.matrix(L4,dtype='float64')
      L5 = np.matrix(L5,dtype='float64')

      try:
         testcloud = np.hstack([L4.T,L5])
      except ValueError,e:
         print  'L4','=',L4,'L5=',L5
         print j
         pass

      for i in testcloud:
         testofnum += 1

      m = testcloud[:,1 :4]

      Xlabel = testcloud[:, :1]

      n = np.ravel(Xlabel)




      try:
        n_neighbors = k
        # we create an instance of Neighbours Classifier and fit the data.
        clf = neighbors.KNeighborsClassifier(n_neighbors, 'uniform')
        clf.fit(X, y)



        r = 0
        Z = clf.predict(m)
        k = abs(Z-n)
        for i in k :
            if(int(i)==0):
                r += 1
        countofRight += r
        errorValue += np.sum(k)
      except ValueError,e:
         print e
         print j
         pass
          # try:
         #     errorValue += k               #累加误差
        # except ValueError,e:
       #     print e
      #     print k



   avg = errorValue/testofnum

   accourty = float(countofRight)/testofnum

   print 'n_neighbors=',n_neighbors

   print 'avg=',avg

   print 'accourty',accourty

   return avg,accourty

if __name__ == "__knn__":
     originFile = "C:\Users\ZHOUXINMIN\Desktop\movie\movie.csv"           #读取训练文件
     
     cloudFile  = "C:\Users\ZHOUXINMIN\Desktop\movie\u2.csv"           #读取云模型
     
     testFile   = "C:\Users\ZHOUXINMIN\Desktop\movie\est.csv"           #读取测试文件
     
     k = 15                                                 #设置k值
     
     avgError,acc = knn(originFile,cloudFile,testFile,k)
     
     print "avgError:%f,acc:%f",avgError,acc