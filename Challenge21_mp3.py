from pygame import mixer
from time import sleep

mixer.init()
mixer.music.load('C:/Dev/Python/PythonStudies/source/audio/sample01.mp3')
mixer.music.play()

while mixer.music.get_busy():  # wait for music to finish playing
    sleep(1)