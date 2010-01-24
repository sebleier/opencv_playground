import cv
from optparse import OptionParser
from plugins import Plugin
from collections import defaultdict


class WebCam(object):
    def __init__(self, width=None, height=None, fps=30, plugins=[]):
        self.width = width
        self.height = height
        self.camera = cv.CreateCameraCapture(0)
        self.fps = fps
        if width is not None and height is not None:
            cv.NamedWindow('Camera')
            cv.ResizeWindow('Camera', width, height)
        else:
            cv.NamedWindow('Camera', cv.CV_WINDOW_AUTOSIZE)

        # Add the specified plugins from the available plugins
        self._plugins = []
        for plugin_name in plugins:
            for plugin in Plugin.plugins:
                if plugin.__name__.lower() in ("plugin", plugin_name.lower()):
                    self._plugins.append(plugin())

    def get_image(self):
        """ Get the current frame and convert to an Image object """
        image = cv.QueryFrame(self.camera)
        for plugin in self._plugins:
            image = plugin(image)
        return image

    def handle_events(self):
        key = cv.WaitKey(int(1000 * 1.0/self.fps))
        if key != -1:
            for plugin in self._plugins:
                plugin.pressed(key)

    def process_frame(self):
        while True:
            self.handle_events()
            image = self.get_image()
            yield image

    def capture_video(self):
        for frame in self.process_frame():
            cv.ShowImage('Camera', frame)

if __name__=="__main__":
    parser = OptionParser()
    plugins = []
    (options, args) = parser.parse_args()
    for arg in args:
        try:
            plugins.append(arg)
        except KeyError:
            pass

    webcam = WebCam(plugins=plugins)
    webcam.capture_video()
