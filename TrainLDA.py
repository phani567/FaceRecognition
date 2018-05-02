

import sys, getopt, os
import numpy as np


def GetCurrentPath():
    return os.path.dirname(os.path.realpath(__file__))

def SetupPath():
    newpath = GetCurrentPath() + '/Utils'
    sys.path.append(newpath)
    
    newpath = GetCurrentPath() + '/Algo'
    sys.path.append(newpath)



def RunTrainLDA(infile, pcaFile, ldaFile):
    
    import cPickle

    fp = open(infile, "r")
    dataset = cPickle.load(fp)
    subjID = cPickle.load(fp)
    fp.close()
    
    
    pca = PCA(dataset)
    pca_proj = pca.compute()
    
    np.save(pcaFile, pca_proj)
    
    lda_proj = []
    lda = LDA(dataset, subjID, pca_proj)
    projData = lda.projectData()
    lda_proj = lda.train(projData)

    np.save(ldaFile, lda_proj)

    
############### main function #################    
if __name__ == '__main__':
    SetupPath()
    from define import *
    from PCA import *
    from LDA import *
    
    infile  = GetCurrentPath() + "/Data/train-dataset.pkl" 
    pcaFile = GetCurrentPath() + '/Models/PCA.npy'
    ldaFile = GetCurrentPath() + '/Models/LDA.npy'
    
    RunTrainLDA(infile, pcaFile, ldaFile)
