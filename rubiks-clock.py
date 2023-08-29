# This python script shows the time of day on the face of a Rubik's cube
# The script is very simple.  Every minute it plays a short video of a Rubik's cube
# transitioning to show a new set of numbers on the front.
#
# The videos are captured from the rubiks-clock javascript webpage that can be found running here:
#   rubiksclock.com
#   24.rubiksclock.com
#
# This is intended to run on a Raspberry Pi computer as it relies on the vlc video player.
# The technique of showing simple videos may be useful for less-powerful computers that may not
# be able to handle the complex calculations of the javascript from rubiksclock.com . But it has
# the disadvantage the it uses a lot of sdcard memory to store the images.  The image quality is not
# nearly as good for the videos compared to the vector graphics from the original javascript webpage.
#
# Author: Michael Hirst
# License: MIT
#

import argparse

import schedule
import time
import datetime
import subprocess
import vlc

#from guizero import App, Picture
#import PIL
#from PIL import Image

#import moviepy.editor as mp

import tkinter


def tkAnimateGIF(ind):

    global label
    global root
    global frames
    global frameCnt
    global numFrames

    frame = frames[ind]
    ind += 1
    if ind == numFrames:
        ind = 0
        root.quit()
        return
    label.configure(image=frame, width=200, height=120)
    root.after(100, tkAnimateGIF, ind)
     
def showNextMinute():

    global vlcInstance
    global app

    global label
    global root
    global frames
    global frameCnt
    global numFrames
    
    now = datetime.datetime.now()
    soon = now + datetime.timedelta(0,3) # 0 days,  3 seconds in the future

    hour = int(soon.hour)
    min = int(soon.minute)
    filename = f"{videoDir}/rubiks-clock-{hour:02d}{min:02d}.gif"
    isGif = False
    
    useImageViewer = False
    useVLC = False
    useMoviepy = False
    useGuizero = False
    useTkinter = True
    
    if useImageViewer:
        img = Image.open(filename)
        img.show()

    if useVLC:
        if isGif:
            #TODO:  conversion gif to mp3 is hopelessly slow
            print (f"read gif: {filename}")
            gif = mp.VideoFileClip(filename)
            mp4 = "/tmp/rubiks-clock.mp4"
            print (f"write mp4: {mp4}")
            gif.write_videofile(mp4, fps=24)
            print (f"init VLC...")
            video = vlcInstance.media_new(mp4)
        else:
            video = vlcInstance.media_new(filename)
        player.set_media(video)
        print (f"play on VLC...")

        player.play()
        
    if useMoviepy:
        #gif = mp.VideoFileClip(filename)

        #gif = PIL.Image.open(filename)
        pic = Picture(app, image=gif)
        app.display()
        
    if useGuizero:
        app = App()
        pic = Picture(app, image=filename)
        app.display()
        
    if useTkinter:
        
        print ("useTkinter..")
        root = tkinter.Tk()
        canvas = tkinter.Canvas(root)
        canvas.grid(row = 0, column = 0)
        # create the canvas, size in pixels
        #canvas = tkinter.Canvas(width = 300, height = 200, bg = 'yellow')

        # pack the canvas into a frame/form
        #canvas.pack(expand = tkinter.YES, fill = tkinter.BOTH)
        canvas.pack()

        # load the .gif image file
        # put in your own gif file here, may need to add full path
        # like 'C:/WINDOWS/Help/Tours/WindowsMediaPlayer/Img/mplogo.gif'
        #gif1 = tkinter.PhotoImage(file = filename)
        
        # put gif image on canvas
        # pic's upper left corner (NW) on the canvas is at x=50 y=10
        #canvas.create_image(50, 10, image = gif1, anchor = tkinter.NW)
        
        numFrames = 0
        frameCnt = 100
        frames = []
        for frameNum in range(frameCnt):
            try:
                frame = tkinter.PhotoImage(file=filename,format = f'gif -index {frameNum}')
                frames = frames + [frame]
                numFrames = numFrames + 1
            except Exception:
                break



        label = tkinter.Label(root)
        label.pack()
        root.after(0, tkAnimateGIF, 0)

        # run it ...
        print ("tkinter loop..")
        tkinter.mainloop()
        print ("tkinter loop done.")
    
parser = argparse.ArgumentParser(prog='rubiks-clock', description="Shows time of day on a Rubik's Cube")
parser.add_argument('--type', choices=["12", "24"], default="12")

args = parser.parse_args()

print (f"type = {args.type}")
if args.type == "12":
    videoDir = "videos/12hourclock-200x120"
else:
    videoDir = "videos/24hourclock-200x120"

print (f"videos in {videoDir}")

#exit

vlcInstance = vlc.Instance("--aout=alsa")
player = vlcInstance.media_player_new()

if False:
    app = App()

showNextMinute()

schedule.every().minute.at(":59").do(showNextMinute)

try:
    while True:
        schedule.run_pending()
        time.sleep(1)

except KeyboardInterrupt:

    player.stop()

