# Write a function that returns the count of characters that have to be 
# removed in order to get a string with no consecutive repeats.

def count_repeats(txt):
    holdchar = ''
    count = 0

    for x in text:
        if x == holdchar:
            count += 1
        holdchar = x

    return(count)
