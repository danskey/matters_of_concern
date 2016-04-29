from __future__ import print_function

#from itertools import chain

import datetime
import time
from shutil import copyfile
import os
from os import walk
from os.path import join
#import LAME
#import libmp3lame
from moviepy import *
from AngelofHistory import watch
from AngelofHistory import forget
from ThingClass import *
from moviePie import *
# import video
# import audio
# import images

##############   Hippocampus   ##############


####### Variables to fine tune the functioning of the program ########

archive = "TheArchive" #name of the file directory to be worked on
cycle_length = 90 #time is in seconds, cycle length for the monitoring period
combo_window = 6 #time is in seconds, window in which files need to be accessed in order to trigger the Combiner
L = 7
K = 14
kRatio = 2

######################################################################

archiveLog = "ArchiveLOG.txt"
archiveNeglectedLOG = "ArchiveNeglectedLOG.txt"
content = []
Things = []
neglected_content = []
momentary_path = "MomentaryArchive/"


def main():
    #start_time = time.time()
    start_time = 1461624490.0 #Dev start_time
    #watch(archive, cycle_length, start_time)
    print("Angel of History finished watching")
    print("loading the archive...")
    forget(archive, start_time)
    content = load_the_log(archiveLog)
    neglected_content = load_the_log(archiveNeglectedLOG)
    print(neglected_content)
    print("sorting the archive...")
    content = sorted(content, key = lambda x: float(x[4]))
    contents = look_for_file_extentions(content)
    neglected_content = look_for_file_extentions(neglected_content)
    neglected_content = look_for_repeats(contents)
    contents = look_for_repeats(contents)
    contents = look_for_buddies(contents)
    print("making things now...")
    Things = make_things(contents)
    neglected_Things = make_things(neglected_content)
    print("going to Remember now")
    Forgetter(neglected_Things, start_time)
    remembered = Rememberer(Things)
    Rememberer_part2(remembered)
    print(" ---- Cycle Complete ---- ")
    #print(len(remembered))
    #tester = Things[0]
    #print(tester)
    # print(tester.filepath)
    # print(Things[7].filepath)
    # print(Things[8].filepath)
    # print(Things[9].filepath)
    # print(Things[11].filepath)


def load_the_log(archiveLog):
    with open(archiveLog) as f:
        lines = f.readlines()
    for l in lines:
        l = l[1:-2]
        fields = l.split(",")
        fields[0] = fields[0][1:-1]
        content.append(fields)
    return content

#
# def look_for_neglected_files(archive):
#     for root, directories, files in os.walk(archive):
#         for filepath in files:
#             #t = os.path.getatime(filename)
#             filepath = os.path.join(root, filepath)
#             t = os.path.getatime(filepath)
#             if t < starting_time:
#                 neglected_files.append(filepath)
#             else:
#                 pass
#     print(neglected_files)
#     neglected_files = look_for_file_extentions(neglected_files)
#     return neglected_files


def look_for_file_extentions(content):
    contents = []
    for index in content:
        filepath = index[0]
        extension = filepath[filepath.rfind("."):]
        #print(extension)
        if extension in (".mp3", ".m4a"):
            index.append("audio")
        elif extension in  (".txt", ".docx", ".pdf", ".doc"):
            index.append("text")
        elif extension in (".mp4", ".mov", ".mkv"):
            index.append("video")
        elif extension in (".jpg", ".tiff", ".tif", ".gif", ".JPG"):
            index.append("image")
        else:
            print ("something is wrong, extension is not recognized")
        contents.append(index)
    return contents


def look_for_repeats(contents):
    for index in contents:
        filepath = index[0]
        counts = sum(x.count(filepath) for x in contents)
        index.append(counts)
    return contents


def look_for_buddies(contents):
    buddies = []
    previous = None
    next = None
    for i in range(len(contents)):
        index = contents[i]
        previous_file = contents[i - 1]
        if (abs(float(index[4])-float(previous_file[4])) < combo_window):
            index.append(previous_file[0])
        if i < (len(contents)-1) and (abs(float(index[4])-float(contents[i + 1][4])) < combo_window):
            index.append(contents[i + 1][0])
        else:
            pass
        buddies.append(index)
    return buddies


def make_things(contents): # takes log items and builds class objects
    for index in contents:
        item = Thing(index[0], index[4], index[5], index[6], index[7:]) #path, access_time, type, access_count, buddies
        Things.append(item)
    print("done making things....")
    return Things

# def matters_of_concern(Things):
#     for thing in Things:
#         if thing.access_count > 1:
#             thing

def Forgetter(Things, start_time):
    print("running the forgetter")
    for thing in Things:
        if thing.access_count == 1 and thing.access_time < start_time:
            if thing.fType is "text":
                output = thing.LR_sum(thing.filepath, 1)
                output_file_path = os.path.join(momentary_path, thing.filepath)
                f = thing.filepath
                copyfile(f, momentary_path)
                output = str(output)
                print(output)
                print("GOODBYE!!!!!!!!!!")
                for line in output_file_path.readlines():
                    one_line_less = line.replace(output,"")
                output_file = open(output_file_path, "w")
                output_file.writelines(one_line_less)
                output_file.close()
            # elif thing.fType is "video":
            #     output = thing.VideoRememberer(thing.filepath)
            #     final_clip = concatenate_videoclips(output)
            #     output_file_path = os.path.join(momentary_path, thing.filepath)
            #     final_clip.write_videofile(output_file_path, audio=True) # would like to add audio_codec=libmp3lame
            #     del output
            #     del final_clip
            else:
                pass
        else:
            pass
#
# def Rememberer(Things):
#     remembered=[]
#     print("this is the length of things")
#     print(len(Things))
#     seen = set()
#     unique = []
#     for obj in objects:
#         if obj.thing not in seen:
#             unique.append(obj)
#             seen.add(obj.thing)
#
#
#     for thing in Things:
#
#         # search = item.filepath
#
#         # if item[0] == search for items in remembered:
#         #
#         # else:
#         #     remembered.append(thing)
#         #     print("we are in the else part now")
#         #     print(remembered)
#         # return remembered
#         # print(remembered)
#         if not remembered:
#             remembered.append(thing)
#             print("appended the first one")
#             #print(len(remembered)
#
#     print(len(remembered))
#
#     for thing in Things:
#         if thing.filepath != item.filepath
#
#     for item in remembered:
#         for thing in Things:
#             if item.filepath != thing.filepath:
#                 remembered.append(thing)
#             else:
#                 print("we are in the else part now")
#                 pass
#         return remembered
#
#
#     # for item in remembered:
#     #     search = item.filepath
#     #     for thing in Things:
#     #         if thing.filepath is search:
#     #             print("its already here")
#     #             pass
#     #         else:
#     #             remembered.append(thing)
#     #             print("we are in the else part now")
#     #             #print(remembered)
#     #     return remembered
#     #     #print(remembered)
#     # print(remembered)
#     # print("this is the length of remembered")
#     # print(len(remembered))
#
#
#     # for thing in Things:
#     #     search = thing.filepath
#     #     print("trying to add a second")
#     #     for item in remembered:
#     #         print("we are iteming in remembered now")
#     #         if item.filepath is search:
#     #              print("its already here")
#     #              pass
#     #         else:
#     #             remembered.append(thing)
#     #             print("we are in the else part now")
#     #             print(remembered)
#     #     return remembered
#     #     print(remembered)

def Rememberer_part2(remembered):
    for thing in remembered:
        if thing.access_count > 1:
            if thing.fType is "text":
                output = thing.LR_sum(thing.filepath, L)
                output_file_path = os.path.join(momentary_path, thing.filepath)
                output_file = open(output_file_path, "w")
                output_file.writelines(output)
                output_file.close()
            elif thing.fType is "video":
                RMS = thing.VideoRememberer(thing.filepath, kRatio)
                clip_list = thing.make_RMS_Clip(thing.filepath, RMS)
                final_clip = concatenate_videoclips(clip_list)
                output_file_path = os.path.join(momentary_path, thing.filepath)
                final_clip.write_videofile(output_file_path, audio=True, audio_codec="libmp3lame") # would like to add audio_codec=libmp3lame
                del clip_list
                del final_clip
            else:
                pass
        else:
            pass




# def Rememberer(Things):
#     for thing in Things:
#         if thing.access_count > 1:
#             if thing.fType is "text":
#                 output = thing.LR_sum(thing.filepath, L)
#                 output_file_path = os.path.join(momentary_path, thing.filepath)
#                 output_file = open(output_file_path, "w")
#                 output_file.writelines(output)
#                 output_file.close()
#             elif thing.fType is "video":
#                 output = thing.VideoRememberer(thing.filepath, kRatio)
#                 final_clip = concatenate_videoclips(output)
#                 output_file_path = os.path.join(momentary_path, thing.filepath)
#                 final_clip.write_videofile(output_file_path, audio=True, audio_codec="libmp3lame") # would like to add audio_codec=libmp3lame
#                 del output
#                 del final_clip
#             else:
#                 pass
#         else:
#             pass


if __name__ == "__main__":main()
