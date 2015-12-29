# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 19:04:00 2015

@author: timhou

1. Write a function mean(X) that returns the mean value of a list of numbers, as follows:
∑N xi x ̄= i=1
"""
import numpy as np
def np_mean(X):
    print(np.mean(X))

def mean(X):
    print(sum(X)/len(X))
        
        

mean([1,2,3,4,5])
mean([2,2,2,3,3])
mean([3,4,100,1000])
    
