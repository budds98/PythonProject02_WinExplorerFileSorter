#!/usr/bin/env python
# coding: utf-8

# Automatic File Sorter in File Explorer

# In[28]:


import os, shutil


# In[29]:


path = r"C:/Users/budim/Downloads/Documents/Python/"


# In[30]:


file_name = os.listdir(path)


# In[31]:


os.listdir(path)


# In[32]:


folder_name = ['csv files', 'image files', 'ris files']
for loop in range(0,3):
    if not os.path.exists(path + folder_name[loop]):
        #print(path + folder_name[loop])
        os.makedirs((path + folder_name[loop]))
    


# In[33]:


for file in file_name:
    if ".csv" in file and not os.path.exists(path + "csv files/" + file):
        shutil.move(path + file, path + "csv files/" + file)
    elif ".jpg" in file and not os.path.exists(path + "image files/" + file):
        shutil.move(path + file, path + "image files/" + file)
    elif ".JPG" in file and not os.path.exists(path + "image files/" + file):
        shutil.move(path + file, path + "image files/" + file)
    elif ".ris" in file and not os.path.exists(path + "ris files/" + file):
        shutil.move(path + file, path + "ris files/" + file)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




