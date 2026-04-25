
#Simulate the magnitude of current in a series RLC circuit as the input frequency varies. This demonstrates resonance behavior
import numpy as np
import matplotlib.pyplot as plt

#Circuit Parameters
R=10        # Resistance in Ohms
L=1e-3      # Inductance in Henry
C=1e-6      # Capacitance in farads
Vin=100     # Input Voltage in Volts


# Frequencey Variation (1kHz to 100Khz)
f=np.linspace(1e3,100e3,1000)       
w=2*np.pi*f     # angular frequency


# Impedance of each element
Z_r= R 
Z_l=1j*w*L         #inductive reactance in ohms
Z_c=1/(1j*w*C)      # inductive capacitance in ohms

# Total impedance
Z_total=Z_r+Z_l+Z_c         #total impedance of circuit in ohms

# Current magnitude
I=Vin/Z_total
I_mag=np.abs(I)

#Plot
plt.plot(f/1000,I_mag)
plt.title("RLC series resonance")
plt.xlabel("Frequency(khz)")
plt.ylabel("Current Magnitude(Amp)")
plt.grid(True)
plt.show()