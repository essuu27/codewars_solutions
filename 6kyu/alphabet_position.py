# Given a string, replace every letter with its position in the alphabet.

def alphabet_position(text):
    h = [(str(ord(x.lower()) - 96)) for x in text if x.isalpha()]
    return(' '.join(h))