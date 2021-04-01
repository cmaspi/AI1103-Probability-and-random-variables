import random
import matplotlib.pyplot as plt
sample_size=10000
sampleS=[0]*sample_size
s_n=0
Y=0
for i in range(sample_size):
    sampleS[i]=random.random()
    s_n+=sampleS[i]
print("Theoretical mean= 0.5, simulated mean=%f"%(s_n/sample_size))
x=[1+i for i in range(100)]
y=[sampleS[i] for i in range(100)]
for i in range(100):
    Y+=y[i]
Y/=100
plt.scatter(x,y)
plt.plot([0,100],[Y,Y],"r")
plt.xlim(0,101)
plt.show()