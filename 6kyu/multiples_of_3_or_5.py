# Add together all integers from 1 to (number) that are multiples
# of 3 or 5. Add a multiple only once. Return the sum

def solution(number):
    mysum = 0
    if number > 0:
        for i in range(1, number):
            if (i % 3 == 0) | (i % 5 == 0):
                mysum += i
    return(mysum)