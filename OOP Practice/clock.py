class Clock:
    
    def __init__(self, hours, minutes, seconds, meridiem):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
        self.meridiem = meridiem
        
        
    def alarm(self):
        print(f"Your alarm is set on {self.hours:02}:{self.minutes:02}:{self.seconds:02} {self.meridiem}. ")
        
    def time(self):
        print(f"The time is {self.hours:02}:{self.minutes:02}:{self.seconds:02} {self.meridiem}.")
        