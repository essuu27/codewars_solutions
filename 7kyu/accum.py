# Write a function that take a string input and reurns output in the following style:
# accum("abcd") -> "A-Bb-Ccc-Dddd"

def accum(s) -> str:
    outstr = ''
    for cnt, val in enumerate(s):
        outstr = f"{outstr}-{((val * (cnt+1)).capitalize())}"
    return (outstr[1:])

