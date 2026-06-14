# Functions Set 1
# Question 1 — Even or Odd Function
def is_even(n):
    if n % 2 == 0:
        print("Even")
    else:
        print("Odd")
is_even(10)
is_even(7)

# Question 2 — Square Function
def square(n):
    return n * n
x = square(5)
print(x)

# Question 3 — Largest of Two Numbers
def largest(a, b):
    if a > b:
        return a
    else:
        return b
print(largest(10, 20))

# Question 4 — Count Vowels
def count_vowels(word):
    vowels = ["a", "e", "i", "o", "u"]
    count = 0
    for i in word.lower():
        if i in vowels:
            count += 1
    return count
print(count_vowels("Banku"))

# Question 5 — Factorial Function
def factorial(n):
    fac = 1
    for i in range(1,n+1):
        fac = fac * i
    return fac
print(factorial(5))

# Question 6 — List Sum Function
def list_sum(nums):
    s = 0
    for i in nums:
        s += i
    return s
print(list_sum([1,2,3,4]))

# Question 7 — Character Frequency
def char_frequency(word):
    freq = {}
    for char in word:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    return freq
print(char_frequency("banana"))

# Question 8 — Palindrome Function
def is_palindrome(word):
    if word[::-1] == word:
        return True
    else:
        return False
print(is_palindrome("madam"))

# Functions Set 2
# Question 1 — Reverse String
def reverse_string(word):
    return word[::-1]
print(reverse_string("Banku"))

# Question 2 — Count Even Numbers in List
def count_even(nums):
    count = 0
    for i in nums:
        if i % 2 == 0:
            count +=1
    return count
print(count_even([1,2,3,4,6]))

# Question 3 — Find Largest Element in List
def find_largest(nums):
    largest = nums[0]
    for i in nums:
        if i > largest:
            largest = i
    return largest
print(find_largest([1,2,53,4,6]))

# Question 4 — Remove Duplicates
def remove_duplicates(nums):
    result = []
    for i in nums:
        if i not in result:
            result.append(i)
    return result
print(remove_duplicates([1,2,2,3,1,4]))

# Question 5 — Word Frequency Function
def word_frequency(sentence):
    words = sentence.split(" ")
    freq = {}
    for word in words:
        if word in freq:
            freq[word] +=1
        else:
            freq[word] = 1
    return freq
print(word_frequency("python is good python is"))

# Question 6 — Armstrong Number Checker
def is_armstrong(n):
    total = 0
    og = n
    while n > 0:
        digit = n % 10
        total += digit ** len(str(og))
        n = n // 10
    if total == og:
        return True
    else:
        return False
print(is_armstrong(153))

# Question 7 — Most Frequent Character
def most_frequent_char(word):
    freq = {}
    for char in word:
        if char in freq:
            freq[char] +=1
        else:
            freq[char] = 1
    a = tuple(freq.items())
    most_freq_char = a[0][0]
    most_frequent_char_freq = a[0][1]
    for i in a:
        if i[1] > most_frequent_char_freq:
            most_freq_char = i[0]
            most_frequent_char_freq = i[1]
    return most_freq_char, most_frequent_char_freq
print(most_frequent_char("banana"))

# Question 8 — Student Topper Function
def find_topper(marks):
    highest_marks = 0
    for i in tuple(marks.items()):
        if i[1] > highest_marks:
            topper = i[0]
            highest_marks = i[1]
    return topper, highest_marks
print(find_topper({"Banku":85,"Rahul":72,"Aman":91}))

# Question 9 — Prime Number Checker
def is_prime(n):
    prime = True
    if n < 2:
        prime = False
    else:
        for i in range(2, n):
            if n % i == 0:
                prime = False
                break
    return prime
print(is_prime(7))
print(is_prime(10))

# Question 10 — Function Composition (New Idea)
def square(n):
    return n * n
def cube(n):
    return square(n) * n
print(cube(3))

# Functions Set 3
# Question 1 — Function Calling Function
def square(n):
    return n * n
def double_square(n):
    return square(n) * 2
print(double_square(3))

# Question 2 — Multiple Returns
def min_max(nums):
    return min(nums), max(nums)
print(min_max([5,2,8,1,9]))
# I feel like i slacked off by using in built functions
def min_max2(nums2):
    mini = nums2[0]
    maxi = nums2[0]
    for i in nums2:
        if i < mini:
            mini = i
        elif i > maxi:
            maxi = i
    return mini, maxi
print(min_max2([5,2,8,1,9]))
# Now i feel little bit better

# Question 3 — Default Arguments
def greet(name="Guest"):
    print("Hello",name)
greet()
greet("Banku")

# Question 4 — Average Marks
def calculate_average(marks):
    total = 0
    for i in marks:
        total += i
    average = total/len(marks)
    return average
print(calculate_average([85,72,91,88]))

# Question 5 — Split Logic Into Functions
def count_vowels(word):
    vowels = ["a", "e", "i", "o", "u"]
    count = 0
    for i in word.lower():
        if i in vowels:
            count += 1
    return count
def count_consonants(word):
    vowels = ["a", "e", "i", "o", "u"]
    count = 0
    for i in word.lower():
        if i not in vowels:
            count += 1
    return count
def analyze_word(word):
    return count_vowels(word), count_consonants(word)
print(analyze_word("Banku"))

# Question 6 — Number Analyzer Mini Version
def is_even(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"
def is_prime(n):
    prime = True
    if n < 2:
        prime = False
    else:
        for i in range(2, n):
            if n % i == 0:
                prime = False
                break
    return prime
def factorial(n):
    fac = 1
    for i in range(1, n+1):
        fac *= i
    return fac
def analyze_number(n):
    return is_even(n), is_prime(n), factorial(n)
print(analyze_number(5))

# Function Practice Set #4 (Final)
# Question 1 — Sum Any Number of Values (*args)
def add_all(*args):
    total = 0
    for i in args:
        total += i
    return total
print(add_all(1,2,3))
print(add_all(10,20,30,40))

# Question 2 — Student Info (**kwargs)
def show_student(**kwargs):
    for i in tuple(kwargs.items()):
        print(i[0], "->", i[1])
show_student(name="Banku",age=21,branch="Mechanical")

# Question 3 — Return Multiple Values
def circle_info(radius):
    pi = 3.14
    area = pi * radius ** 2
    circumference = 2 * pi * radius
    return area, circumference
area, circum = circle_info(5)
print(area)
print(circum)

# Question 4 — Largest Even Number
def largest_even(nums):
    largest = 0
    for i in nums:
        if i % 2 == 0:
            if i > largest:
                largest = i
    return largest
print(largest_even([3,8,11,2,14]))

# Question 5 — Reuse Functions
def is_vowel_heavy(word):
    if count_vowels(word) > count_consonants(word):
        return True
    else:
        return False
print(is_vowel_heavy("Banku"))

# Question 6 — Frequency Analyzer
def frequency_analyzer(word):
    freq = {}
    for i in word:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    frequency = next(iter(freq.values()))
    most_frequent_char = next(iter(freq.keys()))
    for i in tuple(freq.items()):
        if i[1] > frequency:
            frequency = i[1]
            most_frequent_char = i[0]
    return most_frequent_char, frequency
print(frequency_analyzer("mississippi"))

# Question 7 — Mini Grade System
def get_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 80:
        return "B"
    elif marks >= 70:
        return "C"
    elif marks >= 60:
        return "D"
    else:
        return "F"
print(get_grade(95))

# Question 8 — Mini Project Thinking
def analyze_number(n):
    analyze = {}
    analyze["even"] = is_even(n)
    analyze["prime"] = is_prime(n)
    analyze["factorial"] = factorial(n)
    return analyze
print(analyze_number(5))