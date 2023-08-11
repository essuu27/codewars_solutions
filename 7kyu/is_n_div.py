# Create a function that checks if the first argument n is divisible
# by all other arguments

def is_divisible(*args):
  mynum = args[0]
  y = True
  for x in args:
    if (mynum // x) != (mynum / x):
      y = False
  return(y)
