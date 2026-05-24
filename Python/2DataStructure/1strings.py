print("hello"[::-1])

1.
n = "Python"
for i in n:
    print(i)

2.
#My Version
n = "Banku"
count = 0
vowels = ["a", "e", "i", "o", "u"]
for i in n:
    for j in vowels:
        if i == j:
            count +=1
            break
print(count)

#Best Version
n = "Banku"
count = 0
vowels = "aeiou"
for i in n:
    if i.lower() in vowels:
        count += 1
print(count)

3.
n = "madam"
rev = n[::-1]
if n == rev:
    print("Palindrome")
else:
    print("Not Palindrome")

4.
n = "Palindrome"
print(n.upper())
print(n.lower())
print(n[::-1])

5.
n = "banana"
count = 0
for i in n:
    if i == "a":
        count +=1
print(count)

6.
n = "I am Banku"
print(n.replace(" ", ""))

7.
n = "Python"
l = len(n)
for i in range(1, l+1):
    print(n[:i])

8.
n = "I am learning python"
m = n.split(" ")
l = len(m)
longest = 0
for i in range(l):
    length = len(m[i])
    if longest < length:
        longest = length
        lw = m[i]
print(lw)

9.
n = "manually"
count = 0
for i in n:
    count +=1
print(count)

10.
#My Version
n = "BaNkU"
Upper = 0
Lower = 0
for i in n:
    for j in range(65,91):
        upper = chr(j)
        lower = chr(j).lower()
        if i == upper:
            Upper += 1
        elif i == lower:
            Lower += 1
print("Upper:", Upper)
print("Lower:", Lower)

#Best Version
n = "BaNkU"
upper = 0
lower = 0
for i in n:
    if i.isupper():
        upper += 1
    elif i.islower():
        lower += 1
print("Upper:", upper)
print("Lower:", lower)

11.
n = "banku"
vowels = "aeiou"
nm = ""
for i in n:
    if i not in vowels:
        nm += i
print(nm)

12.
n = "silent"
m = "listen"
for i in n:
    for j in m:
        if i == j:
            break
    else:
        break
else:
    print("Anagram")

#Correct Version
n = "silent"
m = "listen"
if sorted(n) == sorted(m):
    print(True)
else:
    print(False)

13.
n = "banana"
for j in range(65, 91):
    k = chr(j).lower()
    frequency = 0
    if k in n:
        for i in n:
            x = k
            if i == k:
                frequency +=1
        print(x,"->",frequency)

#Best Version
n = "banana"
visited = ""
for i in n:
    if i not in visited:
        count = 0
        for j in n:
            if i == j:
                count += 1
        print(i, "->", count)
        visited += i

14.
n = "aaabbc"
count = 1
for i in range(len(n)-1):
    if n[i] == n[i+1]:
        count += 1
    else:
        print(n[i] + str(count), end="")
        count = 1
print(n[-1] + str(count))

15.
n = "swiss"
visited = ""
for i in n:
    if i not in visited:
        count = 0
        for j in n:
            if i == j:
                count +=1
        if count == 1:
            print(i)
            break

16.
n = "I am learning python"
count = 0
for i in n:
    if i == " ":
        count +=1
print(count+1)

17.
n = "BaNkU"
for i in n:
    if i.isupper():
        i = i.lower()
    elif i.islower():
        i = i.upper()
    print(i, end = "")

print("")

18.
s1 = "ABCD"
s2 = "CDAB"
s3 = s1 + s1
if s2 in s3:
    print(True)
else:
    print(False)

19.
n = "aaabbbbccdddddd"
count = 1
lcac = 0
for i in range(len(n)-1):
    if n[i] == n[i+1]:
        count +=1
    else:
        count = 1
    if lcac < count:
        lca = n[i] #longest consecutive alphabet
        lcac = count #longest consecutive alphabet count
print(lca, lcac)

20.
n = "I am Banku"
m = n.split(" ")
for i in range(len(m)):
     rev = m[i][::-1]
     print(rev, end = " ")