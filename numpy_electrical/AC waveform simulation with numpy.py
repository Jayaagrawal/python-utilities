import numpy as np
# Parameters
f=50    # frequency of sinusoidal quantity in Hertz
T=1/f   # time period 
t=np.linspace(0,2*T,1000) #Time vector (0 to 10 milliseconds with 1000 sapmles)
Vrms= 230 # RMS voltage
Vm=np.sqrt(2)*Vrms  #Peak or maximum Voltage

# Generation of sinusoidal Voltage

v=Vm*np.sin(2*np.pi*f*t)

# Key Characteritsics
Vpp=2*Vm   # Peak to peak voltage
w=2*np.pi*f   # Angular frequency
print('The maximum Voltage is :',Vm)
print("The peak to peak voltage is :",Vpp)
print('The angular frquency of sinusoidal volatge is:',w)