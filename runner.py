import schedule
import time
import uploadVideo
import downloadClips
import editVideo



def job(t):
    downloadClips.downloadClips()
    editVideo.editClips()
    uploadVideo.uploadVideo()
    editVideo.deleteOldVideos()
    return

schedule.every().day.at("23:53").do(job,'It is 01:00')

while True:
    schedule.run_pending()
    time.sleep(60) # wait one minute
