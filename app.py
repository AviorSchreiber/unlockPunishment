import pyautogui
import random
import time


def move_mouse_randomly(screen_size,duration=0):
    random_width_pos=random.randrange(0,screen_size.height)
    random_height_pos=random.randrange(0,screen_size.width)
    pyautogui.moveTo(
        random_width_pos,
        random_height_pos,
        duration=duration
    )


screen_size=pyautogui.size()

while True:
    move_mouse_randomly(screen_size,duration=0.2)
    time.sleep(5*60)
