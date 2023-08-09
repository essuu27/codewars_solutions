# Write a function that takes in a line, splits it into individual words and returns
# an array made up of those words following by a space and their length

def add_length(str_):
    x = str_.split(" ")
    str_ = [ (f"{y} {len(y)}") for y in x ]
    return(str_)

