from datetime import datetime
from pygame import mixer
from time import time

def musiconloop(file, stopper):
    mixer.init()
    mixer.music.load(file)
    
    while True:
        mixer.music.play()
        a = input()
        if a == stopper:
            mixer.music.stop()
            break

def lognow(file, msg):
    with open(file, "a") as f:
        f.write(f"{msg} {datetime.now()}\n")

if __name__ == "__main__":
    init_water = 5
    init_eyes = 10
    init_exercise = 15

    water = time()
    eyes = time()
    exercise = time()

    while True:
        if(time()-water) > init_water:
            print("Enter drank to stop the music", end=" ")
            musiconloop("water.mp3", "drank")
            lognow("Water log.txt", "Drank Water at")
            water = time()

        if(time()-eyes) > init_eyes:
            print("Enter eydone to stop the music", end=" ")
            musiconloop("eyeex.mp3", "eydone")
            lognow("Eyes log.txt", "Eyes exercise at")
            eyes = time()

        if(time()-exercise) > init_exercise:
            print("Enter exdone to stop the music", end=" ")
            musiconloop("physicalex.mp3", "exdone")
            lognow("Physical log.txt", "Physical exercise done at")
            exercise = time()