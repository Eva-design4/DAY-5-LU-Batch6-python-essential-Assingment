#!/usr/bin/env python
# coding: utf-8

# # Assingment 1
# Sort increasing order but all zeros should be at the right had side.
# [0,1,2,10,4,1,0,56.2,0,1,3,0,56,0,4]

# In[11]:


list = [0,1,2,10,4,1,0,56.2,0,1,3,0,56,0,4]
list.sort()
n = list.count(0);
print(list[n:]+list[:n])


# # Merge two sorted list to produce one sorted list but use only one loop while or for only one time
# 
# list1 =[10,20,40,60,70,80]
# 
# List2 = [5,15,25,35,45,60] 

# In[1]:


list1 = [10,20,40,60,70,80]
list2 = [5,15,25,35,45,60]
num = list1 + list2
for each in range(5,81):
    for each in num:
        break
else:
        print (num)


# In[ ]:




