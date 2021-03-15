import numpy as np
from scipy.stats import bernoulli
import random
import matplotlib.pyplot as plt

#theoretical values
th_8=5/36     
th_13=0
th_leq12=1

sample_size=10000
#initialise
sampleB=[0]*sample_size
sampleG=[0]*sample_size

# assigning random values between 1 and 6
for i in range(sample_size):
    sampleB[i],sampleG[i]=int(6*random.random()+1),int(6*random.random()+1)

count_for_8=0
for i in range(sample_size):
    if sampleB[i]+sampleG[i]==8:
        count_for_8+=1
sim_8=count_for_8/sample_size

count_for_13=0
for i in range(sample_size):
    if sampleB[i]+sampleG[i]==13:
        count_for_3+=1
sim_13=count_for_13/sample_size
count_for_leq12=0

for i in range(sample_size):
    if sampleB[i]+sampleG[i]<=12:
        count_for_leq12+=1
sim_leq12=count_for_leq12/sample_size

print("Case i:    Theoretical probability = %f , probability generated from simulation = %f"%(th_8,sim_8))
print("Case ii:   Theoretical probability = %f , probability generated from simulation = %f"%(th_13,sim_13))
print("Case iii:  Theoretical probability = %f , probability generated from simulation = %f"%(th_leq12,sim_leq12))

cases=['i','ii','iii']
probab_theo=[th_8,th_13,th_leq12]
probab_sim=[sim_8,sim_13,sim_leq12]

# plot
x = np.arange(len(cases))
plt.bar(x + 0.00, probab_theo, color = 'red', width = 0.25, label = 'Theoretical')
plt.bar(x + 0.25, probab_sim, color = 'yellow', width = 0.25, label = 'Sim')
plt.xlabel('Cases')
plt.ylabel('Probabilities')
plt.xticks(x  + 0.25/2,['i', 'ii', 'iii'])
plt.legend()
plt.show()
