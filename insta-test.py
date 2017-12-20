from InstagramAPI import InstagramAPI
from datetime import datetime
import time

#Trying to get this thing to fire at a certain date and time.

#print the_date
#print datetime.strftime('%Y-%m-%d %H:%M:S').date()

user, pwd = 'puristcoffee', 'Coffee25'

InstagramAPI = InstagramAPI(user, pwd)
InstagramAPI.login()  # login

# You need to iterate through a list here.
photo_path = '/Users/LukeVenter/Desktop/IMG_3162.JPG'
caption = "Image \n sdfsaf" 
#You also need to iterate through a list for the above.

while 1:
    time.sleep(5)
    the_date = datetime.now().strftime('%Y-%m-%d %H:%M')
    print the_date
    print "Checking Again"
    if datetime.now().strftime('%Y-%m-%d %H:%M') == '2017-12-20 16:20': #Set this to the date and time you want to post the post.
        print (caption) #Post the image here.
        #InstagramAPI.uploadPhoto(photo_path, caption=caption)
        break
    else:
        print "not now, nope"
