import sys, getopt, os
import numpy as np
from pylab import *


def GetCurrentPath():
    return os.path.dirname(os.path.realpath(__file__))

def SetupPath():
    newpath = GetCurrentPath() + '/Utils'
    sys.path.append(newpath)
    
    newpath = GetCurrentPath() + '/Algo'
    sys.path.append(newpath)


    
def ComputeMatch(inquire, dataset):
    q = np.tile(inquire, (np.array(dataset).shape[0],1))
    d = (q - dataset)
               
    dist = np.zeros((np.array(dataset).shape[0],1))     
    for j in range(0,np.array(dataset).shape[0],1):
        dist[j] = np.linalg.norm(d[j,:])
                
    return dist            

    

def RunTest(inFile, projFile):
        
    import cPickle    
    fp = open(inFile, "r")
    querySet = cPickle.load(fp)
    targetSet = cPickle.load(fp)
    queryID = cPickle.load(fp)
    targetID = cPickle.load(fp)
    fp.close()    

    
    proj = np.load(projFile)
    proj_transpose = np.transpose(proj)
    
    #perform projection on query set
    query = np.array(querySet)
    query_new = np.dot(query,proj_transpose)
    
    #perform projection on target set
    target = np.array(targetSet)
    target_new = np.dot(target,proj_transpose)
    
    print query_new.shape
    print target_new.shape
    
    # normalize query
    query_length = len(query_new)
    i = 0
    query = np.zeros((query_new.shape[0], query_new.shape[1]))
    print query.shape
    while i < query_length:
        row_norm = np.linalg.norm(query_new[i,:])
        query[i,:] = query_new[i,:]/row_norm
        i = i + 1
    
    
    # normalize target
    target_length = len(target_new)
    i = 0
    target = np.zeros((target_new.shape[0], target_new.shape[1]))
    while i < target_length:
        row_norm = np.linalg.norm(target_new[i,:])
        target[i,:] = target_new[i,:]/row_norm
        i = i + 1
    
    with open("Output.txt", "w") as output_file:
        for i in range(0,np.array(querySet).shape[0],1):
            
            dist = ComputeMatch(query[i,:], target)
            match = 1 * np.array(queryID[i] == np.array(targetID))
        
            for j in range(0,np.array(targetSet).shape[0],1):
                output_file.write("%d %f\n" % (match[j], dist[j]))    


############### main function #################
if __name__ == '__main__':
    SetupPath()
    from define import *
    
    infile = GetCurrentPath() + '/Data/test-dataset.pkl'
    pcaFile = GetCurrentPath() + '/Models/PCA.npy'
    ldaFile = GetCurrentPath() + '/Models/LDA.npy'
    
    ## TP = 35.5%
    #RunTest(infile, pcaFile)
    ## TP = 72.7%
    RunTest(infile, ldaFile)