import threading
import time

from pynput import keyboard
from pynput.keyboard import Controller
from win10toast import ToastNotifier

import idle
import settings
import splash

# Init variables
keyboard1 = Controller()
toast = ToastNotifier()
splash.print_splash_screen_intro()

active = False
user_idle = False
running = True


# Functions
def on_key_release(key):
    global active, running
    # print('Released Key %s' % key)

    if str(key) == "'m'":
        if active:
            active = False
            print("ANTI-AFK OFF")
        else:
            active = True
            print("ANTI-AFK ON")

    if str(key) == "'!'":
        running = False


def anti_afk():
    global user_idle
    while running:
        if idle.get_idle_duration() >= settings.get_timeout_duration():
            user_idle = True
            toast.show_toast(
                "Anti-AFK",
                "Started sending random inputs on your keyboard",
                duration=5,
                threaded=True,
            )
        if idle.get_idle_duration() < settings.get_timeout_duration() and user_idle:
            user_idle = False
            print("User back in activity.")
        if active and user_idle:
            keyboard1.press("w")
            keyboard1.press("z")
            time.sleep(1)
            keyboard1.press("d")
            time.sleep(1)
            keyboard1.press("a")
            keyboard1.press("q")
            time.sleep(1)
            keyboard1.press("s")
            time.sleep(1)


# Main script
listener = keyboard.Listener(on_release=on_key_release)
listener.start()

anti_afk_thread = threading.Thread(target=anti_afk)
anti_afk_thread.start()
anti_afk_thread.join()

listener.stop()
