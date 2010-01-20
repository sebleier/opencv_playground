import cv
from optparse import OptionParser
from manipulators import canny, dilate, erode, facedetect, goodfeatures


class WebCam(object):
    def __init__(self, width=640, height=480, manipulators=[]):
        self.width = width
        self.height = height
        self.camera = cv.CreateCameraCapture(0)
        self.key_events = {}
        self.manipulators = manipulators

    def get_image(self):
        """ Get the current frame and convert to an Image object """
        im = cv.QueryFrame(self.camera)
        im = self.process_image(im)
        for f in self.manipulators:
            im = f(im)
        return im

    def process_image(self, im):
        """ Hook to do some image processing / manipulation """
        return im

    def capture_video(self):
        fps = 30.0
        try:
            cv.NamedWindow('Camera', cv.CV_WINDOW_AUTOSIZE)
            while True:
                im = self.get_image()
                cv.ShowImage('Camera', im)
                key = cv.WaitKey(int(1000 * 1.0/fps))
                if key == 0x1b:
                    break
                elif key == -1:
                    continue
                elif self.key_events.has_key(key):
                    self.key_events[key]()
        except KeyboardInterrupt:
            return


if __name__=="__main__":
    parser = OptionParser()
    manipulators = []
    manipulators_options = {
        'canny': canny.canny,
        'dilate': dilate.dilate,
        'erode': erode.erode,
        'facedetect': facedetect.facedetect,
        'goodfeatures': goodfeatures.goodfeatures,
    }
    (options, args) = parser.parse_args()
    for arg in args:
        try:
            manipulators.append(manipulators_options[arg])
        except KeyError:
            pass

    webcam = WebCam(manipulators=manipulators)
    webcam.capture_video()
