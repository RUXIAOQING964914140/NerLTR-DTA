#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import pandas as pd
import linecache


# In[ ]:


#threshold /SSAF
a = np.loadtxt("kiba_drug_sim.txt")
each_row_1 = np.mean(a,axis=1)
each_row_median = np.median(a, axis=1)
each_row_quantile_75 = np.percentile(a, 75, axis=1)
each_row_quantile_85 = np.percentile(a, 85, axis=1)
each_row_quantile_95 = np.percentile(a, 95, axis=1)
np.savetxt("quantile\drug_eachrow_avg_sim.txt", each_row_1,fmt='%.3f',delimiter=' ')
np.savetxt("quantile\drug_eachrow_median.txt", each_row_median,fmt='%.3f',delimiter=' ')
np.savetxt("quantile\protein_eachrow_quantile_75.txt", each_row_quantile_75,fmt='%.4f',delimiter=' ')
np.savetxt("quantile\drug_eachrow_quantile_85.txt", each_row_quantile_85,fmt='%.3f',delimiter=' ')
np.savetxt("quantile\drug_eachrow_quantile_95.txt", each_row_quantile_95,fmt='%.3f',delimiter=' ')


# In[ ]:





# In[ ]:


#ASAF-mean
with open('kiba_binding_affinity.txt','r') as f, open('quantile/Affi_DT_avg.txt','w') as f1, open('quantile/Affi_DT_fre.txt','w') as f2:
    lines = f.readlines()
    for i in lines:
        j = i.split(" ")
        counter = 0
        avg = 0
        for i,p in enumerate(j):
            m = float(p)
            #print(m)
            if m > -1.0:                
                counter += 1 
                avg += m
                #f1.write(str(i)+' ')
                #q = i
        f1.write(str(avg/229)+' ')
        f1.write('\n')
        f2.write(str(avg/counter)+' ')
        f2.write('\n')


# In[ ]:


#ASAF-num
with open('kiba_binding_affinity.txt','r') as f, open('quantile/Affi_DT_index.txt','w') as f1, open('quantile/Affi_DT_num.txt','w') as f2:
    lines = f.readlines()
    for i in lines:
        j = i.split(" ")
        counter = 0
        
        for i,p in enumerate(j):
            m = float(p)
            #print(m)
            if m > -1.0:                
                counter += 1 
                f1.write(str(i)+' ')
                #q = i
        f1.write('\n')
        f2.write(str(counter)+' ')
        f2.write('\n')


# In[ ]:


#ASAF-quantiles
#step1
with open('kiba_binding_affinity.txt','r') as f, open('quantile/1/Affi_DT_values.txt','w') as f1:
    lines = f.readlines()
    for i in lines:
        j = i.split(" ")
        for i,p in enumerate(j):
            m = float(p)
            #print(m)
            if m > -1.0:                
                f1.write(str(m)+' ')
        f1.write('\n')


# In[ ]:


#step2
lines1 = linecache.getlines("quantile/1/Affi_DT_values.txt")#AA
lines1 = [line1.rstrip('\n').strip() for line1 in lines1]

def calculate_percentile(arry, percentile):
    size = len(arry)
    return sorted(arry)[int(math.ceil((size * percentile) / 100)) - 1]

mm = open('quantile/Affi_DT_values_percent25.txt',mode = 'w+', encoding='utf-8') 
mm1 = open('quantile/Affi_DT_values_percent50.txt',mode = 'w+', encoding='utf-8') 
mm2 = open('quantile/Affi_DT_values_percent75.txt',mode = 'w+', encoding='utf-8') 
for i in lines1:
    #i=i.replace('\n','')
    
    a = i.split(" ")
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


#ASAF-mode
#step1
lines1 = linecache.getlines("quantile/1/Affi_DT_values.txt")#AA
lines1 = [line1.rstrip('\n').strip() for line1 in lines1]

mm = open('quantile/1/Affi_DT_values_mode.txt',mode = 'w+', encoding='utf-8')
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


#step2
lines1 = linecache.getlines("quantile/1/Affi_DT_values_mode.txt")#AA
lines1 = [line1.rstrip('\n').strip() for line1 in lines1]
mm = open('quantile/Affi_DT_values_mode_avg.txt',mode = 'w+', encoding='utf-8') 
for i in lines1:
    #i=i.replace('\n','')
    
    a = i.split(" ")
    a_float = [ ]
    for num in a:
        a_float.append(float(num))
    #print(a_float)
    li = a_float
    c = np.mean(li)
    print(c)
    mm.write(str(c)+' ')
    mm.write('\n')
mm.close()


# In[ ]:





# In[ ]:


#ASAF-higher/lower values
data = np.loadtxt('kiba_binding_affinity.txt')
sim_index_rank = np.argsort(-data)
#sim_index_rank
#np.savetxt("low_sim_drug\drug_sim_index_rank.txt", sim_index_rank,fmt='%d',delimiter=' ')
low_sort = -np.sort(-data)
q = pd.DataFrame(sim_index_rank)
p = pd.DataFrame(low_sort)
d = q[[0,1, 2,3,4]]
f = q[[0]]
g = p[[0,1, 2,3,4]]
h = p[[0]]
np.savetxt("index/Affis_DT_rank_F5_index.txt", d,fmt='%d',delimiter=' ')
np.savetxt("index/Affis_DT_rank_F1_index.txt", f,fmt='%d',delimiter=' ')
g.to_csv("quantile/Affis_DT_rank_F5_value.txt",sep=' ',header = 0,index=0)
h.to_csv("quantile/Affis_DT_rank_F1_value.txt",sep=' ',header = 0,index=0)


# In[ ]:


#ASAF-num
with open('Trans_kiba_binding_affinity.txt','r') as f, open('index/Trans_Affi_DT_index.txt','w') as f1, open('quantile/Trans_Affi_DT_num.txt','w') as f2:
    lines = f.readlines()
    for i in lines:
        j = i.split(" ")
        counter = 0

        for i,p in enumerate(j):
            m = float(p)
            #print(m)
            if m > -1.0:                
                counter += 1 
                f1.write(str(i)+' ')
                #q = i
        f1.write('\n')
        f2.write(str(counter)+' ')
        f2.write('\n')

        #print(counter)

