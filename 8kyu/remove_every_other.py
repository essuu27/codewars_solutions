# Take an array and remove every second element from the array.
def remove_every_other(my_list):
    x = 1
    while x < len(my_list):
        del my_list[x]
        x += 1

    return my_list
