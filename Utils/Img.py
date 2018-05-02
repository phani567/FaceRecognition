# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 11:00:31 2015

@author: ymlui
"""

from pylab import *
from PIL import Image
import math


class Img:
    def __init__(self, data, dataWidth=0, dataHeight=0):
        if (dataWidth == 0 and dataHeight == 0):
            self.data = []
            self.dataWidth = 0
            self.dataHeight = 0
        
            self.img = data.copy()
            self.width = (array(data).shape)[0]
            self.height = (array(data).shape)[1]
            self.channels = len(array(data).shape)

        else:
            self.img = []
            self.width = 0
            self.height = 0
            self.channels = 0
        
            self.data = data.reshape(dataWidth, dataHeight)
            self.dataWidth = dataWidth
            self.dataHeight = dataHeight
    
    

    def getImgWidth(self):
        return self.width
    
    def getImgHeight(self):
        return self.height


    def getDataWidth(self):
        return self.dataWidth

    def getDataHeight(self):
        return self.dataHeight
    
    def setGrayscaleBuffer(self):
        ## RGB image (w, h, channels)
        if (self.channels == 2):
            self.data = self.img
        elif (self.channels == 3):
            self.data = self.img.convert('L')
        else:
            raise TypeError("Unsuppoted Color Channel: %s ..."%self.channels)


    def setRGBBuffer(self):
        if (self.channels != 3):
            raise TypeError("Unsuppoted Color Channel: %s ..."%self.channels)
        else:
            self.data = self.img

    def setRedBuffer(self):
        if (self.channels != 3):
            raise TypeError("Unsuppoted Color Channel: %s ..."%self.channels)
        else:
            self.data = Image.fromarray(array(self.img)[:,:,0])

    def setChrominanceBuffer(self):
        if (self.channels != 3):
            raise TypeError("Unsuppoted Color Channel: %s ..."%self.channels)
        else:
            img = 0.596 * array(self.img)[:,:,0] - 0.275 * array(self.img)[:,:,1] - 0.321 * array(self.img)[:,:,2]
            self.data = Image.fromarray(img)

    def getDataBuffer(self):
        if (len(array(self.data).shape) < 2):
            raise TypeError("Unsupported Data Buffer ...")
        else:
            return self.data

    def setDataBuffer(self, data):
        self.data = Image.fromarray(data)
        self.dataWidth = (array(self.data).shape)[0]
        self.dataHeight = (array(self.data).shape)[1]

    def display(self):
        fig = figure()
        print array(self.data).shape
        if (len(array(self.data).shape) == 2):
            imshow(self.data, cmap='Greys_r')
        else:
            imshow(self.data)
        axis('off')
        
        show()
