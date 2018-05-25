
# coding: utf-8

# In[43]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from statsmodels.stats.outliers_influence import summary_table

import numpy as np
import statsmodels.api as sm

from sklearn.linear_model import LinearRegression
import scipy, scipy.stats


# We read the data file and store it as a 'dataframe', which is kind of a spreadsheet with different types of variables

# In[44]:


df_FS5 = pd.read_csv('FS5_SUVR.csv')
df_FS6 = pd.read_csv('FS_SUVR.csv')


# In[45]:


# To print the first 5 rows and have an overview of the info:
df_FS5.head()


# In[46]:


# To print the first 5 rows and have an overview of the info:
df_FS6.head()


# In[47]:


# To print the number of rows and cols: 
df_FS5.shape


# In[48]:


# To print the number of rows and cols: 
df_FS6.shape


# In[49]:


get_ipython().run_line_magic('matplotlib', 'inline')

fig, ax = plt.subplots()
ax.scatter(df_FS5['SUVRmean'], df_FS6['SUVRmean'])
ax.set_xlabel("SUVRmean_FS5")
ax.set_ylabel("SUVRmean_FS6")
#plt.ylim((1.5,1.6))

for i, txt in enumerate(df_FS5['regionname']):
     print(i,txt)
     ax.annotate(i,(df_FS5['SUVRmean'][i], df_FS6['SUVRmean'][i]))
        
plt.savefig('Figs/S_HBCFYC_2017-04-21_FS5vsFS6_labels.pdf', format='pdf')
plt.show()


# In[50]:


X = df_FS5['SUVRmean']
Y = df_FS6['SUVRmean']

results = sm.OLS(Y,sm.add_constant(X)).fit()

print(results.summary())

R2 = results.rsquared
st, data, ss2 = summary_table(results, alpha=0.05)

fittedvalues = data[:,2]

plt.plot(X, fittedvalues, 'b-', lw=1, label ='R2= %f'%R2)
plt.scatter(X,Y)
plt.xlabel('SUVRmean_FS5')
plt.ylabel('SUVRmean_FS6')
plt.title('S_HBCFYC_2017-04-21')
plt.legend()

for i, txt in enumerate(df_FS5['regionname']):
     #print(i,txt)
     ax.annotate(txt,(df_FS5['SUVRmean'][i], df_FS6['SUVRmean'][i]))

plt.savefig('Figs/S_HBCFYC_2017-04-21_FS5vsFS6.pdf', format='pdf')
plt.show()

