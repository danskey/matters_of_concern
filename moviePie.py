import subprocess
import os
from skimage.filters import gaussian
from moviepy.editor import *
import time

##############   moviepy files, video   ##############

clip_list=[]

def gfilter():
    return gaussian(image.astype(float), sigma=2)

# def rdvol(self, myclip):
#     myclip = clip.volumex(0.95)

def blur(filepath):
    myclip = VideoFileClip(filepath)
    video = clip.fl_image( gfilter )
    video = clip.volumex(0.95)
    TheVid = str(filename)
    video.write_videofile(TheVid)


# def make_RMS_Clip(filepath, RMS):
#     for segment in RMS:
#         clip = VideoFileClip(filepath).subclip(segment[0],segment[1])
#         clip_list.append(clip)
#     return clip_list


#clipList = map(makeClip, rmsOut3)




#subprocess.call([os.path.join("/", "Applications", "VLC.app", "Contents", "MacOS", "VLC"), ("/Users/nathandanskey/Documents/MovPython/" + TheVid), "--play-and-exit"], shell=False)
