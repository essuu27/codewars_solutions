# Complete the function that accepts a string parameter, and reverses each word
# in the string. All spaces in the string should be retained.

def reverse_words(text) -> str:
    bits = text.split(' ')
    outstr = ''
    for x in bits:
        outstr = outstr + x[::-1] + " "
    return outstr[:-1]
