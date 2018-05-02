
import sys, getopt, os

def GetCurrentPath():
    return os.path.dirname(os.path.realpath(__file__))

def SetupPath():
    newpath = GetCurrentPath() + '/Utils'
    sys.path.append(newpath)
    
    
############### main function #################
if __name__ == '__main__':
    SetupPath()
    from ComputeROC import *
    
    roc = ComputeDistROC('Output.txt')
    roc.MakeROC(0.001)
