# countdown time programme in python

import time         #importing time module

my_time = int(input("Enter the time in seconds: "))     #Asking input from user


#Computing time and displaying in Hours, minutes and seconds

for x in range(my_time, 0, -1):
    seconds = x % 60
    minutes = int(x / 60) % 60
    hours = int(x / 3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)
    



print("TIME UP")

