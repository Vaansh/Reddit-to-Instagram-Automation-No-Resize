from instabot import Bot, API
from PIL import Image
import credentials
import urllib
import praw
import time

bot = Bot()
bot.login(username=credentials.IGusername, password=credentials.IGpassword)

filePath = ""  # Folder to save images in; Example: /Users/username/Desktop/folder/destination/
currentPost = 1
numPosts = 100  # Num of rounds can be decided here
urlPosted = []  # To avoid duplicates
postGap = 7200  # Gap between the posts (in seconds)
subreddit = credentials.reddit.subreddit("")  # Name of subreddit to source posts from

while currentPost <= numPosts:
    for submission in subreddit.hot(limit=25):
        url = submission.url
        fileName = str(submission)
        fullPath = filePath + fileName + "."  # Extension name; Example: .PNG
        title = '"' + str(submission.title) + '"'
        credit = "(Via: u/" + str(submission.author) + " on Reddit)"
        caption = title + "\n" + credit + "\n"

        if (url.endswith("jpg") or url.endswith("png")) and (not url in urlPosted):  # Decide post bounds here
            try:
                saveImage(url, filePath, fileName)
                urlPosted.append(url)

                img = Image.open(fullPath)
                imgWidth, imgHeight = img.size
                ratio = imgWidth / imgHeight

                if 0.8 <= ratio <= 1.91:  # Checks if the ratio can be posted in instagam, this program does not resize
                    if not bot.upload_photo(fullPath, caption=caption):
                        currenpost = currenpost + 1
                        time.sleep(postGap)
                        subreddit = credentials.subreddit("ksi")  # Refresh to get the newer posts
                        break
            except:
                print("cant be posted, next...")
                continue
        else:
            continue
        break


def saveImage(postUrl, filePath, fileName):  # Saves image in designated path
    fullPath = filePath + fileName + ".PNG"
    urllib.request.urlretrieve(url, fullPath)
