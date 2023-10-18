import os
import random
import time
import colorama
from colorama import Fore
import pyautogui
import userinput
from progress.bar import Bar


def welcome_message():
    print("**************************\n"
          "*                        *\n"
          "* Welcome to MouseMover! *\n"
          "*                        *\n"
          "**************************\n")


def clear():
    _ = os.system("cls")


def move_mouse_random():
    min_width = int(1)
    min_height = int(1)

    max_width, max_height = pyautogui.size()

    x_pos = random.randint(min_width, max_width)
    y_pos = random.randint(min_height, max_height)

    pyautogui.moveTo(x_pos, y_pos, duration=2, tween=pyautogui.easeInOutQuad)


if __name__ == '__main__':
    while True:
        try:
            colorama.init(autoreset=True)

            welcome_message()

            interval = userinput.ask_for_interval()

            while True:
                clear()

                welcome_message()

                print("To stop press \"Ctrl + C\"")

                with Bar("Waiting for Interval") as bar:
                    for i in range(100):
                        time.sleep(interval / 100)
                        bar.next()

                print(Fore.GREEN + "Moving mouse")

                move_mouse_random()

                clear()
        except KeyboardInterrupt as interrupt:
            clear()

            welcome_message()

            print(Fore.RED + "Stopping...")

            if userinput.ask_for_restart():
                print("Restarting...")
            else:
                break
