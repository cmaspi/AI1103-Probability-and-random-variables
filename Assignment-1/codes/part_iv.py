import random

sample_size=1000
n=int(100*random.random())
# n represents the number of elementary events
#for each run, we'll have one outcome from the elementary events.
arr=[[0 for i in range(sample_size)] for j in range(n)] #this is our test case matrix.
prob_arr=[0]*n
count_arr=[0]*n
for i in range(sample_size):
    j=int(n*random.random())
    arr[j][i]=1
    
    
  
for i in range(sample_size):
    for j in range(n):
        if arr[j][i]==1:
            count_arr[j]+=1
            
total_prob=0
for j in range(n):
   prob_arr[j]=count_arr[j]/sample_size
   total_prob+=prob_arr[j]
   print("The probability of %dth event is %f"%(j,prob_arr[j]))   
print("The total probability is %f"%total_prob)     

