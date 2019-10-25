#!/usr/bin/python3
import cv2
import numpy as np 

img = cv2.imread('/home/samyak/Pictures/parrots.jpg',1)

cv2.imshow('parrot',img)

b,g,r = cv2.split(img)

cv2.imshow('only red',r)

for i in range(980):
	b[...,i]=0
	g[...,i]=0

img=cv2.merge((b,g,r))

cv2.imshow('parrots',img)

cv2.waitKey(0)

cv2.destroyAllWindows()