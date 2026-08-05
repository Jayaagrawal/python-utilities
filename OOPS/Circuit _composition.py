class PowerSource:
    def __init__(self,voltage:float):
        self.voltage=voltage        #Store the voltage value inside the objec

class Resistor:
    def __init__(self,resistance:float):
        self.resistance=resistance      #Store the resistance value inside the object

# Composite Class
class Circuit :
    def __init__(self,voltage:float):
        #COMPOSITION: The circuit creates and owns its own PowerSource object.
        # It takes the 'voltage' number passed by the user and gives it to PowerSource.
        self.power_source=PowerSource(voltage) 
        # COMPOSITION: The circuit prepares an empty list. 
        # This list will hold our Resistor objects later.
        self.resistors=[]

    def add_resistors(self,resistance:float):
          # 1. Create a brand new Resistor object using the number provided
        new_resistor=Resistor(resistance)
        # 2. Append this new object into our internal list
        self.resistors.append(new_resistor)

    def calculate_total_resistance(self)->float:
        # Loop through the list of Resistor objects, extract their '.resistance' value, and sum them up
        total=sum(resistor.resistance for resistor in self.resistors)
        return total
    
    def get_current(self)->float:
        total_r=self.calculate_total_resistance()
# To prevent crashing if there are no resistors (division by zero)
        if total_r ==0:
            return 0.0

        else:
            return self.power_source.voltage/total_r

# Testing the circuit
#1 Create a 12 V volatge source
my_circuit=Circuit(12.0)

#2 Add two resistors
my_circuit.add_resistors(10.0)
my_circuit.add_resistors(20.0)

#3 Print the current 
print(f'Total Resistance:{my_circuit.calculate_total_resistance()} Ohms')
print(f"Total Current :{my_circuit.get_current()} Amps")

