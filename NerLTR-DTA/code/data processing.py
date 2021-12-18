#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import linecache
import pandas as pd
import numpy as np


# In[ ]:


#addrank
input_file = "all_feature/nor/combine_fea/all_F_R_fea.txt"
output_file = "all_feature/nor/combine_fea/R_all_F_R_fea.txt"
fout = open(output_file, "w")
with open(input_file) as fin:
    for line in fin:
        if ':' in line:
            fout.write(line)
        else:
            n = 0
            for i in line.split():
                if n != 0:
                    fout.write(' ')
                n += 1
                fout.write(str(n)+':' + i )
            fout.write('\n')
fout.close()


# In[ ]:


#Extract the data set
fm = open ("folds/train_del_1_sort.txt")#Flatten data
m = fm.readlines()
m = list(map(int,m))

fb = open ("all_feature/nor/combine_fea/Qid_all_F_R_fea_del.txt")#all sample
b = fb.readlines()
fc = open("Process1/train1_all_F_R_fea.txt","w")#train/test set
for i in m:
    fc.write(b[i])
fc.close()


# In[ ]:


#Trans
a = np.loadtxt('kiba_binding_affinity.txt')
np.shape(a)
a_trans = a.transpose()
np.shape(a_trans)
b = a_trans
#np.savetxt("protein\kiba_Trans_affi.txt",b,fmt='%.3f') #bb文件名
r = pd.DataFrame(b)
r.to_csv("Trans_kiba_binding_affinity.txt",sep=' ',header = 0,index=0)


# sharing-sharing matrix
data = np.loadtxt('davis_binding_affinity.txt')
def func1(x,y):
#    print(type(x),y)
    sum = 0
    for i in range(x.shape[0]):
        if x[i] == 5.0 or y[i] == 5.0:
            sum += 0
        else:
            sum+=1
    return  sum

mm = open('Share/1/Affi_drug_shareTarget_num.txt',mode = 'w+', encoding='utf-8')
for i in range(data.shape[0]):
    for j in range(data.shape[0]):
        #print(str(func1(data[i,:] ,data[j,:])),end=' ')
        mm.write(str(func1(data[i,:] ,data[j,:]))+' ')
    #print()
    mm.write('\n')

mm.close()
