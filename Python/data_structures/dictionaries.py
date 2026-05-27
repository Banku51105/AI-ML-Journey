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
a["age"] = 22
print(a)

# Q3 — Frequency counter (VERY IMPORTANT)
text = "banana"
freq = {}
for char in text:
    if char in freq:
        freq[char] += 1
    else:
        freq[char] = 1
print(freq)

