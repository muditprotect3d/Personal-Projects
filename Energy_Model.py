import numpy as np
import matplotlib.pyplot as plt

TANK_VOLUME = 0.17 # m^3
TANK_MASS = TANK_VOLUME * 1000000
TANK_DIAMETER = 0.4 # m
#area of tank through which heat could be lost is the total surface area of the tank 
TANK_AREA_LOSS = ((((TANK_DIAMETER/2)**2) * np.pi) *2) + ((2 * np.pi * (TANK_DIAMETER/2)) * 1.35)
HEAT_LOSSES_COEFF = 0.846 * 3600 # W/m^2/K
AMBIENT_AIR_TEMP = 7 # degC
MAINS_WATER_TEMP = 10 # degC
SPECIFIC_HEAT_WATER = 4.18 #J/g/K
FINAL_WATER_TEMP = 54.4 #degC  (value based off of reccomendation of the Department of Energy for EWH Settings)
T_THERMOSTAT = 54.4 
TOTAL_HEAT_LOSS_DAY = (((FINAL_WATER_TEMP - AMBIENT_AIR_TEMP) * TANK_AREA_LOSS * HEAT_LOSSES_COEFF) *3600 * 24)
MAXIMUM_CAPACITY = 3000 #w
t = np.linspace(0,23,24)
t1 = np.linspace(0,24,25)

def water_heater_power(water_usage: np.ndarray): # Hot water volumetric flow rate in L/s
      T_array = np.zeros(25) #adjusted heating values due to thermostat
      heater_power = np.full(24, 3000.00)

      for i in range(1, 24):   
          T_array[0] = T_THERMOSTAT       
          T_array[i] = ((T_array[i-1] * TANK_MASS * SPECIFIC_HEAT_WATER) +     
                     (MAXIMUM_CAPACITY * 3600) - (
                     3600 * 1000 * water_usage[i-1] * SPECIFIC_HEAT_WATER * ((T_array[i-1]/2) - MAINS_WATER_TEMP)) - (
                     HEAT_LOSSES_COEFF * TANK_AREA_LOSS * ((T_array[i-1]/2) - AMBIENT_AIR_TEMP))
                     ) / ((water_usage[i-1] * 3600 * 1000 * SPECIFIC_HEAT_WATER * 0.5) + (SPECIFIC_HEAT_WATER * TANK_MASS) + (HEAT_LOSSES_COEFF * TANK_AREA_LOSS * 0.5))
           

          if T_array[i] > T_THERMOSTAT:
                    T_array[i] = T_THERMOSTAT
                    heater_power[i-1] = ((((T_array[i] - T_array[i-1]) * 0.5) * TANK_MASS * SPECIFIC_HEAT_WATER) + 
                    (water_usage[i-1] * 1000 * (((T_array[i] + T_array[i-1]) * 0.5) - 10) * SPECIFIC_HEAT_WATER * 3600) + 
                    ((((T_array[i] + T_array[i-1]) * 0.5) - AMBIENT_AIR_TEMP) * TANK_AREA_LOSS * HEAT_LOSSES_COEFF)) / (3600)
      #final_dictionary = {"heater power array": heater_power, "Temperature over time array": T_array}

      return heater_power , T_array

ideal = (water_heater_power(np.array([0]*3+[0.0378]*2+[0]*11+[0.0189]*6+[0]*2)))
print(ideal)


fig1 = plt.figure(num=1, clear=True)
ax1 = fig1.add_subplot(1, 1,1)
ax1.plot(t, ideal[0])
ax1.set(xlabel = "Time", ylabel = "Heater Power", title = "Heater Power over Time")
ax1.grid(True)

#Plotting error for Range Kunta Method
fig2 = plt.figure(num=2, clear=True)
ax2 = fig2.add_subplot(1,1,1)
ax2.plot(t1, ideal[1])
ax2.set(xlabel = "Time (hours)", ylabel = "Temperature", title = "Temperature over Time")
ax2.grid(True)

plt.show()









                
               
          