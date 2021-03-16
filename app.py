#!/usr/bin/python2.7
import random
import time
import sys
import os

if os.path.exists("/tmp/lockfile"):
    print("Already running, exiting...")
    sys.exit(0)

os.system("touch /tmp/lockfile")

time.sleep(2*60*60) #1 Hour for startup
def notify(title, text):
    os.system("""
              osascript -e 'display notification "{}" with title "{}" sound name "Submarine"'
              """.format(text, title))
try:
    while True:
        notify("It-Security Awareness", "Dont Forget To lock your screen,When you play Snooker...")
        time.sleep(random.randrange(0,10))
except:
    print("Ending...")
    os.system("rm /tmp/lockfile")




















#
# def move_mouse_randomly(screen_size,duration=0):
#     random_width_pos=random.randrange(0,screen_size.height)
#     random_height_pos=random.randrange(0,screen_size.width)
#     print(f"moving to {random_width_pos},{random_height_pos}")
#     pyautogui.moveTo(
#         random_width_pos,
#         random_height_pos
#     )
#
#
# screen_size=pyautogui.size()
#
# # while True:
# #     # move_mouse_randomly(screen_size,duration=0.2)
# #     time.sleep(random.randrange(0,10))
