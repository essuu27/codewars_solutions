# Given a string, replace every letter with its position in the alphabet.
# If anything in the text isn't a letter, ignore it and don't return it.

def strnum(mystr):
    h = [(str(ord(x.lower()) - 96)) for x in mystr if x.isalpha()]
    return(' '.join(h))
