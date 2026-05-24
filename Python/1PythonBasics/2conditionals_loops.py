1.
for i in range(1, 11):
    print(i)
2.
n = 1
i = 10
while i>=n:
    print(i)
    i=i-1
3.
n = 562
if n%2==0:
    print("Even")
else:
    print("Odd")

4.
for i in range(1,21):
    if i%2==0:
        print(i)

5.
n = 45
total = 0
for i in range(1, n+1):
    total = total + i
print(total)

6.
for i in range(4):
    for j in range(i+1):
        print("*",end=" ")
    print()

7.
for i in range(1,11):
    if i==5:
        continue
    print(i)

8.
for i in range(1,11):
    if i==6:
        break
    print(i)

9.
n = 54
sum=0
for i in range(1,n+1):
    if i%2==0:
        sum += i
print(sum)

10.
n = 67
count = 0
while n > 0:
    n = n // 10
    count += 1
print(count)

11.
n = 52
rev = 0
while n > 0:
    digit = n % 10
    rev = rev * 10 + digit
    n = n // 10
print(rev)

12.
rows = 4
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

13.
n = 875
total = 0
while n > 0:
    digit = n % 10
    total += digit
    n = n // 10
print(total)

14.
n = 256
original = n
rev = 0
while n > 0:
    digit = n % 10
    rev = rev * 10 + digit
    n = n // 10
if original == rev:
    print("Palindrome")
else:
    print("Not Palindrome")

15.
n = 5832
largest_digit = 0
while n > 0:
    digit = n % 10
    if digit > largest_digit:
        largest_digit = digit
    n = n // 10
print(largest_digit)

16.
n = 325
count = 0
while n > 0:
    digit = n % 10
    if digit % 2 == 0:
        count +=1
    n = n // 10
print(count)

17.
n = 215
og = n
total  = 0
while n > 0:
    digit = n % 10
    total = total + (digit**3)
    n = n // 10
if og == total:
    print(True)
else:
    print(False)

18.
n = 321
total  = 0
while n > 0:
    digit = n % 10
    total = total + (digit**2)
    n = n // 10
print(total)

19.
n = 254
while n > 0:
    digit = n % 10
    if digit == 0:
        print(True)
        break
    n = n // 10
else:
    print(False)

20.
n = 326
n = n // 10
print(n)

21.
#My code
n = 123456
rev = 0
l = len(str(n))/2
mid = int(l) + (l > int(l))
while n > 0:
    digit = n % 10
    rev = rev * 10 + digit
    n = n // 10
    if len(str(rev)) == mid:
        break
print(rev)

#Clean Code
n = 123456
temp = n
digits = len(str(n))
half = (digits + 1) // 2
rev = 0
count = 0
while count < half:
    digit = n % 10
    rev = rev * 10 + digit
    n = n // 10
    count += 1
print(rev)

22.
n = 123
product = 1
while n > 0:
    digit = n % 10
    product = product * digit
    n = n // 10
print(product)

23.
n = 2368
while n > 0:
    digit = n % 10
    if digit % 2 != 0:
        print(False)
        break
    n = n // 10
else:
    print(True)

24.
n = 5
factorial = 1
for i in range(1,n+1):
    factorial = factorial * i
print(factorial)

25.
n = 512
while n >= 10:
    n = n // 10
print(n)