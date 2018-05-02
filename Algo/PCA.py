# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 11:00:31 2015

@author: ymlui
"""

import numpy as np
from pylab import *
from Img import *
from Display import *
from define import *

class PCA:
    def __init__(self, data, keep=0.98):
        print "PCA constructor"
        self.data = np.array(data)
        
        print self.data.shape
        
        DisplayImgset(self.data, DST_SIZE[1], DST_SIZE[0], 5, 4)

    def compute(self):
        print "Computing PCA..."
        datamean=mean(self.data,axis=0) 
        X=self.data-datamean
        [u,s,v]=np.linalg.svd(X,full_matrices=False)
        
        DisplayImgset(v, DST_SIZE[1], DST_SIZE[0], 5, 4)
#        sum_f = sum(s)
#        print sum_f
       
        sumval = 0.00
        for i in range(0, 1766):
            sumval += sum(math.pow(s[i],2))
#        print sumval 
        i=0
        opt=0.00
        while(opt<0.98*sumval):
            opt= opt+sum(math.pow(s[i],2))
            i=i+1
        print i-1
        pca_projection = v[:i-1,:]
        print pca_projection.shape

        return pca_projection