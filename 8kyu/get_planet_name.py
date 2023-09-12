""" The function is not returning the correct values. Can you figure out why?
 This is a debugging exercise. The target error is that the code originally
 gives "switch id:" instead of "match id:" (line 8). A secondary non-fatal issue 
 is the variable name 'id' which clashes with the built-in 'id()' function
"""


def get_planet_name(id):
    # This doesn't work; Fix it!
    name = ""
    match id:
        case 1: name = "Mercury"
        case 2: name = "Venus"
        case 3: name = "Earth"
        case 4: name = "Mars"
        case 5: name = "Jupiter"
        case 6: name = "Saturn"
        case 7: name = "Uranus"
        case 8: name = "Neptune"
    return name
