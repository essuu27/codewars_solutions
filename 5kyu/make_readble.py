# Write a function, which takes a non-negative integer (seconds) as input and 
# returns the time in a human-readable format (HH:MM:SS)

def make_readable(seconds):
    hrs, rem = divmod(seconds, 3600)
    mins, secs = divmod(rem, 60)
    outs=f"{hrs:02}:{mins:02}:{secs:02}"
    return(outs)
    