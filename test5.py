'''

Student Name: Mugdha Chakma
Student ID  : 22122847

test5.py: Simulate spread of disease through a population 
            using SIR model 
 
Based on SIR model:
    Shiflet&Shiflet Module 4.3 Modeling the Spread of SARS S2/24
    and https://www.youtube.com/watch?v=k6nLfCbAzgo 
'''

import matplotlib.pyplot as plt # pyplot module name fixed
import numpy as np
import sys

Scur = 762   # number of people susceptible
Rcur = 0     # number of people recovered
Icur = 1     # number of people infected

trans_const = float(sys.argv[1])   # infectiousness of disease: r = kb/N
recov_rate = float(sys.argv[2])        # recovery rate: a = 1/(# days infected)


simlength = 20          # number of days in simulation

resultarray = np.zeros((simlength,3)) # 2D array of floats 
resultarray[0,:] = Scur, Rcur, Icur     # record initial values

for i in range(1, simlength):
    new_infected = trans_const * Scur * Icur   # = rSI
    new_recovered = recov_rate * Icur          # = aI

    Scur = Scur - new_infected
    Icur = Icur + new_infected - new_recovered # new_recovered variable name fixed
    Rcur = Rcur + new_recovered

    resultarray[i,:] = Scur, Rcur, Icur
 
print("Scur,Rcur,Icur")
for i in range(simlength):
    print("{:.6f}, {:.6f}, {:.6f}".format(resultarray[i,0], resultarray[i,1], resultarray[i,2])) # prints susceptible column of array, add recovered and infected


plt.title(f"SIR Model with r: {trans_const}, a: {recov_rate}") # Figure Title
plt.xlabel('# Days') # Figure X Label
plt.ylabel('# People') # Figure Y Lable

# modify colors and markers
plt.plot(resultarray[:,0], 'k-', label='Susceptible')  # solid black line
plt.plot(resultarray[:,1], 'g^-', label='Recovered')  # green triangles
plt.plot(resultarray[:,2], 'r:d', label='Infected')  # red diamonds

plt.savefig(f"SIR_Model_r_{trans_const}_a_{recov_rate}.png") # save the figure

