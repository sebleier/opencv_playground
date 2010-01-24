from collections import defaultdict
from constants import KEYS

class PluginMetaClass(type):
    def __init__(cls, name, bases, attrs):
        if not hasattr(cls, 'plugins'):
            cls.plugins = []
        cls.plugins.append(cls)

class Plugin(object):
    __metaclass__ = PluginMetaClass

    key_events = {}

    def __call__(self, image):
        return image

    def press_esc(self):
        raise StopIteration

    def pressed(self, key):
        try:
            method = getattr(self, "press_%s" % KEYS[key])
        except (KeyError, AttributeError):
            pass
        else:
            if callable(method):
                method()

from erode import Erode
from canny import Canny
from dilate import Dilate
from facedetect import FaceDetect
from goodfeatures import GoodFeatures
