# Given a string of words, you need to find the highest scoring word.Each letter of
# a word scores points according to its position in the alphabet

def high(x):
    words = x.split(' ')
    return max(words, key=lambda word: sum(ord(char) - 96 for char in word))
