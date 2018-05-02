# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 11:00:31 2015

@author: ymlui
"""

import numpy as np
import scipy as sp
from pylab import *
from Img import *

class LDA:
    def __init__(self, dataset, labels, pca_proj=[]):
        self.data = np.array(dataset)
        self.pca_proj=pca_proj
        self.labels=np.array(labels)
        print "LDA constructor"
    def projectData(self):
        print "Shape of pca output :"+str(self.pca_proj.shape)
        print "Shape of input :"+str(self.data.shape)
        proj_transpose = np.transpose(self.pca_proj)
        
        #perform projection on data
        proj_data = np.dot(self.data,proj_transpose)
        
        print "Shape of projected data :"+str(proj_data.shape)
        
        
        return proj_data
        

    def train(self, data,dim=128):
        lda = []
        
        data_shape = data.shape
        print "Shape of projected data :"+str(data_shape)
        #print data.values
        train_data = np.array(self.labels)
        #print train_data.shape
        classes = np.unique(train_data)
        no_of_classes = len(classes)
        
        #calculating the mean vectors for each class
        mean_vectors = []
        i = 0
        for cl in classes:
            mean_vectors.append(np.mean(data[train_data==cl], axis=0))
            i = i + 1
        
        #calculating the global mean
        global_mean = np.mean(data,axis=0)
        
        #calculating the between class scatter matrix
        Scatter_Between = np.zeros((data_shape[1],data_shape[1]))
        i = 0
        for mean_vec in mean_vectors:  
            n = data[train_data==classes[i],:].shape[0]
            mean_vec = mean_vec.reshape(data_shape[1],1) # make column vector
            global_mean = global_mean.reshape(data_shape[1],1) # make column vector
            diff = (mean_vec - global_mean)
            diff_transpose = np.transpose(diff)
            temp = np.dot(diff,diff_transpose)
            Scatter_Between += n * temp
            i = i + 1
        print 'Betweeen-class Scatter Matrix:'
        print Scatter_Between
        
        #calculating the within class scatter matrix
        Scatter_Within = np.zeros((data_shape[1],data_shape[1]))
        i = 0
        for mean_vec in mean_vectors:  
            class_sc_mat = np.zeros((data_shape[1],data_shape[1]))
            for row in data[train_data==classes[i]]:
                row = row.reshape(data_shape[1],1) # make column vector
                mean_vec = mean_vec.reshape(data_shape[1],1) # make column vector
                diff = (row - mean_vec)
                diff_transpose = np.transpose(diff)
                temp = np.dot(diff,diff_transpose)
                class_sc_mat += temp
            Scatter_Within += class_sc_mat
            i = i + 1
        print 'Within-class Scatter Matrix:'
        print Scatter_Within
        
        #find the projection matrix using eigenvalue problem
        print 'find the projection matrix using eigenvalue problem'
        [eigVal, eigVec] = sp.linalg.eig(Scatter_Between,Scatter_Within)
        
        #reverse the order
        order = eigVal.argsort()[::-1]
        eigVal = eigVal[order]
        eigVec = eigVec[:,order]        
        
        #print eigVal
        #print eigVec
        
        #truncate the LDA dimension
        eigVec = eigVec[:,:dim]
        
        #re project back
        result = np.dot(np.transpose(eigVec),self.pca_proj)
        return result