class WeekdayError(Exception):
    """Custom exception raised when an invalid weekday string is provided"""
    pass
class Weekely:
    # A class variable holding the correct sequence of days.This acts as our calender blueprint
    _validdays =['Mon','Tue','Wed','Thu','Fri','Sat','Sun']

    def __init__(self,day):
        #Automatically grab the first 3 letter and format them eg.Monday to Mon
        formatted_day=day[:3].capitalize()

        if formatted_day not in Weekely._validdays:
            raise WeekdayError(f"'{day} ' is not a valid day of the week.")
        
        self.__day=formatted_day


    def __str__(self):
        """Return the private day string whenever the object is printed """
        return self.__day
    
    def add_days(self,n):
        # Asks the master list for index of currrent days (0 to 6)
        index=Weekely._validdays.index(self.__day)
        # Shifts forward by n
        index=index+n
        # Safely wrap around the week using %7
        new_index=index%7
        # Grab the new day string and save it back into our private variable
        self.__day=Weekely._validdays[new_index]

    def subtract_days(self,n):
         # Asks the master list for index of currrent days (0 to 6)
        index=Weekely._validdays.index(self.__day)
        # Backward by n
        index=index-n
        # Safely wrap around the week using %7
        new_index=index%7
        # Grab the new day string and save it back into our private variable
        self.__day=Weekely._validdays[new_index]
    def is_weekend(self):
        """returns true if its Sat or Sun"""
        return self.__day in ['Sat','Sun']


if __name__== '__main__':
    print("Testing the weekly class")

#testing input
    weekday=Weekely('Monday')
    print(f"Initialized with 'Monday',stored as : {weekday}")

# testing adding days
    weekday.add_days(15)
    print(f'After adding days the result is :   {weekday}')

#testing adding backwards
    weekday.subtract_days(22)
    print(f'After subtracting given days the result is :{weekday} ')

#testing weekend or not
    print(f'is {weekday} a weekend ? :   {weekday.is_weekend()}')

#testing for invalid day
    try:
        print("Attempting to create an in valid day ('funday')")
        invalid_day=Weekely('Funday')
    except WeekdayError as error:
        print(f'Success caught custom exception :{error}')