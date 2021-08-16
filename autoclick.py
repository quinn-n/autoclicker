#!/usr/bin/env python
import pyautogui
import sys
import time
import os
import psutil
import multiprocessing
if len(sys.argv) == 2:
    timeToPause = float(sys.argv[1])
else:
    timeToPause = .1
pyautogui.PAUSE = timeToPause
time.sleep(1)
def clicker():
    me = psutil.Process(os.getpid())
    while True:
        if me.parent != None:
            pyautogui.click()
        else:
            exit()
clickerProcess = multiprocessing.Process(target=clicker)
clickerProcess.start()
input("Press enter to exit.")
clickerProcess.terminate()
