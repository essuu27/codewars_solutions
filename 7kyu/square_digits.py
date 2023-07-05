# square every digit of a number and concatenate them

def square_digits(num):
    outstr = ''
    for x in str(num):
        outstr = outstr + (str(int(x)**2))
    return(int(outstr))
