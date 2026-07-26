import math
class CircuitComponent():
    def __init__(self,name,value):
        "Initializes foundational circuit component metrics"
        self.__name=name
        self.__value=value
    def get_name(self):
        "Getter method to safely read the component identifier."
        return self.__name
    def get_value(self):
        "Getter method to safely read the raw electrical value."
        return self.__value
    def get_impedance(self,frequency):                                      
        "Default impedance placeholder to be overridden by child classes."
        return 0
class Resistor(CircuitComponent):
    """A resistor's impedance is independent of frequency."""
    def get_impedance(self, frequency):
        return self.get_value()
    
class Capacitor(CircuitComponent):
    """Calculates capacitive reactance, handling DC circuit condition."""
    def get_impedance(self, frequency):
        if frequency==0:
            return float('inf')
        else:
            return (1/(2*(math.pi)*frequency*self.get_value()))

    
class Inductor(CircuitComponent):
    """Calculates inductive reactance"""
    def get_impedance(self, frequency):
            return (2*(math.pi)*frequency*self.get_value())
        
"""Execution and Demonstration Block"""
if __name__=='__main__':
    print('Circuit Impdeance Calculator')

    """ 1.Initialize a 20 ohm resistor"""
    R1=Resistor("R1",20.0)

    """2.Initialize a 0.01 farad capacitor"""
    C1=Capacitor("C1",0.01)

    """3.Initalize a 0.05 Henry inductance"""
    L1=Inductor("L1",0.05)

    """4.Testing"""
    print(f"{R1.get_name()} impedance at 50 hz is :{R1.get_impedance(50)} Ohms")
    print(f"{C1.get_name()} impedance at 0 hz is :{C1.get_impedance(0)} Ohms")
    print(f"{C1.get_name()} impedance at 100 hz is :{C1.get_impedance(100)} Ohms")
    print(f"{L1.get_name()} impedance at 0 hz is :{L1.get_impedance(0)} Ohms")
    print(f"{L1.get_name()} impedance at 150 hz is :{L1.get_impedance(150)} Ohms")


    