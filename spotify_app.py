import spotipy
from user_cred import CLIENT_ID, CLIENT_SECRET, REDIRECT_URI
from spotipy.oauth2 import SpotifyOAuth
import json

# Set your Spotify API credentials
client_id = CLIENT_ID
client_secret = CLIENT_SECRET
redirect_uri = REDIRECT_URI

# Create a Spotify OAuth object
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri, scope='user-read-playback-state user-modify-playback-state'))

def get_active_device():
    devices = sp.devices()
    active_device = next((device for device in devices['devices'] if device['is_active']), None)

    return active_device

def toggle_player():
    active_device = get_active_device()

    # If active_device is not None
    if active_device:
        playback_state = sp.current_playback()

        # If it is playing
        if playback_state is not None and 'is_playing' in playback_state and playback_state['is_playing']:
            sp.pause_playback(device_id=active_device["id"])
            print("Playback paused.")
        # If it is not playing
        else:
            sp.start_playback(device_id=active_device["id"])
            print("Playback started.")
    # Else if active device is None
    else:
        print("No devices are currently active. Start playing music on one of your devices.")

def next_track():
    active_device = get_active_device()
    sp.next_track(device_id=active_device["id"])
    print("Skipped to the next track.")

def previous_track():
    active_device = get_active_device()
    sp.previous_track(device_id=active_device["id"])
    print("Went back to the previous track.")

def enable_shuffle():
    sp.shuffle(state=True)
    print("Shuffle enabled.")

def disable_shuffle():
    sp.shuffle(state=False)
    print("Shuffle disabled.")