# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 11:00:31 2015

@author: ymlui
"""

from pylab import *
from Img import *

def DisplayImgset(data, m, n, c=4, r=4, offset=0):
    figure()
    gray()
    
    if ((offset+r*c) >= data.shape[0]):
        offset = 0
        raise TypeError("Display data is out of range ...")
    
    for i in range(1,r*c+1):
        subplot(r,c,i)
        imshow(data[i+offset-1,:].reshape(m,n))
        axis('off')
        
    show()


def DisplayImg(img, m, n):
    pic = Img(img, m, n)
    pic.display()