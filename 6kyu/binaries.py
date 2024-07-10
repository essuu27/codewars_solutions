# Encode a number into a reduced form of binary. Decode a reduced binary back
# into a base10 number

codes = ["10", "11", "0110", "0111", "001100", "001101", "001110",
         "001111", "00011000", "00011001"]


def code(number):
    bigstr = ''
    for i in str(number):
        y = str(bin(int(i)))[2:]
        z = ('0' * (len(y) - 1)) + '1'
        bigstr = bigstr + z + y
    return bigstr


def decode(number):
    outstr = ''
    while len(number) > 0:
        for c, v in enumerate(codes):
            if number.startswith(v):
                number = number.replace(v, '', 1)
                outstr += (str(c))
    return outstr
