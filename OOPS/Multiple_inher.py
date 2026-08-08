# Core Apex class
class Engine:
    def start(self):
        print("Engine:spark plugs firing .Fuel pumps online")

# Subsysytem classes 
class Fuelsystem(Engine):
    def start(self):
        print("FuelSystem:Injecting fuel mixture.....")
        super().start()

class Electronics(Engine):
    def start(self):
            print("Electronics:Running diagnostic scan.....")
            super().start()

# Composite class
class Sportcar(Fuelsystem,Electronics):
     def start(self):
          print("SportsCar:Initiating Performance Start sequence....")
          super().start()


 
my_car=Sportcar()
my_car.start()
