# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 11:00:31 2015

@author: ymlui
"""

from PIL import Image
from pylab import *
import csv
from Point import *
from GetFaceChip import *
from define import *


def getFace(img, src_leye, src_reye, bDisplay=False, bRotate=False):
    if (bRotate):
        img = img.rotate(90)

    dst_leye = Point(DST_EYE_COORDINATE[0], DST_EYE_COORDINATE[1])
    dst_reye = Point(DST_EYE_COORDINATE[2], DST_EYE_COORDINATE[3])


    img = GetFaceChip(img, src_leye, src_reye, dst_leye, dst_reye, DST_SIZE, 'Red')

    return img


def ReadImage(fname, leye, reye, bDisplay=False):
    im = Image.open(fname)

    imdata = getFace(im, leye, reye, bDisplay)
    im.close()
    
    return imdata.getDataBuffer()


def ReadFile(fname):
    subjID = []
    filenames = []
    leye = []
    reye = []
    with open(fname, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in reader:
            subjID.append(row[0])
            filenames.append(row[1])
            leye.append(Point(row[3], row[4]))
            reye.append(Point(row[5], row[6]))
    

    return subjID, filenames, leye, reye


def ReadDataFile(fname, datapath):
    [subjID, filenames, leye, reye] = ReadFile(fname)
    
    dataset = []
    
    for i in range(0,len(filenames)):
        print "Loading ", i
        fname = datapath + filenames[i] + '.jpg'
        face = ReadImage(fname, leye[i], reye[i])
        data = Preprocess(array(face).flatten())
        dataset.append(data)

    return dataset, subjID

