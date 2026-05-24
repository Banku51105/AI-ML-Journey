# Q1 — Sum of all elements (solved in 5min)
# we just have to take 1st element add it to sum thn take 2nd add it and so on
# Code
n = [1,2,3,4]
total = 0
for num in n:
    total += num
print(total)

# Q2 — Find largest element (solved in 2-3min)
# we have to take 1st num say it is largest then take 2nd num if 1st<2nd then largest = 2nd and so on
# Code
n = [4,8,2,9,1]
largest_num = n[0]
for i in n:
    if i > largest_num:
        largest_num = i
print(largest_num)

# Q3 — Count even numbers in list (solved in 2-3min)
# we have to see if num%2 =0 if yes then count +=1 and so on
# Code
n = [1,2,3,4,6]
count = 0
for i in n:
    if i % 2 == 0:
        count+=1
print(count)

# Q4 — Remove duplicates manually (solved in 10-15min) (it was easy one but i was trying to complicate it more)
# we have to create new m list if the element in n is not in m then add it and we'll have a list with no duplicate element
# Code
n = [1,2,2,3,1,4]
m = []
count = 0
for i in n:
    if i not in m:
        m.append(i)
print(m)

# Q5 — Reverse list manually (solved in 5-10min) (i was trying to use slicing first but then i saw no slicing in question then i tried to find something and found insert in my lecture notes
#we can use insert to add elements on 0th index each time and we'll have reverse list
# Code
n = [1,2,3,4]
rev_list = []
for i in n:
    rev_list.insert(0,i)
print(rev_list)

# Q6 — Find second largest number (solved it in maybe 20-25min) (i tried to find directly second largest but i couldnt so i just found largest then 2nd largest)
# we gotta find largest num first then find second largest num
# Code
n = [4,8,2,9,1]
largest = n[0]
second_largest = n[0]
for num in n:
    if num > largest:
        second_largest = largest
        largest = num
    elif num > second_largest and num != largest:
        second_largest = num

# Q7 — Frequency of elements (solved in 5-6min) (just copied the string frequency code and replaced string with list maybe i should have tried to solv e it myself but i copied next time i wont)
# we gotta take first num check how many times it is then take 2nd num if it is already done then dont count if it isnt taken earlier then count how many time it is and so on
# Code
n = [1,2,2,3,1,1]
visited = []
for i in n:
    if i not in visited:
        count = 0
        for j in n:
            if i == j:
                count += 1
        print(i, "->", count)
        visited.append(i)

# Q8 — Move all zeros to end (solved in like 15-20min) (i did thought of logic in like 4-5 min but i had to think more about how to sort it then i remembered that we used sorted func one time and used that)
# we gotta check if the num is zero add them to diff list if it is non zero then to diff list and in last add both of them
# Code
n = [1,0,2,20,3,0,4]
zero_list = []
nonzero_list = []
for i in n:
    if i > 0:
        nonzero_list.append(i)
    else:
        zero_list.append(i)
print(nonzero_list+zero_list)

# Q9 — Rotate list right by 1
# we gotta add s1 + s1 and then add element in new list from 1st index to og list len index of big list
# Code
n = [1,2,3,4]
m = n + n
o = []
for i in range(1,len(n)+1):
    o.append(m[i])
print(o)

#Best code
n = [1,2,3,4]
rotated = [n[-1]]
for num in n[:-1]:
    rotated.append(num)
print(rotated)

# Q10 — Common elements in two lists
# we gotta run for loop on first list then run on 2nd list and check if both list have same elements and add them in new list
# Code
n = [1,2,3,4]
m = [3,4,5,6]
o = []
for i in n:
    if i in m:
        o.append(i)
print(o)

# Q11 — List palindrome (logic in like 10-15sec as soon as i saw it clicked what i have to do)
# we gotta reverse the list and equate both of them if they are equal then they are palindrome
# Code
n = [1,2,3,2,1]
m = n[::-1]
if n == m:
    print(True)
else:
    print(False)

# Q12 — Missing number (logic in like 3-4min)
# we'll use range in it with (1,largestnum) and if there are all nums uptil largest num in list then done if there arent then print
# Code
n = [1,2,4,5]
largest = n[0]
missing_nums = []
for i in n:
    if i > largest:
        largest = i
for j in range(1,largest+1):
    if j not in n:
        missing_nums.append(j)
print(missing_nums)

# Q13 — Merge two sorted lists manually (logic in like 15-20min) (i thought first how am i going to solve it but then i saw Q12 solution again and it clicked i can solve like this)
# first of all we gotta add both of list and make a bigger list then
list1 = [1, 3, 5]
list2 = [2, 4, 6]
merged_list = []
i = 0
j = 0
while i < len(list1) and j < len(list2):
    if list1[i] < list2[j]:
        merged_list.append(list1[i])
        i += 1
    else:
        merged_list.append(list2[j])
        j += 1
while i < len(list1):
    merged_list.append(list1[i])
    i += 1
while j < len(list2):
    merged_list.append(list2[j])
    j += 1
print(merged_list)


# Q14 — Pair with target sum (solved in 5min solved first without thinking of logic) (its working but i dont think you want this solution)
# we gotta take num from list check if there is any num that can be added and the target will be found and print both of them
# Code
n = [2,7,11,15]
target = 9
m = []
for i in n:
    if target - i in n:
        m.append(i)
print(m)

# best version
n = [2,7,11,15]
target = 9
for i in range(len(n)):
    for j in range(i+1, len(n)):
        if n[i] + n[j] == target:
            print(n[i], n[j])

# Q15 — Remove all occurrences of element
# we gotta check all elements and remove the element which needs to be remove
# Code
l1 = [1,2,2,3,2,4]
r = 2
l2 = []
for i in l1:
    if i != r:
        l2.append(i)
print(l2)

# Q16 — Find duplicate elements only once
# we gotta count frequency of the element then print those whose frequency is more than 1
# Code
n = [1,2,2,3,1,4,4]
duplicate = []
for i in n:
    if i not in duplicate:
        count = 0
        for j in n:
            if j == i:
                count +=1
        if count > 1:
            duplicate.append(i)
        count = 0
print(duplicate)

# Q17 — Check if two lists contain same elements
# we gotta count frequency of all elements then check if frequency of 1st list elements is = frequency of 2nd list
# Code
list1 = [1,2,3,2,3,3]
list2 = [3,2,1,3,2,3]
if sorted(list1)==sorted(list2):
    print(True)
else:
    print(False)

# Q18 — Find element with highest frequency
# we gotta count frequency of all elements and then the one which has highest frequency will be printed
# Code
list1 = [1,2,2,3,1,1,1,2]
visited = []
highest_frequency = 0
for i in list1:
    if i not in visited:
        count = 0
        for j in list1:
            if j == i:
                count += 1
        if count > highest_frequency:
            highest_frequency = count
            high_fre_num = i
        visited.append(i)
print(high_fre_num,"->",highest_frequency)

# Q19 — Bubble sort manually
#
# Code
n = [5,1,4,2]
for i in range(len(n)):
    for j in range(len(n)-1):
        if n[j] > n[j+1]:
            n[j], n[j+1] = n[j+1], n[j]
print(n)

# Q20 — Separate positives and negatives
# We have to check if it is positive or negative if positive and append positive first and then append negative
# Code
n = [1,-2,3,-4,5]
m = []
for i in n:
    if i > 0:
        m.append(i)
for j in n:
        if j < 0:
            m.append(j)
print(m)

# Q21 — List comprehension basics
# Code
print([i**2 for i in [1,2,3,4]])

# Q22 — List comprehension with condition
# Code
print([i for i in [1,2,3,4,5,6] if i%2==0])

# Q23 — Flatten nested list
# Code
n = [[1,2],[3,4],[5]]
m = []
for i in range(len(n)):
    for j in range(len(n[i])):
        num = n[i][j]
        m.append(num)
print(m)

# Q24 — Find row sum in matrix
n = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
for i in range(len(n)):
    row_sum = 0
    for j in range(len(n[i])):
        row_sum += n[i][j]
    print("Row",i,"->",row_sum)

# Q25 — Matrix transpose thinking
# Code
n = [
    [1,2,3],
    [4,5,6]
]
transpose = []
for col in range(len(n[0])):
    row_list = []
    for row in range(len(n)):
        row_list.append(n[row][col])
    transpose.append(row_list)
print(transpose)