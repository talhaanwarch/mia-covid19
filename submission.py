# -*- coding: utf-8 -*-
"""
Created on Thu Jul  1 12:35:40 2021

@author: TAC
"""
#'non-covid':0,'covid':1

'''
first put all csv produced from inference files in respective folder
There are total seven models, so total 7 inference files are produced
There are 4 threshold techniques, so create 4 folders
Put the 7 csv files in each relevant folder.
This code ensembles all files, but can be done of single threshold level.
'''


import pandas as pd
from glob import glob
import numpy as np
from sklearn.metrics import accuracy_score
preds=[]
files=glob('thresh_10/*.csv')+glob('thresh_20/*.csv')+glob('thresh_30/*.csv')+glob('all_max/*.csv')
print(files)
for file in files:
    preds.append(pd.read_csv(file))
    
dfs = [df.set_index('ID') for df in preds]    
pred=pd.concat(dfs,axis=1)    
from scipy import stats
result=stats.mode(pred,axis=1)

df=pd.read_csv(file)
df.pred=result[0]

df.to_csv('all.csv')
df.pred=df.pred.map({0:'non-covid',1:'covid'})

n=df[df.pred=='non-covid']['ID']
c=df[df.pred=='covid']['ID']
n.to_frame().T.to_csv('submit/all/non-covid.csv',index=False,header=False)
c.to_frame().T.to_csv('submit/all/covid.csv',index=False,header=False)





















df=pd.read_csv('predictions/all/resnest14_0.88.csv')
df.pred=df.pred.map({0:'non-covid',1:'covid'})
print(df.pred.value_counts())

n=df[df.pred=='non-covid']['ID']
c=df[df.pred=='covid']['ID']
n.to_frame().T.to_csv('predictions/submission/best/non-covid.csv',index=False,header=False)
c.to_frame().T.to_csv('predictions/submission/best/covid.csv',index=False,header=False)










df2=pd.read_csv('predictions/sub_thresh5.csv')
print(df2.pred.value_counts())

df3=pd.read_csv('predictions/sub_thresh1.csv')
print(df3.pred.value_counts())


