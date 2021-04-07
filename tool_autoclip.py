import os
import cv2 as cv
import numpy as np
import argparse

def searchimg(dir=".",ext=".bmp"):
    dirs = os.listdir(dir)
    for obj in dirs:
        if os.path.isdir(os.path.join(dir,obj)):
            # is a dir
            searchimg(os.path.join(dir,obj))
        if os.path.isfile(os.path.join(dir,obj)) and os.path.splitext(obj)[-1]==ext:
            filepath = os.path.join(dir, obj)
            processimg(filepath)
    return

def processimg(dir, ext = ".jpg"):
    img = cv.imread(dir)
    imgpath = os.path.dirname(dir)
    imgname = os.path.basename(dir)
    imgname = list(os.path.splitext(imgname))
    imgname[0] = imgname[0] # add extension name

    #process
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    th, threshed = cv.threshold(gray, 240, 255, cv.THRESH_BINARY_INV)
    kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE, (11, 11))
    morphed = cv.morphologyEx(threshed, cv.MORPH_CLOSE, kernel)
    # get contours
    cnts = cv.findContours(morphed, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)[-2]
    if len(cnts) < 1:
        return
    #
    # cnt = sorted(cnts, key=cv.contourArea)[-1]
    # x, y, w, h = cv.boundingRect(cnt)
    # dst = img[y:y + h, x:x + w]
    x = np.inf
    y = np.inf
    x2 = 0
    y2 = 0
    for cnt in cnts:
    ## (4) Crop and save it
        x_1, y_1, w, h = cv.boundingRect(cnt)
        x_2 = x_1 + w
        y_2 = y_1 + h

        x = min(x,x_1)
        y = min(y,y_1)
        x2 = max(x2,x_2)
        y2 = max(y2,y_2)
    print(cv.boundingRect(sorted(cnts, key=cv.contourArea)[-1]))
    print(x,y,x2,y2)
    dst = img[y:y2, x:x2]

    cv.imwrite(os.path.join(imgpath,imgname[0])+ext,dst)

def run():
    pass
def main():
    parser = argparse.ArgumentParser(description="Clip image in a fast way")
    parser.add_argument("path")
    parser.add_argument("-ext",help="the extension of images in the folder", default=".png")
    args = parser.parse_args()
    searchimg(args.path,ext=args.ext)

if __name__ == '__main__':
    main() 
