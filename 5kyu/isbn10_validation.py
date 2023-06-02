# Make a function that checks if a ISBN-10 number is valid. The ISBN-10 number format is 
# the first nine characters are digits 0-9. The last digit can be 0-9 or X, a value of 10.
# The number is valid if the sum of the digits multiplied by their position modulo 11 is zero.

def checkisbn(isbn: str):
    total = 0
    state = 0
        
    if (len(isbn) == 10) &  isbn[:-1].isdigit():
        x = 1
        for y in isbn:
            if (x == 10):
                if (y == 'X'):
                    y = '10'
                elif (not y.isdigit()):
                    state = 0
                    total = -1
                    break

            total += (x*int(y))
            x += 1

        if total % 11 == 0:
            state = 1

    if state == 1:
        return(True)
    else:
        return(False)

print(checkisbn('1234554321'))
