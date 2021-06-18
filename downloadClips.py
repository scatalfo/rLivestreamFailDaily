import praw
import os
from os import path
import editVideo
import uploadVideo
def downloadClips():
    f = open("dailyVideoData.txt", "a") #create our daily video data file for editing purposes (it will contain all the info for editing)

    authfile = open('authfile.txt', 'r') #open the auth file to get our reddit credentials
    authLines = authfile.readlines()
    myClient_id = authLines[0].strip() #removing whitespace and linebreaks
    myClient_secret = authLines[1].strip()
    myUser_agent = authLines[2].strip()

    reddit = praw.Reddit( #creating a read only instance of reddit with the credentials provided in authFile.txt
        client_id = myClient_id,
        client_secret = myClient_secret,
        user_agent = myUser_agent,
    )

    counter = 0
    for submission in reddit.subreddit("livestreamfail").top("day"): #loop through the top posts of the day
        if(submission.url.startswith("https://clips.twitch.tv/")): #make sure the post links to a clip
            os.system("python twitch-dl.1.16.0.pyz download -q source " + submission.url + " > output.txt") #download the clip and extract the info to output.txt
            with open('output.txt', 'r') as output: 
                last_line = output.readlines()[-1]
                f.write(last_line[12:]) #write the file name (which we parsed from the command line output), into the daily video data file
                f.write(str(submission.author) + "\n") #including additional information in the daily video data file
                f.write(str(submission.title)  + "\n")
                f.write(str(submission.url) + "\n")
                print("check passed")
            os.remove("output.txt") #deleting our command line output file that was used for parsing


        counter+=1
        if(counter >= 15): #amount of posts we will look through for clips
            break
        
    f.close()

