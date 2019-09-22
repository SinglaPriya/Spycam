#!/usr/bin/env python
# coding: utf-8

# In[1]:

import cv2
from datetime import datetime as dt


cap= cv2.VideoCapture(0)
ret,frame=cap.read()
if ret:
    loc=r'D:/intruder-{}.jpg'.format(dt.now().strftime('%d%m%y-%H%M%S'))
    cv2.imwrite(loc,frame)
cap.release()

