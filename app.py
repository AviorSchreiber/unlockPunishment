#!/usr/bin/python2.7
import random
import time
import sys
import os

def notify(title, text):
    os.system("""
              osascript -e 'display notification "{}" with title "{}" sound name "Submarine"'
              """.format(text, title))

if os.path.exists("/tmp/lockfile"):
    print("Already running, exiting...")
    sys.exit(0)

os.system("touch /tmp/lockfile")

try:
    # time.sleep(2*60*60) #1 Hour for startup
    while True:
        notify("It-Security Awareness", "Do not forget to lock your screen,When you going out of your position...")
        time.sleep(random.randrange(0,300))
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
