import cv
from plugins import Plugin
from constants import *


class Canny(Plugin):
    def __init__(self, threshold1=70.0, threshold2=140.0):
        self.threshold1 = threshold1
        self.threshold2 = threshold2
        self.inc = 5

    def __call__(self, image):
        # Get the size of the image
        size = cv.GetSize(image)

        # Create a gray scale image
        gray_image = cv.CreateImage(size, 8, 1)
        cv.CvtColor(image, gray_image, cv.CV_RGB2GRAY)

        # Create an image to save edge data to
        edges_image = cv.CreateImage(size, 8, 1)

        # Canny edge detection
        # http://opencv.willowgarage.com/documentation/python/feature_detection.html
        cv.Canny(gray_image, edges_image, self.threshold1, self.threshold2)

        cv.CvtColor(edges_image, image, cv.CV_GRAY2RGB)
        return image

    def press_up(self):
        self.threshold1 += self.inc
        print self.threshold1

    def press_down(self):
        self.threshold1 -= self.inc
        print self.threshold1

    def press_right(self):
        self.threshold2 += self.inc
        print self.threshold2

    def press_left(self):
        self.threshold2 -= self.inc
        print self.threshold2
