# Python-OpenCV-frame-capture
This project was created in order to turn a video file into a series of frames.

##Getting Started

####Prerequisites 
In order to get started there is a package that is required in order to use the program. 

If you have `pip` installed then you will be able to proceed with the next step. If you don't have pip then you must run the command `sudo apt-get install python-pip` on your Linux machine in order to install it.

Next we use the requiements.txt to install the required packages for the program.
Simply type in `pip install -r requirements.txt` if your python version is 2.x or `pip3 install -r requirements.txt` if your current version of python is 3.x. You can check what version of python you have by typing in `python -V`

##How to use the program

###Instructions:
In order to use the program simply have the path of the video file that you want to convert into a series of images. We shall simply call this `/pathtofile/`. Next we want to have the destination directory where the images should be stored. We will simply call this `/outputdirectorypath/`. Since this program uses Python's argparse library the program is executed by giving it an input and an output. This can be done in the format `python FrameParse.py --input /pathtofile/ --output /outputdirectorypath/`. After that the program will run and produce all the frames in the image. 