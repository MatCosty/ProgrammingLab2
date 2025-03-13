#import numpy as np

#3 esempi di liste create con un for e poi con una list comprehension
simple_list = []

for i in range(1,7):
    simple_list.append(i)

simple_list = [i for i in range(1, 7)]

even_list = []

for i in range(10):
    if i % 2 == 0:
        even_list.append(i)

even_list = [i for i in range(10) if i % 2 == 0]

ranged_list = []

for i in range(10):
    if 2 < i < 8:
        ranged_list.append(i)

ranged_list = [i for i in range(10) if 2 < i < 8]

#vettore di numeri primi

def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
        
    return True

primi = [0, 1, 2, 3, 5, 7]

print(len(primi))
#print(primi.size())

#print(primi.dtype())

primi = [i for i in range(10) if is_prime(i)]

print(primi)