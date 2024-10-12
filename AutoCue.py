
import pyautogui
import time 
import tkinter as tk
from tkinter import messagebox
from tkinter import *
global songsToCue

#Loop to get mouse position of beat jump
def toFindPos():
    messagebox.showinfo('Beat Jump', 'Move the mouse to the beatjump button and press enter')
    currentMouseX, currentMouseY = pyautogui.position()
    return currentMouseX, currentMouseY

songsToCue = pyautogui.prompt(text='Type in the number of songs that you want to auto cue', title='Number of Songs', default='')

print(songsToCue)
time.sleep(0.2)

beatJumpX, beatJumpY = toFindPos()
print(beatJumpX, beatJumpY)

for i in range(int(songsToCue)):
    # Move mouse to beatjump button if not already there
    pyautogui.moveTo(beatJumpX, beatJumpY)

    # Sleep to allow track to load
    time.sleep(0.5)

    # Left + ctrl to load track
    with pyautogui.hold('ctrl'):  # Press the Control key down and hold it.
        pyautogui.press('left')

    # Sleep
    time.sleep(0.4)

    # Set 1st cue point with CTRL + key '1'
    with pyautogui.hold('ctrl'):
        pyautogui.press('1')

    # Move mouse to forward beat jump and click to jump forward
    pyautogui.moveTo(beatJumpX, beatJumpY)
    pyautogui.click()

    # Sleep
    time.sleep(0.4)

    # Set 2nd cue point with CTRL + key '2'
    with pyautogui.hold('ctrl'):
        pyautogui.press('2')

    # Jump foward by clicking
    pyautogui.click()

    # Sleep
    time.sleep(0.4)

    # Set 3rd cue point with CTRL +  key '3'
    with pyautogui.hold('ctrl'):
        pyautogui.press('3')

    # Jump foward  2X by clicking twice
    pyautogui.click()
    pyautogui.click()

    # Sleep
    time.sleep(0.4)

    # Set 4rd cue point with CTRL +  key '4'
    with pyautogui.hold('ctrl'):
        pyautogui.press('4')

    # Jump foward X2 by clicking twice
    pyautogui.click()
    pyautogui.click()

    # Sleep
    time.sleep(0.4)

    # Set 5th cue point with CTRL +  key '5'
    with pyautogui.hold('ctrl'):
        pyautogui.press('5')

     # Sleep
    time.sleep(0.4)

    # Jump foward X2 by clicking twice
    pyautogui.click()
    pyautogui.click()

    # Move mouse to 6th cue point top right corner and click
    pyautogui.moveTo(191,264)
    pyautogui.click()

    # Move mouse to 6th cue point bottom and click
    pyautogui.moveTo(166,304)
    pyautogui.click()

    # Click down to go to next track
    pyautogui.press('down')
    time.sleep(0.4)
quit()