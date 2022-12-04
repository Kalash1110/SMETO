#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random
#number of task nodes
TN=2
#number of helper nodes
HN=5
p=[]
for i in range(TN):
    for j in range(HN):
        num=random.randint(120,220)
        p.append(num)


# In[2]:


import numpy as np
arr=np.array(p)
arr.shape=(TN,HN)
#print(arr)
p=arr.tolist()


# In[3]:


print(p)


# In[4]:


import math
SE = [[0]*TN]*HN
SE_NEW=[]
B=200
N=150
#print(SE)
for l in range(HN):
    for i in range(TN):
        P=min((p[i][l]),200)
        SE[l][i]=B*(math.log2(1+(P/(B*N))))
        value=SE[l][i]
        #print(SE[l][i])
        SE_NEW.append(value)


# In[5]:


print(SE_NEW)


# In[6]:


import numpy as np
SE_UP=np.array(SE_NEW)
#print(SE_UP)
SE_UP.shape=(HN,TN)
print(SE_UP)


# In[7]:


SE_UP = SE_UP.tolist()


# In[8]:


PL_HN=[]
for i in range(HN):
    #print(SE_UP[i])
    PLHN=SE_UP[i].index(max(SE_UP[i]))
    #print(PLHN)
    PL_HN.append(PLHN)


# In[9]:


print(PL_HN)


# In[10]:


C=[]
for k in range(HN):
    num4=random.randint(100,250)
    C.append(num4)
print(p[0])
print(C)
e= []
for j in range(TN):
    for i in range(HN):
        temp5=((1/C[i])+(1/SE_UP[i][j]))
        R=1/temp5
        temp6=((150/C[i])+(p[j][i]/SE_UP[i][j]))
        Q=(temp6/temp5)
        new=(R/Q)*100
        if new>1:
            new=new-1
        print(new)
        e.append(new)
arr=np.array(e)
arr.shape=(TN,HN)
eta=arr.tolist()      


# In[11]:


print(eta)


# In[12]:


EE=[[0]*TN]*HN
for i in range(TN):
    lst=eta[i]
    EE[i]= {i: lst[i] for i in range(0, len(lst))}
    print(EE[i])


# In[13]:


PL_t0= []
PL_T0=[]
PL_EE=[]
for i in range(TN):
    PL_t0= sorted(EE[i].items(), key=lambda x:x[1], reverse=True)
    PL_t0= dict(PL_t0)
    print(PL_t0)
    PL_T0=list(PL_t0.keys())
    print(PL_T0)
    PL_EE.append(PL_T0)
    


# In[14]:


print(PL_EE)


# In[15]:


j=0
assigned=0
for i in range(HN):
    if assigned<2:
        val=PL_EE[0][i]
        if (PL_HN[int(val)] == 0):
            assigned+=1
            print('Helper Node ' +str(val)+ " assigned to task node 0")
j=1
assigned=0
for i in range(HN):
    if assigned<2:
        val=PL_EE[j][i]
        if (PL_HN[int(val)] == 1):
            assigned+=1
            print('Helper Node ' +str(val)+ " assigned to task node 1")  


# In[16]:


import matplotlib.pyplot as plt
plt.plot(SE_UP[0],label='SERVICE EFFICIENCY - T0')
plt.plot(SE_UP[1],label='SERVICE EFFICIENCY- T1')
#plt.plot(eta,label='test')
plt.legend()
plt.show()


# In[17]:


import matplotlib.pyplot as plt
plt.plot(eta[0],label='ENERGY EFFICIENCY - TN0')
plt.plot(eta[1],label='ENERGY EFFICIENCY - TN1')
plt.legend()
plt.show()

