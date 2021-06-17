import os
from moviepy.editor import *
import datetime
def editClips():
    linenum = 0
    editedClips = []
    with open("dailyVideoData.txt",'r', encoding='utf-8') as fin:
        dailyVideoData = fin.readlines()
    print(dailyVideoData)

    t = datetime.datetime.now()
    title = TextClip("The top clips of /r/Livestreamfail for " + t.strftime('%b %d, %Y'),fontsize=70,color='white',align='center')
    title = title.set_fps(60)
    title = title.set_duration(5)
    editedClips.append(title)
    for line in dailyVideoData:
        if(linenum%4 == 0):
            print(linenum)
            vfc = VideoFileClip(line[:-1])
            print(dailyVideoData[linenum + 2] + " posted by: " + dailyVideoData[linenum+1])
            tc = TextClip(dailyVideoData[linenum + 2] + " posted by: " + dailyVideoData[linenum+1], fontsize=70,color='black',align="South")
            tc = tc.set_fps(60)
            tc = tc.set_duration(5)
            editedClips.append(CompositeVideoClip([vfc, tc]))
        linenum+=1
    final_clip = concatenate_videoclips(editedClips, method="compose")
    final_clip.write_videofile("dailyClips.mp4")


def deleteOldVideos():
    forDeletion = open("dailyVideoData.txt", "r")

    linenum = 0

    for line in forDeletion:
        if(linenum%4 == 0):
            os.remove(line[:-1])
        linenum+=1
    forDeletion.close()
    os.remove("dailyVideoData.txt")


