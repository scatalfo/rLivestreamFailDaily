import schedule
import time
import uploadVideo
import downloadClips
import editVideo



def job(t):
    downloadClips.downloadClips()
    editVideo.editClips()
    uploadVideo.uploadVideo()
    #editVideo.deleteOldVideos()
    return

schedule.every().day.at("14:30").do(job,'It is 02:30 PM')

while True:
    schedule.run_pending()
    time.sleep(60) # wait one minute
