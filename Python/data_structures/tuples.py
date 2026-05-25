# Q1 — Tuple basics
t = (10,20,30,40)
print(t[0])
print(t[-1])
print(t[1:3])

# Q2 — Tuple immutability
t = (1,2,3)
# t[0] = 1
print(t)
# TypeError: 'tuple' object does not support item assignment
# it shows this error cause tuple is immutable

# Q3 — Packing & unpacking
a = 5
b = 10
a, b = b, a

# Q4 — Count occurrences
t = (1,2,2,3,2)
count = 0
for i in t:
    if i == 2:
        count += 1
print(count)

# Q5 — Find maximum in tuple manually
t = (4,8,2,9,1)
max_num = t[0]
for i in t:
    if i > max_num:
        max_num = i
print(max_num)

# Q6 — Convert list to tuple and tuple to list
t = (1,2,3)
l = list(t)
print(l)
t2 = tuple(l)
print(t2)

# Q7 — Nested tuple traversal
t = ((1,2),(3,4),(5,6))
for i in t:
    for j in i:
        print(j)
