# -*- coding: utf-8 -*-
"""
An example of face detection using OpenCV and the new Python bindings.

You can detect faces in an image from your local filesystem::

    python facedetect.py -f image.jpg

You can also detect faces in an image from a remote URL::

    python facedetect.py -u http://example.com/image.jpg

You'll need to set an environment variable (HAAR_PATH) to the location that you installed
OpenCV Haar support files to.  This defaults to ``/usr/local/share/opencv/haarcascades``,
the default location on OSX 10.5 and perhaps other platforms.

This program is based on code from `Fun with Python, OpenCV and face detection`_
which in turn was based on code from `Face Detection on the OLPC XO`_ and updated
to use the `OpenCV 2.0 Python API`_, heavily referencing the `OpenCV 2.0 Python Reference`_.

.. _Fun with Python, OpenCV and face detection: http://blog.jozilla.net/2008/06/27/fun-with-python-opencv-and-face-detection/
.. _Face Detection on the OLPC XO: http://eclecti.cc/code/face-detection-on-the-olpc-xo
.. _OpenCV 2.0 Python API: http://opencv.willowgarage.com/wiki/PythonInterface
.. _OpenCV 2.0 Python Reference: http://opencv.willowgarage.com/documentation/python/index.html
"""

__author__ = 'Matt Croydon'
__version__ = ('0', '1', '0', 'alpha')
__license__ = 'BSD'

import cv, os
from plugins import Plugin

HAAR_PATH = os.environ.get('HAAR_PATH', '/usr/local/share/opencv/haarcascades/')

class FaceDetect(Plugin):
    def __call__(self, image):
        # Make a grayscale copy
        size = cv.GetSize(image)
        gray_image = cv.CreateImage(size, 8, 1)
        cv.CvtColor(image, gray_image, cv.CV_RGB2GRAY)

        # Equalize histogram
        cv.EqualizeHist(gray_image, gray_image)

        # Detect faces
        cascade = cv.Load(os.path.join(HAAR_PATH, "haarcascade_frontalface_default.xml"))
        faces = cv.HaarDetectObjects(gray_image, cascade, cv.CreateMemStorage())
        for (x,y,w,h),n in faces:
            cv.Rectangle(image, (x,y), (x+w,y+h), 255)

        # Return the face-detected image
        return image
