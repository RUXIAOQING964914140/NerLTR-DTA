#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import numpy as np
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from sklearn.metrics import mean_squared_error, r2_score
get_ipython().run_line_magic('matplotlib', 'inline')


# In[ ]:


#CI MSE
from lifelines.utils import concordance_index
b=pd.read_csv("Ensemble/tree/tree.csv")
df = pd.DataFrame(b)
m = df['Y']
n = df['P']

print(f'Concordance index: {concordance_index(m, n)}')
print(f"(MSE)：{mean_squared_error(m, n)}")


# In[ ]:


#Rm2
def r_squared_error(y_obs,y_pred):
    y_obs = np.array(y_obs)
    y_pred = np.array(y_pred)
    y_obs_mean = [np.mean(y_obs) for y in y_obs]
    y_pred_mean = [np.mean(y_pred) for y in y_pred]

    mult = sum((y_pred - y_pred_mean) * (y_obs - y_obs_mean))
    mult = mult * mult

    y_obs_sq = sum((y_obs - y_obs_mean)*(y_obs - y_obs_mean))
    y_pred_sq = sum((y_pred - y_pred_mean) * (y_pred - y_pred_mean) )

    return mult / float(y_obs_sq * y_pred_sq)
def squared_error_zero(y_obs,y_pred):
    k = get_k(y_obs,y_pred)

    y_obs = np.array(y_obs)
    y_pred = np.array(y_pred)
    y_obs_mean = [np.mean(y_obs) for y in y_obs]
    upp = sum((y_obs - (k*y_pred)) * (y_obs - (k* y_pred)))
    down= sum((y_obs - y_obs_mean)*(y_obs - y_obs_mean))

    return 1 - (upp / float(down))

def get_k(y_obs,y_pred):
    y_obs = np.array(y_obs)
    y_pred = np.array(y_pred)

    return sum(y_obs*y_pred) / float(sum(y_pred*y_pred))
def get_rm2(ys_orig,ys_line):
    r2 = r_squared_error(ys_orig, ys_line)
    r02 = squared_error_zero(ys_orig, ys_line)

    return r2 * (1 - np.sqrt(np.absolute((r2*r2)-(r02*r02))))

if __name__ == '__main__':
    df = pd.read_csv('T1_rank_L300_T500_shr003_mls5.csv')
    ys_orig = df['Y']
    ys_line = df['P']
    print(get_rm2(ys_orig, ys_line))


# In[ ]:


#del_query（sample_num =1,sample_affi are equal）
import linecache

file = open("qid_T1_T5.csv", "w")
lines = open('qid_T1_T5_2.csv').readlines()
lines = [line.rstrip('\n') for line in lines]
qid='0'
y_l=[]
all=[]
for line in lines:
	es=line.split(',')
	if es[0]==qid:
		if es[1] not in y_l:
			y_l.append(es[1])
		all.append(line)
	else:
		if len(y_l)>1:
			for l in all:
				file.write(l+'\n')
		all=[]
		all.append(line)
		qid=es[0]
		y_l=[]
		y_l.append(es[1])
if len(y_l)>1:
	for l in all:
		file.write(l+'\n')
file.close()
print('end')


# In[ ]:


#per-qid ci
data = pd.read_csv("qid_T1_T5.csv")

Y = data.groupby('qid')['Y'].apply(list)
P = data.groupby('qid')['P'].apply(list)


def get_cindex(Y, P,qid):
    # concordance_index(Y, P)

    print(f'{qid}, {concordance_index(Y, P)}')


for i, YP  in enumerate(zip(Y, P,Y.index)):
    get_cindex(YP[0], YP[1],YP[2])


# In[ ]:





# In[ ]:




