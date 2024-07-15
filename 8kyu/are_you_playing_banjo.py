# Create a function which answers the question "Are you playing banjo?".
# If your name starts with the letter "R" or lower case "r", you are playing banjo!

def are_you_playing_banjo(name):
    name += " plays banjo" if name.lower().startswith("r") else " does not play banjo"
    return name
