# rubiks-clock-v
Show the time of day on a Rubik's cube.

This is an implementation related to the javascript Clock implemented here: https://github.com/mhirst1960/rubiks-clock
but for computers that are not very powerful at running calculations. The tradeoff
is it uses lots of diskspace.  There are 1441 10-second videos for the 12-hour clock and another 1441 videos for the 24-hour clock.
which adds up to about 900 Megabytes for each of these two variations for 800x480 resolution.  Or 1.7GB to support both clock formats.

This version that shows different video clip every minute.  The videos are simply screen-shot recordings of the javascript version
of rubiks-clock.

# Installation

On Raspberry Pi do this from commandline

pip3 install python-vlc
sudo apt-get install vlc-bin vlc-plugin-base 
pip3 install schedule

# Run
python3 rubiks-clock.py 

<img width="1347" alt="Screenshot 2023-08-02 at 11 39 52 PM" src="https://github.com/mhirst1960/rubiks-clock-v/assets/6749076/bc3f74f5-044e-4ccd-b01e-c4566cecda3a">
