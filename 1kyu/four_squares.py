import math

#my_num = 9287645
my_num = 215
lang_arr = []

while my_num > 0:
#  x = int(my_num ** (1/2))
  x = int(math.sqrt(my_num))
  y = x ** 2
  print(x, my_num)
  my_num = my_num - y
  
  