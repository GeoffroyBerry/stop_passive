#!/usr/bin/python3
from pynput import keyboard
import time
import threading
from playsound import playsound
import os
import sys

previous_time = time.time()
current_time = time.time()
dirname = os.path.dirname(os.path.abspath(__file__))
music_path = os.path.join(dirname, 'sound.mp3')


def on_press(key):
    global previous_time
    previous_time = time.time()


def check():
    global previous_time
    global music_path
    threading.Timer(float(sys.argv[2]), check).start()

    current_time = time.time()

    if current_time - previous_time > (float(sys.argv[1]) - 0.1):
        playsound(music_path)


def main():
    print('exit with ^C or ^D')
    with keyboard.Listener(on_press=on_press) as listener:
        check()
        listener.join()


if __name__ == '__main__':
    main()
