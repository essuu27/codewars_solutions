# Input an RGB value, given as decinals and return it in hexadecimal format

def rgb(r, g, b):
    rgbdec = (r, g, b)
    rgbout = ''
    for y in rgbdec:
        if y < 0:
            y = 0
        if y > 255:
            y = 255
        rgbout = rgbout + "{:02x}".format(y)

    return(rgbout.upper())