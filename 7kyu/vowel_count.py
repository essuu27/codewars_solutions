# Return the number/count of vowels in the given string.

def get_count(sentence):
    vowels='aeiou'
    cnt = 0
    for i in vowels:
        cnt += sentence.count(i)
    return(cnt)
    