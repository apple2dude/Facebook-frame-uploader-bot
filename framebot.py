import time
import facebook
import os


access_token = '' #here goes your access token
facebook_page_id = '' #page id# goes here




episodenum = 9 #episode number
totalframes = 4055 #total number of frames
episodename = "The Time Traveler's Pig" #name of episode
season = 1 #season number



dir_name = ('C:\\Users\\Sam\\Desktop\\Gravity Falls\\Episode ' + str( episodenum )) #path to folder with frames-folder must be named "Episode X" where X is the episode number
framesleft = len([f for f in os.listdir(dir_name) if os.path.isfile(os.path.join(dir_name, f))])
currentframe = totalframes - framesleft + 1

while ( framesleft ) > 0:
    
    graph = facebook.GraphAPI(access_token)

    msg = "Season " + str( season ) + ", Episode " + str( episodenum ) + ' "' + str( episodename) + ',"' + " Frame " + str( currentframe ) + " of " + str( totalframes ) #caption for facebook post- this will make it 'Season Y, Episode X "Episode name," Frame A of B'
    
    graph.put_photo(image = open('C:\\Users\\Sam\\Desktop\\Gravity Falls\\Episode ' + str( episodenum ) + '\\' + str( currentframe ) + '.jpg', 'rb'), message = msg) #path to photo (same as above) and command to post to facebook
    
    os.remove(('C:\\Users\\Sam\\Desktop\\Gravity Falls\\Episode ') + str( episodenum ) + ('\\') + str( currentframe ) + ('.jpg')) #path to photo (same as above) and command to delete frame that was just uploaded

    print('GF Frame ' + str( currentframe ) + ' has been uploaded to Facebook!')

    currentframe=currentframe + 1

    time.sleep(180)
