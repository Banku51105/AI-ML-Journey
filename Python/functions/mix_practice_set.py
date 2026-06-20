# Q1 — Count Even Numbers
def count_even(nums):
    return len([x for x in nums if x%2==0])
print(count_even([1,2,3,4,6]))

# Q2 — Most Frequent Character
def most_frequent_char(word):
    freq = {}
    for char in word:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    most_freq_char = next(iter(freq.keys()))
    most_freq_char_freq = next(iter(freq.values()))
    for j in freq.items():
        if j[1] > most_freq_char_freq:
            most_freq_char = j[0]
            most_freq_char_freq = j[1]
    return most_freq_char,most_freq_char_freq
print(most_frequent_char("banana"))

# Q3 — Student Average
def calculate_average(marks):
    total = 0
    for i in marks:
        total += i
    average = total/len(marks)
    return average
print(calculate_average([85,72,91]))

# Q4 — Filter Even Numbers
nums = [1,2,3,4,5,6]
result = list(filter(lambda x: x%2==0, nums))
print(result)

# Q5 — Square Numbers
def square_numbers(nums):
    return [x*x for x in nums]
print(square_numbers([1,2,3,4]))

# Q6 — Word Frequency
def word_frequency(sentence):
    freq = {}
    for word in sentence.split(" "):
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1
    return freq
print(word_frequency("python is good python"))

# Q7 — Function Reuse
def word_frequency(word):
    freq = {}
    for char in word:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    return freq
def most_frequent_char(word):
    frequency = word_frequency(word)
    most_freq_char = next(iter(frequency.keys()))
    most_freq_char_freq = next(iter(frequency.values()))
    for j in frequency.items():
        if j[1] > most_freq_char_freq:
            most_freq_char = j[0]
            most_freq_char_freq = j[1]
    return most_freq_char,most_freq_char_freq
def analyze_word(word):
    return {"frequency" : word_frequency(word), "most_frequent" : most_frequent_char(word)}
print(analyze_word("banana"))

# Q8 — Mini Challenge
def topper(marks):
    topper_student = next(iter(marks.keys()))
    highest_marks = next(iter(marks.values()))
    for i in marks.items():
        if i[1] > highest_marks:
            topper_student = i[0]
            highest_marks = i[1]
    return topper_student,highest_marks
print(topper({"Banku":85,"Rahul":72,"Aman":91}))