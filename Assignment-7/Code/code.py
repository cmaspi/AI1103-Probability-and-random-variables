import numpy as np
import matplotlib.pyplot as plt
th_prob=7/20
sample_size=10000
SampleX1=[0]*sample_size
sampleX2=[0]*sample_size
count=0
for i in range(sample_size):
    x1=np.random.choice([0,1],p=[15/25,10/25])
    if x1==0:
        x2=np.random.choice([0,1],p=[14/24,10/24])
        if x2==0:
            count+=1
sim_prob=count/sample_size
print("Theoretical probability=%f, simulated probability=%f"%(th_prob,sim_prob))

cases=['i']

x = np.arange(len(cases))
plt.bar(x + 0.00, th_prob, color = 'green', width = 0.25, label = 'Theoretical')
plt.bar(x + 1, sim_prob, color = 'indigo', width = 0.25, label = 'Simulated')
plt.xlabel('Case')
plt.ylabel('Probabilities')

plt.legend()
plt.show()

