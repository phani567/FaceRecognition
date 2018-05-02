# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 11:00:31 2015

@author: ymlui
"""

from pylab import *
from Img import *

try:
    from PIL.Image import AFFINE,NEAREST,BILINEAR,BICUBIC,ANTIALIAS
except:
    from Image import AFFINE,NEAREST,BILINEAR,BICUBIC,ANTIALIAS



def AffineFromPoints(imdata, src1, src2, dst1, dst2, dst_size, filter=BILINEAR):
    A = [[src1.getX(), -src1.getY(), 1, 0],
         [src1.getY(), src1.getX(),  0, 1],
         [src2.getX(), -src2.getY(), 1, 0],
         [src2.getY(), src2.getX(),  0, 1]]
    b = [dst1.getX(), dst1.getY(), dst2.getX(), dst2.getY()]
    
    A = array(A)
    b = array(b)
    result = solve(A,b)
         
    a,b,tx,ty = result
    # Create the transform matrix
    matrix = array([[a,-b,tx],[b,a,ty],[0,0,1]],'d')
    
    inverse = inv(matrix)
    invdata = inverse[:2,:].flatten()
    newsize = int(dst_size[0]),int(dst_size[1])
    
    im = imdata.getDataBuffer()
    transformedData = im.transform(newsize, AFFINE, invdata, filter)
    imdata.setDataBuffer(array(transformedData))

    return imdata

    #img = im.load()
    


