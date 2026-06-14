def is_positive(n):
    if n > 0:
        return True
    elif n < 0:
        return False
    else:
        return None
def is_even(n):
    return n % 2 == 0
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
    if n >=0:
        fac = 1
        for i in range(1, n+1):
            fac *= i
    else:
        fac = "Undefined"
    return fac
def multiplication_table(n):
    table = []
    for i in range(1,11):
        table.append(f"{n} * {i} = {n * i}")
    return table
def number_analyzer(n):
    return {"positive": is_positive(n), "even": is_even(n), "prime": is_prime(n), "factorial": factorial(n), "table": multiplication_table(n)}
def main():
    n = int(input("Enter number: "))
    result = number_analyzer(n)
    print("\n--- Analysis Report ---")
    print(f"Number Type: {'Positive' if result['positive'] is True else 'Negative' if result['positive'] is False else 'Neutral'}")
    print(f"Even or Odd:      {'Even' if result['even'] is True else 'Odd'}")
    print(f"Prime:     {'Yes' if result['prime'] is True else 'No'}")
    print(f"Factorial: {result['factorial']}")
    print("\nMultiplication Table:")
    for row in result['table']:
        print(f"{row}")
main()