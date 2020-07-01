#!/usr/bin/env python
# coding: utf-8

# In[5]:


# 1. Dictionary is a mutable data type in Python. A python dictionary is a collection of key and value pairs separated by a colon (:)
mydict = {'StuName': 'vijji', 'StuAge': '18', 'StuCity': 'kurnool'}
print("Student Age is:", mydict['StuAge'])
print("Student City is:", mydict['StuCity'])


# In[12]:


# 2. to sum all the items in a list
def sum_list(items):
    sum_numbers = 0
    for x in items:
        sum_numbers += x
    return sum_numbers
print(sum_list([4,-20,3]))


# In[14]:


# 3. create a list of empty dictionaries
n =4
l = [{} for _ in range(n)]
print(l)


# In[15]:


# 4. Access dictionary keys element by index
num = {'physics': 80, 'math': 90, 'chemistry': 86}
print(list(num)[2])


# In[17]:


# 5. python program to iterate over dictionaries using for loops
d = {'blue': 4, 'Green': 2, 'Blue': 3} 
for color_key, value in d.items():
     print(color_key, 'corresponds to ', d[color_key]) 


# In[19]:


# 6. python program to sum all the items in a dictionary
my_dict = {'num1':10,'num2':-54,'num3':50}
print(sum(my_dict.values()))


# In[20]:


# 7. concatenate dictionaries to create a new one 
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
dic4 = {}
for d in (dic1, dic2, dic3): dic4.update(d)
print(dic4)


# In[21]:


# 8. Expected result:{1:10,2:20,3:30,4:40,5:50,6:60}
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
dic4 = {}
for d in (dic1, dic2, dic3): dic4.update(d)
print(dic4)


# In[23]:


# 9. Create a tuple 
x = ()
print(x)


# In[24]:


# 10. Create a tuple with different data types
tuplex = ("tuple", True, 4.2, 1)
print(tuplex)


# In[25]:


# 11.covert a tuple to string 
tup = ('v','i','j','j','i')
str =  ''.join(tup)
print(str)


# In[27]:


# 12. to slice a tuple
tuplex = ('v','i','j','j','i')
_slice = tuplex[2:]
print(_slice)


# In[29]:


# 13. length of a tuple
tuplex = tuple("python")
print(tuplex)
print(len(tuplex))


# In[30]:


# 14. convert a tuple to dictionary
tuplex = ((1, "v"),(4, "i"))
print(dict((y, x) for x, y in tuplex))


# In[31]:


# 15. to reverse a tuple
x = (5, 10, 15, 20)
y = reversed(x)
print(tuple(y))


# In[32]:


# 16. convert a list of tuples in to a dictionary
l = [("v", 1), ("i", 2), ("j", 3), ("j", 4), ("i", 5)]
d = {}
for a, b in l:
    d.setdefault(a, []).append(b)
print (d)


# In[33]:


# 17.Convert list to tuple
listx = [5, 10, 7, 4, 15, 3]
tuplex = tuple(listx)
print(tuplex)


# In[ ]:




