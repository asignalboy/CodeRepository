#!/usr/bin/python
def loadDataSet(fileName):
    dataMat=[];labelMat=[]
    fr=open(fileName)
    for line in fr.readlines():
        lineArr=line.strip().split()
        dataMat.append()