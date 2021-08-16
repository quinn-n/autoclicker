#!/usr/bin/env python3.6
import pyautogui
import sys
import time
import os
import psutil
import multiprocessing
if len(sys.argv) == 2:
    if sys.argv[1] == "-h" or sys.argv[1] == "--help":
        print("Usage: "+sys.argv[0]+" <number of threads>")
        sys.exit()
    numOfProcesses = int(sys.argv[1])
else:
    numOfProcesses = 10
time.sleep(1)
def clicker():
    me = psutil.Process(os.getpid())
    while True:
        if me.parent != None:
            pyautogui.click()
        else:
            exit()
if __name__ == "__main__":
    multiprocessing.set_start_method("spawn")
    for i in range(0,numOfProcesses):
        print("starting thread "+str(i))
        clickerProcess = multiprocessing.Process(target=clicker)
        clickerProcess.start()
    print("Press Ctrl+C to exit, or Ctrl+Z to pause.")
