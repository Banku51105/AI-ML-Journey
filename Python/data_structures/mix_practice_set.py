# Q1 — Most frequent character
# Logic -> we gotta create a freq dict then print the one whose freq is highest
word = "mississippi"
freq = {}
for char in word:
    if char in freq:
        freq[char] += 1
    else:
        freq[char] = 1
most_frequent_char = next(iter(freq))
most_frequent_char_freq = freq[most_frequent_char]
for i in freq:
    if freq[i] > most_frequent_char_freq:
        most_frequent_char_freq = freq[i]
        most_frequent_char = i
print(most_frequent_char, "->", most_frequent_char_freq)

# Q2 — Common unique elements
# Logic -> basic sets
a = [1,2,2,3,4]
b = [2,2,4,5]
unique_elements = set(a) & set(b)
print(unique_elements)

# Q3 — Tuple unpacking
student = ("Banku",21,"AI/ML")
name, age, course = student
print("Name -> ", name)
print("Age -> ", age)
print("Course -> ", course)
print(f"Name -> {name}\nAge -> {age}\nCourse -> {course}")

# Q4 — First repeated character
word = "programming"
freq = {}
for char in word:
    if char in freq:
        freq[char] += 1
    else:
        freq[char] = 1
    if freq[char] > 1:
        print(char)
        break

# Q5 — Merge frequencies
list1 = ["a","b","a"]
list2 = ["b","c","a"]
freq = {}
for i in list1 + list2:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1
print(freq)

# Q6 — Remove duplicate words
sen = "python is good python is powerful"
words = sen.split(" ")
visited = set()
result = []
for word in words:
    if word not in visited:
        result.append(word)
        visited.add(word)
print(" ".join(result))

# Q7 — Student topper and average marks
marks = {"Banku":85,"Rahul":72,"Aman":91,"Priya":88}
highest_marks = next(iter(marks.values()))
total = 0
topper = next(iter(marks))
for i in marks:
    if marks[i] > highest_marks:
        highest_marks = marks[i]
        topper = i
    total += marks[i]
average = total/len(marks)
print(f"Topper -> {topper} -> {highest_marks}\nAverage -> {average}")

# Q8 — Frequency sorted output
word = "banana"
freq = {}
for char in word:
    if char in freq:
        freq[char] += 1
    else:
        freq[char] = 1
a = list(freq.items())
for i in range(len(a)):
    for j in range(len(a)-1):
        if a[j][1] < a[j+1][1]:
            a[j], a[j+1] = a[j+1], a[j]
for key, value in dict(a).items():
    print(f"{key} -> {value}")