#!/usr/bin/env python
# coding: utf-8

# VARIABLES IN PYTHON

# In[6]:


a = r"'Rahul\n"
print(a)


# In[2]:


b = 345
# print(b)
# print(type(b))


# In[3]:


c = 45.32
d = True
# print(c)
# print(d)
# print(type(c))
# print(type(d))


# OPERATOR

# In[8]:


a = 3
b = 4

# Arithmetic Operators
# print("The value of 3+4 is ", 3+4)
# print("The value of 3-4 is ", 3-4)
# print("The value of 3*4 is ", 3*4)
print("The value of 3/4 is ", 3/4)


# In[5]:


# Assignment Operators
a = 34
a -= 12
print(a)
a *= 12
print(a)
a /= 12
print(a)


# In[6]:


# Comparison Operators
# b = (14<=7)
# b = (14>=7)
# b = (14<7)
# b = (14>7)
# b = (14==7)
b = (14!=7)
# print(b)


# In[7]:


# Logical Operators
bool1 = True
bool2 = False
# print("The value of bool1 and bool2 is", (bool1 and bool2))
# print("The value of bool1 or bool2 is", (bool1 or bool2))
# print("The value of not bool2 is", (not bool2))


# In[9]:


a = "35fgrfg34"
# a = int(a)
# print(type(a))
print(a + 5)


# In[11]:


a = input("Enter a number: ")
 # Convert a to an Integer(if possible)
print(type(a))


# String Slicing

# In[16]:


name = "Ayush"
print(name[4]) 
#print(name[1:4])
#print(name[:4]) # is same as name[0:4]
# print(name[1:]) # is same as name[1:5]
c = name[-4:-1] # is same is name[1:4]
print(c)

# name = "AyushIsGood"
# d = name[0::3]
# d = name[:0:-1]
# print(d)


# In[17]:


story = "once upon a time there was a man who loved reading"

# String Functions
print(len(story))
print(story.endswith("reading"))
print(story.count("c"))
print(story.capitalize())
print(story.find("upon"))
print(story.replace("man","Women"))


# In[ ]:


story = "Tushar is good.\nHe\tis ve\\ry good"
# print(story)


# DataTypes in Python

# In[18]:


a = [1, 2 , 4, 56, 6]

# Print the list using print() function
# print(a)

# Access using index using a[0], a[1], a[2]
# print(a[2])

# Change the value of list using
a[0] = 98
print(a)

# We can create a list with items of different types
c = [45, "Sam", False, 6.9]
# print(c)


# In[20]:


friends = ["Harry", "Tom", "Rohan", "Sam", "Divya", 45]
print(friends[0:5])
print(friends[-4:])


# In[ ]:


l1 = [1, 8, 7, 2, 21, 15]
# print(l1)
# l1.sort() # sorts the list
# l1.reverse() # reverses the list
#l1.append(45) # adds 45 at the end of the list 
# l1.insert(2, 544) # inserts 544 at index 2
# l1.pop(2) # removes element at index 2
l1.remove(21) # removes 21 from the list
# print(l1)


# In[21]:


# Creating a tuple using ()
t = (1, 2, 4, 5)

# t1 = () # Empty tuple
# t1 = (1) # Wrong way to declare a Tuple with Single element
t1 = (1,) # Tuple with Single element
# print(t1)
t[1]=3


# In[23]:


myDict = {
    "Fast": "In a Quick Manner",
    "Sam": "A Coder",
    "Marks": [1, 2, 5],
    "anotherdict": {'Sam': 'Player'}
}

print(myDict['Fast'])
# print(myDict['Harry'])
myDict['Marks'] = [45, 78]
# print(myDict['Marks'])
print(myDict["anotherdict"]["Sam"])


# In[ ]:


a = {1}
# print(type(a))


# In[ ]:


a = input("Enter a number")

# 1. if-elif-else ladder in Python
# if(a<3): 
#     print("The value of a is greater than 3")
# elif(a>13):
#     print("The value of a is greater than 13")
# elif(a>7):
#     print("The value of a is greater than 7")
# elif(a>17):
#     print("The value of a is greater than 17")
# else:
#     print("The value is not greater than 3 or 7")

# 2. Multiple if statements
if(a<3): 
    print("The value of a is greater than 3")

if(a>13):
    print("The value of a is greater than 13")
    
if(a>7):
    print("The value of a is greater than 7")

if(a>17):
    print("The value of a is greater than 17")
else:
    print("The value is not greater than 3 or 7")

print("Done")


# In[ ]:


a = [45, 56, 6]
# print(435 in a)


# In[26]:


marks =input("Enter Your Marks\n")

if marks>=90:
	grade = "Ex"
elif marks>=80:
    grade = "A"
elif marks>=70:
    grade = "B"
elif marks>=60:
    grade = "C"
elif marks>=50:
    grade = "D" 
else:
    grade = "F"

print("Your grade is " + grade)


# In[ ]:




