# Write a function which calculates the average of the numbers in a given list.
# Empty arrays should return 0.

def find_average(numbers) -> int:
  return(sum(numbers) / len(numbers)) if (len(numbers) > 0) else 0
