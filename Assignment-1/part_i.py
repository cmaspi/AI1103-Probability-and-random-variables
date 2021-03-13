import numpy as np
from scipy.stats import bernoulli
import random
sample_size = 10000
E,notE=0,0
prob_E=random.random()
sample = bernoulli.rvs(size = sample_size, p = prob_E)
#considering success (1) for the occurence of event E, so failure (0) is not E.
for i in range(sample_size):
    if sample[i]==1:
        E+=1
    elif sample[i]==0:  
        notE+=1
p_E=E/sample_size
p_notE=notE/sample_size

print("The probability assigned to event E was %f"%prob_E)
print("The probability of event E as calculated using array is %f, while that of not E is %f"%(p_E,p_notE))
print("probability of E + probability of not E=%f"%(p_E+p_notE))

