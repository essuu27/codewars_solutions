# Return a list of possible combinations from the input string and
# the adjacent keys on a keypad

from itertools import product

ADJS = {'0': '08', '1': '124', '2': '1235', '3': '236', '4': '1457',
        '5': '24568', '6': '3569', '7': '478', '8': '05789', '9': '689'}

def get_pins(observed):

    adj_key = [ADJS[i] for i in observed]
    return [''.join(combo) for combo in product(*adj_key)]
