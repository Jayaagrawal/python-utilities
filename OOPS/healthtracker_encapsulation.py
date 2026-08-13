class HealthTracker:
    def __init__(self,username:str,heart_rate=70):
        self.username=username
        self._heart_rate=heart_rate

    @property
    def heart_rate(self):
        print(f"Reading secure pulse stream for {self.username}")
        return self._heart_rate
    
    @ heart_rate.setter
    def heart_rate(self,new_pulse):
        if not isinstance(new_pulse,int):
            print(f'X Type error :heart rate must be integer,not {type(new_pulse).__name__}.')
        elif  new_pulse <=40 or new_pulse>220:
            print(f" XX Biometric error {new_pulse} BPM is physically impossible.Input Rejected")
        else:
            self._heart_rate=new_pulse
            print(f"Pulse update verified .The new value is {new_pulse}")

tracker=HealthTracker(username='John')
 # Test Case A:Read the default heart rate 
print(f'The baseline heart rate is {tracker.heart_rate} BPM')

 # Test Case B :A valid heart rate
tracker.heart_rate=149
print(f'Updated heart rate is {tracker.heart_rate} BPM')

# Test Case C : Assign an invaid heart Rate
tracker.heart_rate=39

 # Test Case D :Invalid data type udpade 
tracker.heart_rate="Very High pulse Rate"   

