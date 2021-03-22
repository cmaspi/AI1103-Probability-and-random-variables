import numpy as np
from scipy.stats import bernoulli
import random
import matplotlib.pyplot as plt


th_prob=2/9

sample_size=10000
#initialise
sample1=[0]*sample_size
sample2=[0]*sample_size

# assigning random values between 1 and 6
for i in range(sample_size):
    sample1[i],sample2[i]=int(6*random.random()+1),int(6*random.random()+1)

count=0
for i in range(sample_size):
    if (sample1[i]*sample2[i]) in [1,4,9,16,25,36]:
        count+=1
        
sim_prob=count/sample_size

print("Theoretical probability =%f, simulated probability=%f"%(th_prob,sim_prob))

cases=['i']

x = np.arange(len(cases))
plt.bar(x + 0.00, th_prob, color = 'black', width = 0.25, label = 'Theoretical')
plt.bar(x + 1, sim_prob, color = 'orange', width = 0.25, label = 'Sim')
plt.xlabel('Case')
plt.ylabel('Probabilities')

plt.legend()
plt.show()
