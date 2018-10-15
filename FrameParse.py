import cv2
import os
import argparse


def create_directory(output):
    """
    Creates a directory if it doesn't exist.
    :param output: The output directory that is either created or already exists.
    :return: None
    """
    flag = os.path.isdir(output)
    if not flag:
        os.mkdir(output)


def extractImages(pathIn, pathOut):
    """
    Takes in a video file and writes the images in to an output directory.
    :param pathIn:  Path of the image
    :param pathOut: Path of the output directory.
    :return: None
    """
    count = 0
    vidcap = cv2.VideoCapture(pathIn)
    success,image = vidcap.read()
    create_directory(pathOut)
    while success:
      out_filename = os.path.join(pathOut, "frame%d.jpg" % count)
      cv2.imwrite(out_filename, image)
      success, image = vidcap.read()
      count = count + 1
    print("All done!")


if __name__ == "__main__":
   a = argparse.ArgumentParser()
   a.add_argument("--input", help="path to video")
   a.add_argument("--output", help="path to images")
   args = a.parse_args()
   if os.path.isfile(args.input):
        extractImages(args.input, args.output)
   else:
       print("{} is not a valid file".format(args.input))
