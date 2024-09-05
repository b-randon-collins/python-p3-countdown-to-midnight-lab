import time

def countdown(seconds):
    if seconds <= 0:
        print("HAPPY NEW YEAR!")
        return
    
    while seconds > 0:
        print(f"{seconds} SECOND(S)!")
        seconds -= 1
        time.sleep(1)
    
    print("HAPPY NEW YEAR!")

def countdown_with_sleep(seconds):
    if seconds <= 0:
        print("HAPPY NEW YEAR!")
        return
    
    while seconds > 0:
        print(f"{seconds} SECOND(S)!")
        seconds -= 1
        time.sleep(1)
    
    print("HAPPY NEW YEAR!")


countdown(10)
countdown_with_sleep(10)