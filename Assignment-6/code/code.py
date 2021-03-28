import numpy as np
import matplotlib.pyplot as plt

th_prob_E=0.4
th_prob_F=0.3
th_prob_EF=0.2
th_prob_E_given_F=th_prob_EF/th_prob_F
sample_size=10000
sampleE=[0]*sample_size
sampleF=[0]*sample_size
countEF,countE,countF=0,0,0
for i in range(sample_size):
    a=np.random.choice([1,2,3,4],p=[0.2,0.2,0.1,0.5])
    if a==1:
        sampleE[i]=1
        sampleF[i]=1
    elif a==2:
        sampleE[i]=1
        sampleF[i]=0
    elif a==3:
        sampleE[i]=0
        sampleF[i]=1
for i in range(sample_size):
    if sampleE[i]==1 and sampleF[i]==1:
        countEF+=1
        countE+=1
        countF+=1
    elif sampleE[i]==1:
        countE+=1
    elif sampleF[i]==1:
        countF+=1
sim_prob_E_given_F=countEF/countF
print("Theoretical probability=%f, simulated probability=%f"%(th_prob_E_given_F,sim_prob_E_given_F))

cases=['i']

x = np.arange(len(cases))
plt.bar(x + 0.00, th_prob_E_given_F, color = 'red', width = 0.25, label = 'Theoretical')
plt.bar(x + 1, sim_prob_E_given_F, color = 'black', width = 0.25, label = 'Sim')
plt.xlabel('Cases')
plt.ylabel('Probabilities')

plt.legend()
plt.show()


