#!/usr/bin/env python
# coding: utf-8

# In[39]:


import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings('ignore')
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns


# In[40]:


marketing_costumer = pd.read_csv(r"C:\Users\Utilizador\Desktop\Labround4\lab-customer-analysis-round-4\files_for_lab\csv_files\marketing_customer_analysis.csv")
marketing_costumer


# In[41]:


cols = []
for i in range(len(marketing_costumer.columns)):
    cols.append(marketing_costumer.columns[i].lower().replace(' ', '_'))
marketing_costumer.columns = cols
marketing_costumer


# In[64]:


numerical = marketing_costumer.select_dtypes(include=[np.number])
numerical


# In[65]:


categorical = marketing_costumer.select_dtypes(include=[object])
categorical


# In[66]:


sns.displot(numerical)
plt.show()


# In[67]:


sns.histplot(numerical)
plt.show()


# In[68]:


correlations_matrix = numerical.corr()
correlations_matrix


# In[69]:


sns.heatmap(correlations_matrix, annot=True)
plt.show()
mask = np.zeros_like(correlations_matrix)
mask[np.triu_indices_from(mask)] = True
fig, ax = plt.subplots(figsize=(10, 8))
ax = sns.heatmap(correlations_matrix, mask=mask, annot=True)
plt.show()


# In[ ]:




