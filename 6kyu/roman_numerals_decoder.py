"""
Create a function that takes a Roman numeral as its argument and returns 
its value as a numeric decimal integer.
"""

def solution(roman):
  numerals = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000,' ':0}
  score = 0
  roman = f"{roman} "
  for x in range(len(roman)-1):
    if numerals[roman[x]] >= numerals[roman[x+1]]:
      score = score + numerals[roman[x]]
      print(f"{roman[x]} {score} + {numerals[roman[x]]} {numerals[roman[x+1]]}")
    else:
      score = score - numerals[roman[x]]
      print(f"{roman[x]} {score} - {numerals[roman[x]]} {numerals[roman[x+1]]}")
  return(score)