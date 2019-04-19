# import the python auto controller
import pyautogui
#import the time module for waiting
import time

#Set the pause duration to 1 section, pauses for 1 second after every action
pyautogui.PAUSE = 1
#Enable the 'fail-safe' feature, move mouse to upper right hand corner to abort pyautogui
pyautogui.FAILSAFE = True

# import window utility
import ctypes
ctypes.windll.user32.MessageBoxW(0,
"Site Manager is starting. Ensure that your web browser is open to the Azure Experiments Page. Close this message box and unminimize the browser window", "", 1)

#set a variable for sleep timer
sleep = 8

#Wait 4 seconds for user to open appropriate time
time.sleep(4)

#Create a function to click run and then back button
def clickrun():
    #Move the mouse to run button and click
    pyautogui.moveTo(1010,1000, duration=1.25)
    pyautogui.click()
    #Pause sleep seconds for run to start
    time.sleep(sleep)
    #back button to experiments page
    pyautogui.moveTo(20,55, duration=1.25)
    pyautogui.click()

#Move the mouse to first site and click
pyautogui.moveTo(405,380, duration=1.25)
pyautogui.click()

#Move to run, wait, click back button
clickrun()

#Move the mouse to 2nd site and click
pyautogui.moveTo(405,410, duration=1.25)
pyautogui.click()

#Move to run, wait, click back button
clickrun()
               
#Move the mouse to 3rd site and click
pyautogui.moveTo(405,455, duration=1.25)
pyautogui.click()

#Move to run, wait, click back button
clickrun()
