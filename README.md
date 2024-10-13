# Dice's Serato DJ AutoCue program v1.0
This is a python script used to automate the setting of cue points in Serato DJ software. This code is based off of [Bide's Rekordbox AutoCuer v1.0](https://github.com/Bide-UK/Bides-Rekordbox-AutoCuer?tab=readme-ov-file#bides-rekordbox-autocuer-v10-) 
which can be found at the link provided. I have kept this README the same as Bide's while adjusting for where the python program differs from the apple script version. This program is necessary because Bide's program uses AppleScripts which excludes Windows/Linux users from running 
the program sucessfully without having to use methods to run Applecripts on Windows/Linux.
The program automates the default keyboard shortcuts to set cue points automatically. The following configuration is how the cue points will be set.

```
A: 0 - B:4 - C:8 - D:16 - E:32 - F:40
```
# Installation Guide
1. Click the Green Code button at the top of this page and click download zip.
2. Unpack the zip (double click).
3. Double Click the AutoCue.py file.

# How to Use
1. Ensure Serato DJ is open and in the Left Player.
2. To make sure that you've aligned the beat grid correctly with the first cue on the first down beat enable the Quantize feature in the top left corner next to the "MIDI" button.
3. Analyze all of the tracks in the playlist before running the program.
4. Record how many tracks are in the playlist. (For best results use this on tracks that don't have cue points set.)
5. Load the first track on the playlist and ensure it's loaded in the player in 1 player mode, the script works downwards in a given playlist.
6. Enter the number of tracks you want to process and press ok e.g playlist has 100 tracks put 100
7. Wait for the program to finish (DO NOT LET THE COMPUTER SLEEP, TOUCH KEYBOARD or click out of the window).
In an emergency press cmd+alt+esc and try to quit the script process. The script uses keystrokes to automate Rekordbox so it will try to fight you.
