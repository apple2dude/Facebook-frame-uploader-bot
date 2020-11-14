import time
import facebook
import os


access_token = '' #here goes your access token from http://maxbots.ddns.net/token
facebook_page_id = ''




episodenum = 14 #episode number
totalframes = 4074 #total number of frames
episodename = '"Secrets" and "School Car Washes,"' #name of episode
season = 2 #season number



dir_name = ("C:\\Users\\Sam\\Desktop\\Ned's Declassified\\Episode " + str( episodenum ))
framesleft = len([f for f in os.listdir(dir_name) if os.path.isfile(os.path.join(dir_name, f))])
currentframe = totalframes - framesleft + 1

while ( framesleft ) > 0:

    postofset = 0

    while ( postofset ) < 20:
    
        graph = facebook.GraphAPI(access_token, version="7.0")

        msg = "Season " + str( season ) + ", Episode " + str( episodenum ) + " " + str( episodename ) + " Frame " + str( currentframe ) + " of " + str( totalframes ) #caption for facebook post
    
        graph.put_photo(image = open("C:\\Users\\Sam\\Desktop\\Ned's Declassified\\Episode " + str( episodenum ) + '\\' + str( currentframe ) + '.jpg', 'rb'), message = msg) #path to photo and command to post to facebook
    
        os.remove(("C:\\Users\\Sam\\Desktop\\Ned's Declassified\\Episode ") + str( episodenum ) + ('\\') + str( currentframe ) + ('.jpg'))

        print("Ned's Frame " + str( currentframe ) + ' of ' + str( totalframes ) + ' has been uploaded to Facebook!')

        currentframe=currentframe + 1

        postofset = postofset + 1

        time.sleep(1)

    time.sleep(3496)

