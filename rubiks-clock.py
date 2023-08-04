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


def showNextMinute():

    global vlcInstance
    
    now = datetime.datetime.now()
    soon = now + datetime.timedelta(0,3) # 0 days,  3 seconds in the future

    hour = int(soon.hour)
    min = int(soon.minute)
    filename = f"{videoDir}/rubiks-clock-{hour:02d}{min:02d}.mpg"
    
    video = vlcInstance.media_new(filename)
    player.set_media(video)

    player.play()

parser = argparse.ArgumentParser(prog='rubiks-clock', description="Shows time of day on a Rubik's Cube")
parser.add_argument('--type', choices=["12", "24"], default="12")
#parser.add_argument('-12', dest='doClock12', action='store_true')
#parser.add_argument('-24', dest='doClock12', action='store_false')
#parser.set_defaults(doClock12=True)

args = parser.parse_args()

print (f"type = {args.type}")
if args.type == "12":
    videoDir = "videos/12hourclock-800x480"
else:
    videoDir = "videos/24hourclock-800x480"

print (f"videos in {videoDir}")

exit

vlcInstance = vlc.Instance("--aout=alsa")
player = vlcInstance.media_player_new()

showNextMinute()

schedule.every().minute.at(":59").do(showNextMinute)

try:
    while True:
        schedule.run_pending()
        time.sleep(1)

except KeyboardInterrupt:

    player.stop()

