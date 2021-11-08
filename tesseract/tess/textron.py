'''
https://github.com/AyanGadpal/TextTron-Lightweight-text-detector
'''

import cv2
from TextTron.TextTron import TextTron
import glob

adir = '/home/sandeep/github/personal/web/playwright/screenshot/screenshots/*.png'
files = glob.glob(adir)

for f in files:
    screenshot = f
    print(f)
    img = cv2.imread(screenshot)
    TT = TextTron(img)

    tbbox = TT.textBBox
    print(tbbox)
    plotImg = TT.plotImg
    print(type(plotImg))
    try:
        cv2.imshow('example', plotImg)
        print('pring')
    except:
        print(e)
    cv2.waitKey(1)