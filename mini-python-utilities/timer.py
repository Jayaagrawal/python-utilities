class Timer:
    """Initializes the Timer object with military time values.
        Includes validation checks to prevent invalid time inputs."""
    def __init__(self,hours=0,minutes=0,seconds=0):
      #Validate hours (Must be between 0 and 23 for military time)
      if hours<0 or hours>23:
          raise ValueError("Hours must be between 0 and 23")
     
      #Validate minutes (Must be between 0 and 59)
      if minutes<0 or minutes>59:
          raise ValueError("Minutes must be between 0 and 59")
     
    #Validate seconds (Must be between 0 and 59)  
      if seconds<0 or seconds>59:
          raise ValueError("Seconds must be between 0 and 59")
    # If all checks pass, save the values into permanent instance variables
      self.hours=hours
      self.minutes=minutes
      self.seconds=seconds

    def __str__(self):
       """Converts the timer object into a human-readable string format: hh:mm:ss.
        Uses ':02d' to ensure numbers less than 10 always have a leading zero."""
       return f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}"
    
    def next_second(self):
       """Increments the time stored inside the object by exactly +1 second.
        Handles nested wrap-arounds for seconds, minutes, and hours (midnight)."""
      
       self.seconds=self.seconds+1
        ## If seconds hit 60, reset them to 0 and advance the minutes
            
       if self.seconds==60:             
            self.seconds=0
            self.minutes=self.minutes+1
            #If minutes hit 60, reset them to 0 and advance the hours
            if self.minutes==60:
                self.minutes=0
                self.hours=self.hours+1
                #  If hours hit 24, wrap around back to midnight (00)
                if self.hours==24:
                        self.hours=0
            
    def previous_second(self):
        """Decrements the time stored inside the object by exactly -1 second.
        Handles nested underflows for seconds, minutes, and hours."""
        self.seconds=self.seconds-1
        # If seconds drop below 0, roll back to 59 and decrease the minutes
        if self.seconds<0:
            self.seconds=59
            self.minutes=self.minutes-1
        #  If minutes drop below 0, roll back to 59 and decrease the hours
            if self.minutes<0:
                self.minutes=59
                self.hours=self.hours-1
        # If hours drop below 0, wrap back to the previous day (23)
                if self.hours<0:
                    self.hours=23

# Create a clock at 1 second before midnight
clock=Timer(22,59,59)
print("Start time:",clock)
# Roll forward
clock.next_second()
print("Tick forward:",clock)
# Roll Backward
clock.previous_second()
print("Tick backward:",clock)