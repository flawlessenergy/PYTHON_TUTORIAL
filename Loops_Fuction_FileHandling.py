#!/usr/bin/env python
# coding: utf-8

# WHILE LOOP

# In[ ]:


i = 0
while i<10:
    print("Yes " + str(i))
    i = i + 1

print("Done")


# In[ ]:


i = 1

while i<=50:
    print(i)
    i = i + 1


# In[1]:


fruits = ['Banana', 'Watermelon', 'Grapes', 'Mangoes']
i = 0
print(len(fruits))
while i<len(fruits):
    print(fruits[i])
    i = i+1


# FOR LOOP

# In[2]:


fruits = ['Banana', 'Watermelon', 'Grapes', 'Mangoes']

for item in fruits:
    print(item)
   


# In[ ]:


for i in range(1, 8, 1):
    print(i)


# In[ ]:


for i in range(10):
    print(i)
else:
    print("This is inside else of for")


# In[5]:


for i in range(10):
    print(i)
    if i == 5:
        pass
else:
    print("This is inside else of for")
#When the pass statement is executed, nothing happens, but you avoid getting an error when empty code is not allowed.


# In[3]:


for i in range(10):
    if i == 5:
        continue
    print(i)


# In[1]:


for i in range(10):
    print(i)
    if i == 5:
        break
else:
    print("This is inside else of for")


# In[7]:


num = int(input("Enter the number"))
for i in range(1, 12):
    # print(str(num) + " X " + str(i) + "=" + str(i*num))
    print(f"{num}X{i}={num*i}")


# In[ ]:


l1 = ["Sam", "Sohan", "Sachin", "Rahul"]

for name in l1:
    if name.startswith("S"):
        print("Hello " + name)


# In[ ]:


num = int(input("Enter the number: "))
prime = True

for i in range(2, num):
    if(num%i == 0):
        prime = False
        break
if prime:
    print("This number is Prime")
else:
    print("This number is not Prime")


# FUNCTIONS IN PYTHON

# In[ ]:


def percent(marks):
    p = ((marks[0] + marks[1] + marks[2]+ marks[3])/400 )*100
    return p

marks1 = [45, 78, 86, 77]
percentage1 = percent(marks1)

marks2 = [75, 98, 88, 78]
percentage2 = percent(marks2)
print(percentage1, percentage2)


# In[ ]:


def greet(name):
    print("Good Day, "+ name)

def mySum(num1, num2):
    return num1 + num2

greet("Tushar")
s = mySum(6, 32)
print(s)


# In[ ]:


def maximum(num1, num2, num3):
    if (num1>num2):
        if(num1>num3):
            return num1
        else:
            return num3
    else:
        if(num2>num3):
            return num2
        else:
            return num3

m = maximum(13, 55, 2)
print("The value of the maximum is " + str(m))


# In[ ]:


def remove_and_split(string, word):
    newStr = string.replace(word, "")
    return newStr.strip()

this = "     Tushar is a good      "
n = remove_and_split(this, "Tushar")


# In[ ]:


f = open('sample.txt') # by default the mode is r
# data = f.read()
data = f.read(5) # reads first 5 characters from the file
print(data)
f.close()


# In[ ]:


with open('another.txt', 'r') as f:
    a = f.read()
with open('another.txt', 'w') as f:
    a = f.write("me")
print(a)


# In[ ]:


for i in range(2, 21):
    with open(f"tables/Multiplication_table_of_{i}.txt", 'w') as f:
        for j in range(1, 11):
            f.write(f"{i}X{j}={i*j}")
            if j!=10:
                f.write('\n')


# In[ ]:




