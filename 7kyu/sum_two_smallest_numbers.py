# Create a function that returns the sum of the two lowest positive numbers
# given an array of minimum 4 positive integers.

def sum_two_smallest_numbers(numbers):
    numbers.sort()
    return numbers[0] + numbers[1]
