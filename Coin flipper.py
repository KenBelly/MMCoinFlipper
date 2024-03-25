#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random

results = []
for i in range(1, 68):
    flip = random.choice(['Heads','Tails'])
    results.append(flip)
    print(f"Flip {i}: {flip}")

print(f"\nTotal results: {results.count('Heads')} Heads, {results.count('Tails')} Tails")


# In[ ]:




