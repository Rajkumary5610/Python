# Alarm setting programme in python

import time
import datetime          #Time 24 hours formate
import pygame
import re


def set_alarm(alarm_time):
    print(f'Alarm is set at {alarm_time}')

    pattern = r"^([01]\d|2[0-3]):([0-5]\d):([0-5]\d)$"
    if re.match(pattern, alarm_time):
        print(f"the given alarm time {alarm_time} is in 'HH:MM:SS' formate ")
    else:
        print(f"the given alarm time {alarm_time} is not in 'HH:MM:SS' formate")
        return set_alarm

    is_running = True
    sound_file = "Music_file.mp3"

    while is_running:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(f"Current Time: {current_time}")

        if alarm_time == current_time:
            print("Wake Up!")

            pygame.mixer.init()
            pygame.mixer.music.load(sound_file)
            pygame.mixer.music.play()

            while pygame.mixer.music.get_busy():            #Play's music till the complete song is played in the file
                time.sleep(1)

            is_running = False

        elif alarm_time < current_time:
            print(f"The alarm time {alarm_time} is lesser than current time {current_time}")
            return set_alarm

        time.sleep(1)

if __name__ == '__main__':
    alarm_time = input("Enter the alarm time (HH:MM:SS): ")
    set_alarm(alarm_time)