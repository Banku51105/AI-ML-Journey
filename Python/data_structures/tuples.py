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
