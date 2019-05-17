# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 18:58:23 2019

@author: Binit Mishra
"""
im1=input("Enter File:")

from PIL import Image 
  
# Read image 
img = Image.open(im1).convert('LA')
img.save('greyscale.png')

# Output Images 
img.show() 
  
# prints format of image 
print(img.format) 
  
# prints mode of image 
print(img.mode) 

# get pixel data
pix_val = list(im1.getdata())