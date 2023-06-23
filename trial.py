# -*- coding: utf-8 -*-
"""kla.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/16IeKG4KTSCPs4qyxtk5ygQhAeUcXm5C3
"""
import json
import cv2
from PIL import Image, ImageStat


f = open('input.json')
  
data = json.load(f)
  


def mean(filename):
  print("Mean",filename)
  im = Image.open(str(filename))
  stat = ImageStat.Stat(im)
  print(stat.mean)

mean("wafer_image_1.png")
mean("wafer_image_2.png")
mean("wafer_image_3.png")
mean("wafer_image_4.png")
mean("wafer_image_5.png")

def convert_gray(filename):
  imgg= cv2.imread(str(filename),0)

  #print(imgg)
  x=np.unique(imgg)
  return x

convert_gray("wafer_image_1.png")
convert_gray("wafer_image_2.png")
convert_gray("wafer_image_3.png")
convert_gray("wafer_image_4.png")
convert_gray("wafer_image_5.png")

x=convert_gray("wafer_image_1.png")
print(x)
print(len(x))

def counting_defects(x,filename):
  list1=[]
  #since 255 is white we do not consider
  img = cv2.imread(str(filename))

  for i in range(0,47):
  # counting the number of pixels
    print("\n")
    #255 its a white pixel
    number = np.sum(img == x[i])
    list1.append(number)
    #number_of_black_pix = np.sum(img == 128)
    print('Number of white pixels:', number)
    #print('Number of grey pixels:', number_of_black_pix)
    print("\n")

y=[128 ,133, 134 ,135 ,136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149,
 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167,
 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178]

#trying to find the mean of pixels
#so the mean = sum of pixel values divided by the total number of pixel values

#total nos of pixels 4,80,000
#Since the wholre part is the care area so we iterate through the whole area

# we try to find the number of

def finding(filename):
  img = cv2.imread(str(filename))
# counting the number of pixels
  print("\n")

  print(filename)
  #255 its a white pixel
  number_of_white_pix = np.sum(img == 255)
  number_of_black_pix = np.sum(img == 128)
  print('Number of white pixels:', number_of_white_pix)
  print('Number of grey pixels:', number_of_black_pix)
  print("\n")

finding("wafer_image_1.png")
finding("wafer_image_2.png")
finding("wafer_image_3.png")
finding("wafer_image_4.png")
finding("wafer_image_5.png")

img = cv2.imread("wafer_image_1.png")
#print(img.shape)

#print(prev)

for i in range(0,600):
  for j in range(0,800):
    x=img[i][j]
    if x[0]==255:
      pass
    elif x[0]==128:
      pass
    else:

      print("Defect Found")
      print("i ",j,"j ",i)

import numpy as np
list1=[1,2,3,4,2222,2,2,2,]
np.array(list1)
x=np.unique(list1)
print(x)

#By finding mean Image Pixel Intensity

