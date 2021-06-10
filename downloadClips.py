import praw

authfile = open('authfile.txt', 'r')
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
for submission in reddit.subreddit("livestreamfail").top("day"):
    print(submission.title)
    print(submission.url)
    print(submission.author)
    counter+=1
    if(counter >= 25):
        break
    

