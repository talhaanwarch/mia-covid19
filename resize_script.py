# -*- coding: utf-8 -*-
"""
Created on Thu Jun 24 03:29:25 2021

@author: TAC
"""

import cv2
from glob import glob
import os
from tqdm import tqdm
import sys

def resize(path1,path2):
    os.makedirs(path1+'/resized/'+path2)
    for folder in tqdm(glob('{}/*/'.format(path1+'/'+path2))):
        p=folder.partition(path1+'/'+path2)[-1]
        os.makedirs(path1+'/resized/'+path2+p)
        for image in glob(folder+'*.jpg'):
            img=cv2.imread(image,0)
            try:
                image=image.partition(path1+'/'+path2)[-1]
                img=cv2.resize(img,(224,224))
                cv2.imwrite(path1+'/resized/'+path2+image,img)
            except Exception as e: # work on python 3.x
                print(path1+'/resized/'+path2+image)
                print(str(e))
            
def main(args):
    print(args)
    resize(args[1],args[2])


if __name__ == '__main__':
    main(sys.argv)

