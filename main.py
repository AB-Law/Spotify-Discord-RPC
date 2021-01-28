from SwSpotify import spotify
from pypresence import Presence
import time
import random
from datetime import datetime

now = datetime.now()

current_time = now.strftime("%H:%M:%S")

CLIENT_ID = '804217292434309143'
RPC = Presence(CLIENT_ID)

DESC = "Spotify Presence created by A Law#7777"

spotify_g = "spotify"
spotify_b = "spotify_black"

icons = [spotify_b, spotify_g]


def icon():
    return random.choice(icons)


def update(title, artist):
    RPC.update(
        large_image=icon(),
        large_text=DESC,
        small_image=icon(),
        small_text="Vibing to " +
        title + "by " + artist,
        details=title
    )


def stopped():
    RPC.update(
        large_image=icon(),
        large_text=DESC,
        small_image=icon(),
        small_text="Stopped",
        details="Paused")


RPC.connect()
while True:
    time.sleep(0.1)
    try:
        title, artist = spotify.current()
        print(title, artist)
        update(title, artist)
        time.sleep(5)
        print('start')
    except:
        print('stop')
        stopped()
        time.sleep(5)
        continue
