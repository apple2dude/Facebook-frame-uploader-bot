# Facebook-frame-uploader-bot

This project is for uploading frames of tv shows, cartoons, whatever images you want really, to Facebook in a timed and ordered way. Frames need to be named sequentially 1.jpg, 2.jpg, 3.jpg, etc. for this to work, and also need to be placed in a folder titled "Episode X" where X is some number. Everything else should be pretty self explanatory with the comments in the code

I initially based this off of the code that originally ran the Every Tom and Jerry Frame In Order page, but have made lots of changes since I first adapted it last fall. If the Facebook API changes I'll likely update the code, as I have two pages (Every Magic School Bus Frame In Order and Every Gravity Falls Frame In Order) running off it.

UPDATE 11/2020
declassified.py can be executed to start the program.  This will run neds-uploader.py (rename it if you want, but make sure to change the name in declassified.py too), and will automatically restart it if it crashes for whatever reason.
Additionally, a second loop has been built into the main program, so that frames are uploaded in sets of 20 every hour, rather than once every 3 minutes.  This is to hopefully help increase engagement in posts by getting facebook to show them more.
