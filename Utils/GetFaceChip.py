# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 11:00:31 2015

@author: ymlui
"""

from scipy.ndimage import filters
from Affine import *
from Point import *
from Img import *
import math
import numpy


def GaussianSmooth(imdata, sigma):

    im = filters.gaussian_filter(imdata.getDataBuffer(), sigma)
    imdata.setDataBuffer(im)
    return imdata

def FaceSmoothing(imdata, src_leye, src_reye):
    dx = src_reye.getX() - src_leye.getX()
    dy = src_reye.getY() - src_leye.getY()
    eye_dist = math.sqrt(dx*dx + dy*dy)

    sigma = 0.5 * eye_dist / (0.423 * imdata.getImgWidth())
    
    return GaussianSmooth(imdata, sigma)

def Preprocess(imdata):
    data = [math.log(i) for i in (imdata+0.1)]
    data = (data - mean(data)) / numpy.std(data)    
    
    return data

def GetFaceChip(im, src_leye, src_reye, dst_leye, dst_reye, dst_size, channel='gray'):
    
    imdata = Img(im)
    
    if (channel=='gray' or channel=='Gray' or channel=='GRAY'):
        imdata.setGrayscaleBuffer()
    elif (channel=='RGB'):
        imdata.setRGBBuffer()
    elif (channel=='red' or channel=='Red' or channel=='RED'):
        imdata.setRedBuffer()
    elif (channel=='I'):
        imdata.setChrominanceBuffer()
    else:
        raise TypeError("Unsuppoted Color Channel: %s ..."%channel)

    
    ## smooth the image before applying affine transformation
    imdata = FaceSmoothing(imdata, src_leye, src_reye)

    imdata = AffineFromPoints(imdata, src_leye, src_reye, dst_leye, dst_reye, dst_size)

    
    return imdata

