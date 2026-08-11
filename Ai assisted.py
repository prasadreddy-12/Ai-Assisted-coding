def is_happy_number(n):
    """
    Check if a number is a happy number.
    A happy number is defined by the following process:
    1. Start with any positive integer
    2. Replace the number by the sum of the squares of its digits
    3. Repeat the process until the number equals 1 (happy) or loops endlessly (unhappy)
    """
    seen = set()
    
    while n != 1 and n not in seen:
        seen.add(n)
        # Calculate sum of squares of digits
        n = sum(int(digit) ** 2 for digit in str(n))
    
    return n == 1


def find_happy_numbers(limit):
    """Find all happy numbers up to a given limit"""
    happy_numbers = []
    for num in range(1, limit + 1):
        if is_happy_number(num):
            happy_numbers.append(num)
    return happy_numbers


# Test the functions
if __name__ == "__main__":
    # Check if specific numbers are happy
    test_numbers = [7, 10, 19, 20, 23]
    print("Testing individual numbers:")
    for num in test_numbers:
        result = is_happy_number(num)
        print(f"{num} is {'happy' if result else 'unhappy'}")
    
    # Find all happy numbers up to 100
    print("\nHappy numbers up to 100:")
    happy_nums = find_happy_numbers(100)
    print(happy_nums)


Output:

Testing individual numbers:
7 is happy
10 is happy
19 is happy
20 is unhappy
23 is happy

Happy numbers up to 100:
[1, 7, 10, 13, 19, 23, 28, 31, 32, 44, 49, 68, 70, 79, 82, 86, 91, 94, 97, 100]
