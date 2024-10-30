# Write a function which takes a list of strings and returns each line
#  prepended by the line number using the format 'n: string'

def number(lines):
    outs = [f"{x}: {y}" for x,y in enumerate(lines, 1)]
    return(outs)
