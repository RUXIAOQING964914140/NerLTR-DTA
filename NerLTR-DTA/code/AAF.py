#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import pandas as pd
import linecache
import math


# In[ ]:


#AAF
#step1
lines = linecache.getlines("quantile/Affi_DT_num.txt")#ASAF data file
lines = [line.rstrip('\n') for line in lines]

lines1 = linecache.getlines("index/drug_eachrow_avg_sim_index_del.txt")#index_available file
lines1 = [line1.rstrip('\n').strip() for line1 in lines1]
file = open("features/drug_fea/avg_DT_num.txt",'w')
for idx, line in enumerate(lines1):
    line = line.split(' ')
    for i in line:
        
        #print(lines[int(i)], end=" ")
    #print()
        file.write(lines[int(i)]+" ")
    file.write('\n')
file.close()


# In[ ]:


#step2
lines1 = linecache.getlines("avg_DT_num.txt")#AA
lines1 = [line1.rstrip('\n').strip() for line1 in lines1]

def calculate_percentile(arry, percentile):
    size = len(arry)
    return sorted(arry)[int(math.ceil((size * percentile) / 100)) - 1]

mm = open('f/avg_DT_num_percent25.txt',mode = 'w+', encoding='utf-8') 
mm1 = open('f/avg_DT_num_percent50.txt',mode = 'w+', encoding='utf-8') 
mm2 = open('f/avg_DT_num_percent75.txt',mode = 'w+', encoding='utf-8') 
for i in lines1:
    #i=i.replace('\n','')
    
    a = i.split(" ")
    #print(a)
    #a=a[0:-1]
    a_float = [ ]
    for num in a:
        a_float.append(float(num))
    #print(a_float)
    percentile_25 = calculate_percentile(a_float, 25)
    percentile_50 = calculate_percentile(a_float, 50)
    percentile_75 = calculate_percentile(a_float, 75)
    mm.write(str(percentile_25)+' ')
    mm.write('\n')
    mm1.write(str(percentile_50)+' ')
    mm1.write('\n')
    mm2.write(str(percentile_75)+' ')
    mm2.write('\n')
    #print(percentile_25)
    #print(percentile_50)
   #print(percentile_75)
mm.close()
mm1.close()
mm2.close()


# In[ ]:


lines1 = linecache.getlines("avg_DT_num.txt")#AA
lines1 = [line1.rstrip('\n').strip() for line1 in lines1]

mm = open('f/avg_DT_num_mode.txt',mode = 'w+', encoding='utf-8')
for i in lines1:
    #i=i.replace('\n','')
    
    a = i.split(" ")
    a_float = [ ]
    for num in a:
        a_float.append(float(num))
    #print(a_float)

    li = a_float
    #print(li)
    d = {}
    for i in li:
        ss = d.get(i)
        if ss == None:
            d[i] = 1
        else:
            d[i]+=1
    for i in d.items():
        if i[1] == max(d.values()):
            #print("众数:",i[0])
            
    #print(" ")
            mm.write(str(i[0])+' ')
    mm.write('\n')
mm.close()


# In[ ]:


lines1 = linecache.getlines("avg_DT_num.txt")#AA
lines1 = [line1.rstrip('\n').strip() for line1 in lines1]
mm = open('f/avg_DT_num_mean.txt',mode = 'w+', encoding='utf-8') 
mm1 = open('f/avg_DT_num_min.txt',mode = 'w+', encoding='utf-8')
mm2 = open('f/avg_DT_num_max.txt',mode = 'w+', encoding='utf-8')
for i in lines1:
    #i=i.replace('\n','')
    
    a = i.split(" ")
    a_float = [ ]
    for num in a:
        a_float.append(float(num))
    #print(a_float)
    li = a_float
    c = np.mean(li)#均值
    x = np.amin(li)
    d = np.amax(li)

    mm.write(str(c)+' ')
    mm.write('\n')
    mm1.write(str(x)+' ')
    mm1.write('\n')
    mm2.write(str(d)+' ')
    mm2.write('\n')
mm.close()
mm1.close()
mm2.close()

