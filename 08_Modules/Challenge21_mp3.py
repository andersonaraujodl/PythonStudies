from pygame import mixer
from time import sleep
import os

absolutePath = os.path.abspath('../source/audio/sample01.mp3')

mixer.init()
mixer.music.load(absolutePath)
mixer.music.play()

while mixer.music.get_busy():  # wait for music to finish playing
    sleep(1)