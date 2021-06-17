import datetime
import os
from simple_youtube_api.Channel import Channel
from simple_youtube_api.LocalVideo import LocalVideo

def uploadVideo():
    f = open("dailyVideoData.txt", "r") #take tags from dailyvideodata.txt
    data = f.readlines()
    tags = ""
    linenr = 0
    for line in data:
        if(linenr%2 == 0):
            tags.append(line.split(" "))

    os.remove("dailyVideoData.txt")
    # loggin into the channel
    channel = Channel()

    channel.login("client_secret.json", "login.txt")

    # setting up the video that is going to be uploaded
    video = LocalVideo(file_path="dailyClips.mp4")

    # setting snippet
    t = datetime.datetime.now()
    video.set_title("The top clips of /r/Livestreamfail for " + t.strftime('%b %d, %Y'))
    video.set_description("This is an open source project created and maintained by Sam Catalfo (@scatalfo on GitHub). https://github.com/scatalfo/rLivestreamFailDaily")
    video.set_tags(["LivestreamFail", "Live", "Stream", "Fail"] + tags)
    video.set_category("Gaming")
    video.set_default_language("en-US")

    # setting status
    video.set_embeddable(True)
    video.set_license("creativeCommon")
    video.set_privacy_status("private")
    video.set_public_stats_viewable(True)

    # setting thumbnail
    video.set_thumbnail_path('thumbnail.png')

    # uploading video and printing the results
    video = channel.upload_video(video)
    print(video.id)
    print(video)

    # liking video
    video.like()
