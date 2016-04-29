from sumText import *
from librosaProcess import *
from moviePie import *

##############   Thing   ##############

class Thing:

    def __init__(self, path, access_time, fType, access_count, buddies=None):
        self.filepath = path
        self.access_time = access_time
        self.fType = fType
        self.access_count = access_count
        if buddies is None:
            buddies = []
        self.buddies = buddies

    def LR_sum(self, filepath, L):
        summary = lex_rank_sum(filepath, L)
        return summary

    def KL_sum(self, filepath, K):
        summary = kl_rank_sum(filepath, K)
        return summary

    def VideoRememberer(self, filepath, kRatio):
        RMS = libroRMS(filepath, kRatio)
        return RMS

    def make_RMS_Clip(self, filepath, RMS):
        clip_list = []
        for segment in RMS:
            clip = VideoFileClip(filepath).subclip(segment[0],segment[1])
            clip_list.append(clip)
        return clip_list

    # def __getitem__(self, key):
    #     return self.buddies[key]

    def tofileString(self):
        return ",".join([self.filepath, self.modified, self.accessed])



#
# with open(filename, 'r') as inputfile:
# self.content = inputfile.read()
# self.nLines = content.count('\n')
# self.nWords = len(content.split())
#
# def nchars(self):
#     return len(self.file.read())
#
# def nwords(self):
#     content = self.file.read()
#     words = content.split()
#     return len(words)
#
# def nlines(self):
#     content = self.file.read()
#     return content.count('\n')
