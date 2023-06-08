# I have troubles focusing on things I wanna do rn
# So, I came up with the idea of a reminder of what I'm doing

# This is sargento Pai, he will remind me:
"""
    what I was doing
    why I was doing that thing
 """
# This might help me overcome my mental thoughts... I hope xD

import time
from playsound import playsound

def reproducir_audio():
    playsound('recordings/recording.mp3')

while True:
    time.sleep(6)  # Wait 10 minutes 600
    reproducir_audio()




