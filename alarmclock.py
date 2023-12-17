import time
import pygame

def set_alarm(alarm_time, sound_file):
    current_time = time.strftime("%H:%M")
    while current_time != alarm_time:
        print(f"Current Time: {current_time}")
        current_time = time.strftime("%H:%M")
        time.sleep(1)
    
    print("Wake up!")
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(sound_file)
    pygame.mixer.music.play()
    time.sleep(10)  # Wait for 10 seconds to allow the sound to play

# Example usage:
alarm_time = "20:53"  # Set your alarm time here in HH:MM format
sound_file = r"sound\Loud_Alarm_Clock_Buzzer-Muk1984-493547174.mp3"  # Replace with your audio file path using raw string literal
set_alarm(alarm_time, sound_file)
