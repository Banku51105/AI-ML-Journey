# Q1 — Create and access dictionary
a = {
    "name": "Banku",
    "age": 21,
    "course": "AI/ML"
}
print("Name:", a["name"])
print("Age:", a["age"])

# Q2 — Add and update values
a["city"] = "Jaipur"
print(a)

# Q3 — Update value
a["age"] = 22
print(a)

# Q4 — Loop through dictionary
for i in a:
    print(i, "->", a[i])

# Q5 — Frequency counter (VERY IMPORTANT)
text = "banana"
freq = {}
for char in text:
    if char in freq:
        freq[char] += 1
    else:
        freq[char] = 1
print(freq)

# Q6 — Find highest frequency character
highest_freq = 0
for i in freq:
    if freq[i] > highest_freq:
        highest_freq = freq[i]
        key = i
print(key, "->", highest_freq)

# Q7 — Word frequency
sen = "python is good python is powerful"
lst = sen.split(" ")
freq = {}
for word in lst:
    if word in freq:
        freq[word] += 1
    else:
        freq[word] = 1
print(freq)

# Q8 — First non-repeating character
# Logic -> we'll first check frequency of the char in word then run loop on word again and print the key which comes first in freq dict with value 1
word = "swiss"
freq = {}
for char in word:
    if char in freq:
        freq[char] += 1
    else:
        freq[char] = 1
for i in word:
    if freq[i] == 1:
        print(i)
        break

# Q9 — Character with lowest frequency
# Logic same as the highest freq one we just have to find lowest one
word = "banana"
freq = {}
for char in word:
    if char in freq:
        freq[char] += 1
    else:
        freq[char] = 1
lowest_freq = len(word) # cause if the word has same letter "ssssss" then lowest freq wont be more than length of the word
for i in freq:
    if freq[i] < lowest_freq:
        lowest_freq = freq[i]
        key = i
print(key, "->", lowest_freq)

# Q10 — Invert dictionary
# Logic -> we'll create a inversed dict and add value as key and key as value in new dict
a = {"a":1,"b":2,"c":3}
inversed_a = {}
for i in a:
    inversed_a[a[i]] = i
print(inversed_a)

# Q11 — Student Marks
# Logic -> same as we did in highest freq we just have to find who has highest marks and print the one with highest
marks = {
    "Banku":85,
    "Rahul":72,
    "Aman":91
}
highest_marks = 0
for i in marks:
    if marks[i] > highest_marks:
        highest_marks = marks[i]
        name = i
print("Highest Marks ->", name)

# Q12 — Count words longer than 4 letters
# Logic -> we gotta make a list with splitting the sentence at " " then find length of all elements of the list then print the one whose length is more than 4
sen = "python is good programming language"
lst = sen.split(" ")
longer_words = {}
for i in lst:
    word_len = len(i)
    if word_len > 4:
        longer_words[i] = word_len
print(longer_words)

# Q13 — Dictionary-based duplicate finder
# Logic -> we gotta find frequency then print the one whose freq is more than 1
nums = [1,2,2,3,1,4,4]
freq = {}
duplicate_list = []
for num in nums:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1
for i in freq:
    if freq[i] > 1:
        duplicate_list.append(i)
print(duplicate_list)

# Q14 — Most frequent word
# Logic -> same as highest freq we gotta find freq then print the one whose freq is high
sen = "python is good python is powerful python"
lst = sen.split(" ")
freq = {}
most_frequent_word_freq = 0
for word in lst:
    if word in freq:
        freq[word] += 1
    else:
        freq[word] = 1
for i in freq:
    if freq[i] > most_frequent_word_freq:
        most_frequent_word_freq = freq[i]
        most_frequent_word = i
print(most_frequent_word, "->", most_frequent_word_freq)