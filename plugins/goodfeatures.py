import cv
from plugins import Plugin

class GoodFeatures(Plugin):

    def __init__(self, corners=100, quality=0.04, min_distance=2):
        self.corners = corners
        self.quality = quality
        self.min_distance = min_distance

    def __call__(self, image):
        # Get the size of the image
        size = cv.GetSize(image)

        # Convert to gray
        gray_image = cv.CreateImage(size, 8, 1)
        cv.CvtColor(image, gray_image, cv.CV_RGB2GRAY)

        # Create temporary images for processing
        eig_image = cv.CreateImage(size, 32, 1)
        temp_image = cv.CreateImage(size, 32, 1)

        # http://opencv.willowgarage.com/documentation/python/feature_detection.html#goodfeaturestotrack
        corners = cv.GoodFeaturesToTrack(gray_image, eig_image, temp_image, self.corners, self.quality, self.min_distance)

        for corner in corners:
            cv.Circle(image, corner, 5, cv.RGB(0,255,0), -1)
        return image

    def press_up(self):
        self.corners += 1
        print self.corners

    def press_down(self):
        self.corners -= 1
        print self.corners

    def press_right(self):
        self.quality += .01
        print self.quality

    def press_left(self):
        self.quality -= .01
        print self.quality
