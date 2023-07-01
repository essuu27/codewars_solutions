# A routine that returns True/False if the input number is narcissistic:
# the sum of its own digits, each raised to the power of the number of digits

def narcissistic( value ):
    base=len(str(value))
    z = 0
    for y in str(value):
        z += pow(int(y), base) 

    return True if int(value) == int(z) else False
