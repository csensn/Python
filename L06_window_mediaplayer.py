from pygame import mixer

mixer.init()
mixer.music.load("D:\Songs\Shubh\Baller.mp3")
mixer.music.set_volume(70)
mixer.music.play()

while(1):
    print("press 'p' to pause , 'r' to resume")
    print("press 'e' to exit the program")
    choice1 = input("Enter your choice: ")
    if choice1 == 'p':
        mixer.music.pause()
    elif choice1 == 'r':
        mixer.music.unpause()
    elif choice1 == 'e':
        mixer.music.stop()
    break

# import pygame
# from moviepy.editor import *
# clip = VideoFileClip("C:\Users\nsnar\Downloads\HaayeVe.mp4")
# clip.preview()
# pygame.quit()