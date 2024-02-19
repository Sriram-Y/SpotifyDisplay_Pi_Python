from gpiozero import Button
from spotify_app import toggle_player, next_track, previous_track, enable_shuffle, disable_shuffle
import time

play_pause_button = Button(4)
next_button = Button(22)
previous_button = Button(27)
shuffle_button = Button(23)

shuffle_flag = False;

# TODO: Need to have initialize routine (our flags must reflect the state of the player)

while True:
    if play_pause_button.is_pressed:
        toggle_player() # No print statements needed as they are built in
        time.sleep(0.2)
    if next_button.is_pressed:
        next_track()
        time.sleep(0.2)
    if previous_button.is_pressed:
        previous_track()
        time.sleep(0.2)

    # Need to track how many times the shuffle is pressed.
    if shuffle_button.is_pressed:
        if shuffle_flag == False:
            enable_shuffle()
            shuffle_flag = True
        elif shuffle_flag == True:
            disable_shuffle()
            shuffle_flag = False
        time.sleep(0.5)
