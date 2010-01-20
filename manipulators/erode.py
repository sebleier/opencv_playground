import cv


def erode(image):
    # Get the size of the image
    size = cv.GetSize(image)
    kernel = cv.CreateStructuringElementEx(20, 20, 4, 4, cv.CV_SHAPE_RECT)
    dest = cv.CreateImage(size, image.depth, image.nChannels)
    cv.Erode(image, dest, kernel)

    return dest
