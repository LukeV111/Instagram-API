from InstagramAPI import InstagramAPI
from datetime import datetime
import time

#Trying to get this thing to fire at a certain date and time.

#print the_date
#print datetime.strftime('%Y-%m-%d %H:%M:S').date()

user, pwd = 'puristcoffee', 'Coffee25'

InstagramAPI = InstagramAPI(user, pwd)
InstagramAPI.login()  # login

#The photo paths will need to be on PythonAnywhere.
photo_path1 = '/Users/LukeVenter/Desktop/IMG_3162.JPG'
caption1 = "Image \n sdfsaf"

photo_path2 = '/Users/LukeVenter/Desktop/IMG_3162.JPG'
caption2 = "Image \n sdfsaf"

photo_path3 = '/Users/LukeVenter/Desktop/IMG_3162.JPG'
caption3 = "Image \n sdfsaf"

#You also need to iterate through a list for the above.

while 1:
    time.sleep(5)
    the_date = datetime.now().strftime('%Y-%m-%d %H:%M')
    print the_date
    print "Checking Again"
    if datetime.now().strftime('%Y-%m-%d %H:%M') == '2017-12-20 16:20': #Set this to the date and time you want to post the post.
        print (caption1) #Post the image here.
        #InstagramAPI.uploadPhoto(photo_path1, caption=caption)
        break
        # Set this to the date and time you want to post the post.
    elif datetime.now().strftime('%Y-%m-%d %H:%M') == '2017-12-20 16:20':
        print (caption2)  # Post the image here.
        #InstagramAPI.uploadPhoto(photo_path2, caption=caption)
        break
    elif datetime.now().strftime('%Y-%m-%d %H:%M') == '2017-12-20 16:20':
        print (caption3)  # Post the image here.
        #InstagramAPI.uploadPhoto(photo_path3, caption=caption)
        break
    else:
        print "not now"
