#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import linecache
import numpy as np
import pandas as pd


# In[ ]:


#Get the index of the data that satisfies the constraint
lines1 = linecache.getlines("quantile/drug_eachrow_avg_sim.txt")#AA
lines1 = [line1.rstrip('\n').strip() for line1 in lines1]
num = 0
with open('kiba_drug_sim.txt','r') as f, open('index/drug_eachrow_avg_sim_index.txt','w') as f1, open('index/drug_eachrow_avg_sim_num.txt','w') as f2:
    lines = f.readlines()
   
    for i in lines:
        j = i.split(" ")
        counter = 0
        for i,p in enumerate(j):
            m = float(p)
            if m> float(lines1[num]):
                counter += 1 
                f1.write(str(i)+' ')
                #q = i
        f1.write('\n')
        f2.write(str(counter)+' ')
        f2.write('\n')
        num = num+1


# In[ ]:


#Index of the 5 most similar data
#step1
data = np.loadtxt('kiba_drug_sim.txt')
sim_index_rank = np.argsort(-data)
#sim_index_rank
#np.savetxt("low_sim_drug\drug_sim_index_rank.txt", sim_index_rank,fmt='%d',delimiter=' ')
q = pd.DataFrame(sim_index_rank)
d = q[[0,1, 2,3,4,5]]
f = q[[0,1]]
np.savetxt("index/drug_sim_rank_F5_index_pre.txt", d,fmt='%d',delimiter=' ')
#np.savetxt("index/drug_sim_rank_F1_index.txt", f,fmt='%d',delimiter=' ')


# In[ ]:


#step2
lines1 = linecache.getlines("index/A_Row_index.txt")#AA
lines1 = [line1.rstrip('\n').strip() for line1 in lines1]
num = 0
with open('index/drug_sim_rank_F5_index_pre.txt','r') as f, open('index/drug_sim_rank_F5_index.txt','w') as f1:
    lines = f.readlines()
   
    for i in lines:
        j = i.split(" ")
        counter = 0
        for i,p in enumerate(j):
            #m = float(p)
            if p == lines1[num]:
                counter += 1 
                #f1.write(str(i)+' ')
                #q = i
            
            else:
                #print(p)
                f1.write(p+' ')
        #f1.write('\n')
        #f2.write(str(counter)+' ')
        #f2.write('\n')
        num = num+1

