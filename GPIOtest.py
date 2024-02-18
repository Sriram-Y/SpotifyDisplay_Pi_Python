from gpiozero import Button
from spotify_app import toggle_player, next_track, previous_track, enable_shuffle, disable_shuffle
import time

play_pause_button = Button(4)
next_button = Button(22)
previous_button = Button(27)
shuffle_button = Button(23)
i = 0;

while True:
    if play_pause_button.is_pressed:
        toggle_player() # No print statements needed as they are built in
        time.sleep(0.5)
    if next_button.is_pressed:
        next_track()
        time.sleep(0.5)
    if previous_button.is_pressed:
        previous_track()
        time.sleep(0.5)

    # Need to track how many times the shuffle is pressed.
    if shuffle_button.is_pressed:
        if i == 0:
            enable_shuffle()
            time.sleep(0.5)
            i += 1
        elif i == 1:
            disable_shuffle()
            time.sleep(0.5)
            i += 1
        if i > 1:
            i = 0