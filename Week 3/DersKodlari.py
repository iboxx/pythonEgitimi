#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def fonk(a,):
    print (x*x)

for i in range(11):
    f(i)


# In[ ]:


def fonk(a,b):
    print(a+b)
    print(a-b)
    print(a*b)
    

fonk(5,3),
print()
fonk(2,9)


# In[ ]:


def fonk(a,b):
    print((a + b)/2)
fonk(3,5)
    


# In[ ]:


cumle = input("Lütfen cümle giriniz: ")


def funct(karakter):
    toplam = 0
    for c in cumle:
        if c == karakter:
            toplam += 1
    print("Cümledeki " + str(karakter) + " harfi sayısı = " + str(toplam))
    
    
funct('a')
funct('b')
funct('c')
funct('o')


# In[3]:


def isPrime(x):
    for i in range(2,x):
        if x % i == 0:
            return False
    return True



for i in range (2,100):
    if isPrime(i):
        print(i)


# In[5]:


def artikYilmi(yil):
    return yil % 4 == 0

print(artikYilmi(1990))
print(artikYilmi(2004))


# In[20]:


for i in range(10):
    for j in range(10- int(i/2)):
        print(' ', end="")
    for j in range(i):
        print('*', end="")
    print()


# In[26]:


def half_pyramid(rows):
    print('Half pyramid...\n')
    for i in range(rows):
        print('*' * (i+1))

def full_pyramid(rows):
    print('\nFull pyramid...\n')
    for i in range(rows):
        print(' '*(rows-i-1) + '*'*(2*i+1))

def inverted_pyramid(rows):
    print('\nInverted pyramid...\n')
    for i in reversed(range(rows)):
        print(' '*(rows-i-1) + '*'*(2*i+1))

def inverted_half_pyramid(rows):
    for i in range(rows):
        for j in range(rows-i+1):
            print(' ', end="")
        for j in range(i+1):
            print('*', end="")
        print()
    

half_pyramid(5)
full_pyramid(5)
inverted_pyramid(5)
inverted_half_pyramid(5)


# In[31]:


for i in range (2):
    for j in range (3):
        print(i+j)


# In[ ]:




