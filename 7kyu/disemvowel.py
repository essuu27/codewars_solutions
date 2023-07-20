# write a function that takes a string and return a new string 
# with all vowels removed.

def disemvowel(string_):
  vowels = ['a','A','e','E','i','I','o','O','u','U']

  for x in vowels:
    string_ = string_.replace(x,'')

  return(string_)
