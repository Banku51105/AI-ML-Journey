# Q1 — Remove duplicates using set
l = [1,2,2,3,1,4]
s = list(set(l))
print(s)

# Q2 — Union of sets
a = {1,2,3}
b = {3,4,5}
c = a | b
print(c)

# Q3 — Intersection of sets
a = {1,2,3}
b = {2,3,4}
c = a & b
print(c)

# Q4 — Difference of sets
a = {1,2,3,4}
b = {3,4}
c = a - b
print(c)

# Q5 — Check subset
a = {1,2}
b = {1,2,3,4}
if a | b == b:   # a <= b(i found this one on google but i did solved on my own first)
    print("a subset of b")

# Q6 — Common elements between lists using sets
a = [1,2,3,4]
b = [3,4,5,6]
c = set(a) & set(b)
print(c)

# Q7 — Unique words counter
a = "python is good python is powerful"
count = len(set(a.split(" ")))
print(count)