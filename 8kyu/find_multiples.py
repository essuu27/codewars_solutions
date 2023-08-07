# Take a value, integer , and return a list of its multiples up to 
# another value, limit

def find_multiples(integer,limit):
    mults = []

    nom = integer
    while nom <= limit:
        mults.append(nom)
        nom += integer

    return(mults)
