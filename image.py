import cv2, os
import numpy as np
from matplotlib import pyplot as plt
from PIL import Image
import pytesseract
import argparse

# https://www.geeksforgeeks.org/how-to-install-opencv-for-python-in-linux/
# https://theailearner.com/2018/10/23/understanding-images-with-opencv-python/
file="/Users/volker/Pictures/misc/cost_of_retaining_employees.jpg"

img=cv2.imread(file)

#print(f"Image: ${img.item}")
# https://pyimagesearch.com/2017/07/03/installing-tesseract-for-ocr/
def do_tesseract():
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    filename= "{}_tmp.png".format(os.getpid())
    cv2.imwrite(filename, img_gray)
    text = pytesseract.image_to_string(Image.open(filename))
    os.remove(filename)
    print(text)
    # show the output images
    cv2.imshow("Image", img)
    cv2.imshow("Output", img_gray)
    cv2.waitKey(0)

# [OpenCV Python Tutorial #3 - Cameras and VideoCapture](https://www.youtube.com/watch?v=rKcwcARdg9M)
def do_capture():
    cap = cv2.VideoCapture(1)
    while True:
        ret, frame = cap.read()
        print(f'ret: {ret}')
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) == ord('q'):
            break
        #else:
        #    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        #    filename= "{}_tmp.png".format(os.getpid())
        #    cv2.imwrite(filename, img_gray)
        #    text = pytesseract.image_to_string(Image.open(filename))
        #    os.remove(filename)
        #    print(text)        
    cap.release()
    cv2.destroyAllWindows() 
    pass

def do_stuff():
    # https://www.geeksforgeeks.org/detect-an-object-with-opencv-python/
    # OpenCV opens images as BRG 
    # but we want it as RGB and 
    # we also need a grayscale 
    # version
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    # Creates the environment 
    # of the picture and shows it
    plt.subplot(1, 1, 1)
    plt.imshow(img_rgb)
    #plt.show()


    # Use minSize because for not 
    # bothering with extra-small 
    # dots that would look like STOP signs
    # Use minSize because for not 
    # bothering with extra-small 
    # dots that would look like STOP signs
    #stop_data = cv2.CascadeClassifier('stop_data.xml')
    #found = stop_data.detectMultiScale(img_gray, 
    #                                   minSize =(20, 20))
    # convert image to gray scale image
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  
    # detect corners with the goodFeaturesToTrack function.
    corners = cv2.goodFeaturesToTrack(gray, 27, 0.01, 10)
    corners = cv2.goodFeaturesToTrack(gray, 10, 0.01, 10)
    corners = np.intp(corners)
    
    # we iterate through each corner, 
    # making a circle at each point that we think is a corner.
    for i in corners:
        x, y = i.ravel()
        cv2.circle(img, (x, y), 3, 255, -1)
    
    plt.imshow(img), plt.show()


    # Don't do anything if there's 
    # no sign
    """ amount_found = len(found)

    if amount_found != 0:
        
        # There may be more than one
        # sign in the image
        for (x, y, width, height) in found:
            
            # We draw a green rectangle around
            # every recognized sign
            cv2.rectangle(img_rgb, (x, y), 
                        (x + height, y + width), 
                        (0, 255, 0), 5) """
#do_tesseract()
do_capture()