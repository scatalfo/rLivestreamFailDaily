import os
from moviepy.editor import *
import datetime

def editClips():
    linenum = 0
    editedClips = [] 
    with open("dailyVideoData.txt",'r', encoding='utf-8') as fin: #save dailyVideoData as a list
        dailyVideoData = fin.readlines()
    #print(dailyVideoData)
    t = datetime.datetime.now()
    title = TextClip("The top clips of /r/Livestreamfail for " + t.strftime('%b %d, %Y'),fontsize=70,color='white',align='center', bg_color= 'purple')
    title = title.set_fps(60)
    title = title.set_duration(5)
    
    editedClips.append(title) #add title to edited clips list
    for line in dailyVideoData: 
        if(linenum%4 == 0): #if it is the video file name that was parsed 
            #print(linenum)
            if(os.path.isfile(line[:-1])):
                vfc = VideoFileClip(line[:-1]) #grab the video file (minus the end line character)
                print("Check Passed")
            else:
                print("Check Failed")
                continue
            #print(dailyVideoData[linenum + 2] + " posted by: " + dailyVideoData[linenum+1])
            tc = TextClip(dailyVideoData[linenum + 2] + " posted by: " + dailyVideoData[linenum+1], size = (1920, 1080), fontsize=70,color='black', method='caption',align="South", stroke_color='white')
            tc = tc.set_fps(60)
            tc = tc.set_duration(5)
            comp = CompositeVideoClip([vfc, tc])
            editedClips.append(comp) #add the composite of the video and text to the clips list
            if(linenum == 0):
                comp.save_frame("thumbnail.png", t=0, withmask=True) #generate our YouTube thumbnail from the most popular clip

        linenum+=1 #iteration
    final_clip = concatenate_videoclips(editedClips, method="compose") #concat edited clips together
    final_clip.write_videofile("dailyClips.mp4") 
    
    for clip in editedClips: #close all of our clips so we dont get in use errors
        clip.close()
    final_clip.close()


def deleteOldVideos():
    forDeletion = open("dailyVideoData.txt", "r") #read our text file for the last time

    linenum = 0 

    for line in forDeletion:
        if(linenum%4 == 0):
            os.remove(line[:-1]) #remove all the old downloaded videos
        linenum+=1
    forDeletion.close()
    #os.remove("dailyVideoData.txt")


