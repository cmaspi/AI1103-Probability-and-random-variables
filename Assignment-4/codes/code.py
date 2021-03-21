import matplotlib.pyplot as plt
from scipy.stats import bernoulli
import numpy as np

th_prob=0.09

sample_size=10000


throw=[[0 for i in range(sample_size)] for j in range(2)]
for i in range(2):
    temp=bernoulli.rvs(size=sample_size,p=0.1)
    for j in range(sample_size):
        throw[i][j]=temp[j]

count=0
for i in range(sample_size):
    if throw[0][i]==0 and throw[1][i]==1:
        count+=1
sim_prob=count/sample_size
print("Probability from simulation =",sim_prob," Probability from theory =", th_prob)

cases=['i']

x = np.arange(len(cases))
plt.bar(x + 0.00, th_prob, color = 'green', width = 0.25, label = 'Theoretical')
plt.bar(x + 1, sim_prob, color = 'violet', width = 0.25, label = 'Sim')
plt.xlabel('Cases')
plt.ylabel('Probabilities')

plt.legend()
plt.show()


