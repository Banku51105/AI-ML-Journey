# Q1
def count():
    for i in range(1,6):
        yield i
g = count()
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))

# Q2
def countdown(n):
    for i in reversed(range(1, n+1)):
        yield i
g = countdown(5)
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))

# Q3
def even_numbers(n):
    for i in range(1, n+1):
        if i % 2 == 0:
            yield i
g = even_numbers(10)
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))

# Q4
def square_generator(n):
    for i in range(1, n+1):
        yield i * i
g = square_generator(5)
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))