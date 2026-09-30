from math import sqrt
from abc import ABC,abstractmethod

#========================================================
# 1. Abstract Base class
#========================================================
class SubstationFeeder(ABC):
    
    def __init__(self,feeder_id:str,rated_voltage:float,max_current_limit:float):
        self.feeder_id=feeder_id
        self.rated_voltage=rated_voltage
        self.max_current_limit=max_current_limit
        self._is_tripped = False

        
 # Concrete Method 1
    def check_safety_limit(self,measured_current:float):
        self.measured_current=measured_current
        if measured_current>self.max_current_limit:
            self._is_tripped=True
            print(f"Feeder {self.feeder_id} -Current Overload Fault: Circuit Breaker Tripped!.")

    # Abstract Method   1 
    # Calculate Active power   
    # Making this abstract since Single and Three Phase active power have different formula
    @abstractmethod
    
    def calculate_active_power(self,power_factor=float):
        pass


    # Abstract Method 2
      #"Calculates Apparent Power"
      # Making this abstract since Single and Three Phase reactive power have different formula
    @abstractmethod
    def calculate_apparent_power(self,measured_current:float):
          pass
    
#===========================================================
# 2.Subclass Implementation
#==========================================================
class SinglePhaseFeeder(SubstationFeeder):
    def __init__(self,feeder_id:str,rated_voltage:float=230.0,max_current_limit=63.0):
            super().__init__(feeder_id,rated_voltage,max_current_limit)


    def calculate_apparent_power(self, measured_current: float) -> float:
        self.check_safety_limit(measured_current)
        if self._is_tripped:
            return 0.0
        # Single-Phase: S = V * I
        return self.rated_voltage * measured_current

    def calculate_active_power(self, measured_current: float, power_factor: float) -> float:
        self.check_safety_limit(measured_current)
        if self._is_tripped:
            return 0.0
        # Single-Phase: P = V * I * cos(phi)
        return self.rated_voltage * measured_current * power_factor


class ThreePhaseFeeder(SubstationFeeder):

    def __init__(self, feeder_id: str, rated_voltage: float = 11000.0, max_current_limit: float = 200.0):
        super().__init__(feeder_id, rated_voltage, max_current_limit)
        # Store √3 value for precision
        self._sqrt_3 = sqrt(3)

    def calculate_apparent_power(self, measured_current: float) -> float:
        self.check_safety_limit(measured_current)
        if self._is_tripped:
            return 0.0
        # Three-Phase: S = √3 * V_line * I_line
        return self._sqrt_3 * self.rated_voltage * measured_current

    def calculate_active_power(self, measured_current: float, power_factor: float) -> float:
        self.check_safety_limit(measured_current)
        if self._is_tripped:
            return 0.0
        # Three-Phase: P = √3 * V_line * I_line * cos(phi)
        return self._sqrt_3 * self.rated_voltage * measured_current * power_factor


# ==========================================
# 3. EXECUTION & TEST BLOCK
# ==========================================
if __name__ == "__main__":
    print("--- 🔌 Initializing Substation Monitoring System ---")
    
    # Instantiate our concrete electrical implementations
    domestic_line = SinglePhaseFeeder(feeder_id="Feeder-Residential-A", rated_voltage=230.0, max_current_limit=50.0)
    industrial_line = ThreePhaseFeeder(feeder_id="Feeder-Industrial-01", rated_voltage=11000.0, max_current_limit=150.0)

    print("\n💡 Test 1: Normal Safe Operation")
    # Residential Line pulling 30A with a 0.9 power factor
    s_1ph = domestic_line.calculate_apparent_power(measured_current=30.0)
    p_1ph = domestic_line.calculate_active_power(measured_current=30.0, power_factor=0.9)
    print(f"[{domestic_line.feeder_id}] Apparent Power: {s_1ph/1000:.2f} kVA | Active Power: {p_1ph/1000:.2f} kW")

    # Industrial Line pulling 100A with an 0.85 power factor
    s_3ph = industrial_line.calculate_apparent_power(measured_current=100.0)
    p_3ph = industrial_line.calculate_active_power(measured_current=100.0, power_factor=0.85)
    print(f"[{industrial_line.feeder_id}] Apparent Power: {s_3ph/1000:.2f} kVA | Active Power: {p_3ph/1000:.2f} kW")

    print("\n🚨 Test 2: Overcurrent Fault and Breaker Trip")
    # Simulating a massive industrial load surge to 180A (Limit is 150A)
    print(f"Sending telemetry updates for {industrial_line.feeder_id}...")
    fault_p = industrial_line.calculate_active_power(measured_current=180.0, power_factor=0.85)
    print(f"[{industrial_line.feeder_id}] Calculated Active Power after surge: {fault_p:.2f} Watts")
