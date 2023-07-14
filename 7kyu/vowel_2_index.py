# Take in a string and replaces all the vowels [a,e,i,o,u] with 
# their respective positions within that string.

def vowel_2_index(string):
    outstr = ''.join(
        str(i + 1) if j.lower() in ('a', 'e', 'i', 'o', 'u') else j
        for i, j in enumerate(string)
    )
    return(outstr)