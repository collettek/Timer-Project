import time

def countdown(t):
    
    #displays a countdown timer for a given number of seconds.
    #t = The duration of the countdown in seconds (e.g. 100 seconds).

    while t > 0:
        # use divmod to calculate minutes and seconds
        #divmod(100,60) = (1,40) cuz 
        #100 / 60 is quotient 1 and remainder 40 so 1 minute 40 seconds
        mins, secs = divmod(t, 60)
        
        # format the time as min:sec with leading zeros
        timer = '{:02d}:{:02d}'.format(mins, secs)
        
        # print the timer on the same line 
        print(timer, end="\r")
        
        # pause the timer for 1 second 
        time.sleep(1)
        
        # decrease the time by 1 second
        t -= 1

    print("Time IS UP!      ") 

seconds_input = input("How long in seconds do you want to set the timer for? ")

# check if its a valid number
if seconds_input.isdigit():
    seconds = int(seconds_input)
    countdown(seconds)
else:
    print("Invalid input. Please enter a valid number of seconds.")

    #add a pause function
    

