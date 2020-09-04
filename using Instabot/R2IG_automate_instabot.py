from instabot import Bot, API
from PIL import Image
import credentials
import urllib
import praw
import time

bot=Bot()
bot.login(username=credentials.IGusername, password=credentials.IGpassword)

filePath = '/Users/herculepoirot/Desktop/Automation/pics_ksi/'

def saveImage(url, filePath, fileName):
    fullPath = filePath + fileName + '.PNG'
    urllib.request.urlretrieve(url, fullPath)
prevPath = '/Users/vaanshlakhwara/wholesome_insta/StandardKSIIGAuto/pics/iikkfm.PNG'
preprePath = '/Users/vaanshlakhwara/wholesome_insta/StandardKSIIGAuto/pics/iio66b.PNG'
hashtags = '[#ksi #sidemen #ksivsloganpaul #ksiolajidebt #teamksi #memes #sidemenedit #ksiolajidebthd #dankmemes #ksiedit #sidemenmemes #simonminter #sidemenshow #teamdeji #babatunde #jj #ksimemes #explorepage]'
restofCap = '\n' + '\n' + '🥊 Follow me(@ksi_memepage) for daily ksi memes!' 
subreddit = reddit.subreddit('ksi')
newURL = ''
urlPosted = []

post=7200 #secs
numposts = 100
currenpost=1

while currenpost<=numposts: #num of rounds can be decided here
    for submission in subreddit.hot(limit=25):        
        url = submission.url        
        fileName = str(submission)
        fullPath = filePath + fileName + '.PNG'
        title = '"' + str(submission.title) + '"'
        credit = '(Via: u/' + str(submission.author) + ' on Reddit)'
        caption = title + '\n' + restofCap + '\n' + credit + '\n' + '\n' + '\n' + hashtags        
        if (url.endswith("jpg") or url.endswith("png")) and (not url in urlPosted) and (fullPath != prevPath) and (fullPath != preprePath):
            try:
                saveImage(url, filePath, fileName)
                newURL=url                                                                                                      
                urlPosted.append(url)
                img = Image.open(fullPath)                    
                imgWidth, imgHeight = img.size
                ratio = imgWidth/imgHeight                    
                if(0.8<=ratio<=1.91):
                    if(not bot.upload_photo(fullPath,  caption = caption)):
                        break                    
                    currenpost=currenpost+1 
                    time.sleep(post)
                    subreddit = reddit.subreddit('ksi')
            except:
                print("cant be posted, next...")
                continue
        else:
            continue
        break