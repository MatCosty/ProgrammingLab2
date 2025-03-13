#3 esempi di liste create con un for e poi con una list comprehension
simple_list = []

for i in range(1,7):
    simple_list.append(i)

simple_list = [i for i in range(1, 7)]

print(simple_list)