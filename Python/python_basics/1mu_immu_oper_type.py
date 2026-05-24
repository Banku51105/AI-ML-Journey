#1
a = 10
b = 3
print(a + b)
print(a / b)
print(a // b)
print(a % b)

#2
b = input("No. ")
c = int(b)
print(c**2)

#3
lst = [1, 2, 3]
lst[1] = 10
print(lst)

#4
a = 5
b = "5"
print(a + int(b))

#5
x = [1, 2, 3]
y = x
y[0] = 100
print(x)

#6
print('a' in 'apple')
print('z' not in 'apple')

#7
print(10 > 5 and 2 < 1)
print(10 > 5 or 2 < 1)
print(not(10 > 5))

#8
a = [1,2,3]
b = [1,2,3]
print(a == b)
print(a is b)

#9
g = input("Enter: ")
if g.isdigit():
    num = int(g)
    print(num*2)
else:
    print("Invalid input")

#10
a = [1, 2, 3]
b = a.copy()
b[0] = 100
print(a)
print(b)

#11
x = "10"
y = "20"
print(x + y)
print(int(x) + int(y))

#12
a = 1000
b = 1000
print(a == b)
print(a is b)

#13
v = input("Enter: ")
x = int(v)
if x%2 == 0:
    print("Even")
else:
    print("Odd")