# Write a function that will return the count of distinct case-insensitive alphabetic
# characters and numeric digits that occur more than once in the input string

def duplicate_count(text):
    textstr = text.lower()
    num = 0
    sort_str = set(sorted(textstr))
    for x in sort_str:
        if textstr.count(x) > 1:
            num += 1
    return(num)
