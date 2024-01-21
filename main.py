from time import sleep
from spotify_app import sp
from spotify_app import toggle_player, next_track, previous_track, enable_shuffle, disable_shuffle

def test1():
    # Toggle player state (function should take care of whether to play or 
    # pause and throw error if there is no active devices).
    print("Starting TEST #1 - Start and stop playback")
    # Start. Pause, Start, Pause
    # Pause. Start, Pause, Start
    toggle_player()
    sleep(3)
    
    toggle_player()
    sleep(3)

    toggle_player()
    sleep(3)


def test2():
    # Next and previous tracks 
    print("Starting TEST #2 - Change track (next and previous)")
    next_track()
    sleep(3)
    
    toggle_player()
    sleep(3)
    
    previous_track()
    sleep(3)

def test3():
    # Test #3 - Shuffle
    # Enable shuffle
    enable_shuffle()

    # Next track
    next_track()
    sleep(3)

    # Next track
    next_track()
    sleep(3)

    # Previous track
    previous_track()
    sleep(3)

    # Previous track
    previous_track()
    sleep(3)

    # Disable shuffle
    disable_shuffle()
    sleep(3)

    # Next track
    next_track()
    sleep(3)

    # Next track
    next_track()
    sleep(3)

test1()
