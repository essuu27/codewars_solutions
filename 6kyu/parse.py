"""
Write a simple parser that will parse and run Deadfish.

Deadfish has 4 commands, each 1 character long:

i increments the value (initially 0)
d decrements the value
s squares the value
o outputs the value into the return array
"""

def parse(data):
    sum = 0
    output = []
    for x in data:
        match x:
            case 'i':
                sum += 1
            case 'd':
                sum -= 1
            case 's':
                sum = sum * sum
            case 'o':
                output.append(sum)
    return(output)