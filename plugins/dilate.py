import cv
from plugins import Plugin
from constants import *


class Dilate(Plugin):
    def __init__(self, cols=20, rows=20, x=4, y=4, shape=cv.CV_SHAPE_RECT):
        self.cols = cols
        self.rows = rows
        self.x = x
        self.y = y
        self.shape = shape

    def __call__(self, image):
        # Get the size of the image
        size = cv.GetSize(image)
        kernel = cv.CreateStructuringElementEx(20, 20, 4, 4, cv.CV_SHAPE_RECT)
        dest = cv.CreateImage(size, image.depth, image.nChannels)
        cv.Dilate(image, dest, kernel)
        return dest

    def press_up(self):
        self.cols += 1
        print self.cols

    def press_down(self):
        self.cols -= 1
        print self.cols

    def press_right(self):
        self.rows += 1
        print self.rows

    def press_left(self):
        self.rows -= 1
        print self.rows


