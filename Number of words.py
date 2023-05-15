#!/usr/bin/env python
# coding: utf-8

# In[1]:


def words():
        # Defining the variable 
        s = input("Enter a paragraph ")
        # Defining the second variable for string
        word_list = s.strip().split()
        return len(word_list)
while True:
    num_words = words()
    print("Number of words is", num_words)
words()


# In[3]:


def practice():
    a = input("Enter a string!")
    b = a.split()
    print(b)
practice()    


# In[ ]:




