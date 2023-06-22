"""
 Build a pyramid-shaped tower, as an array/list of strings, given a 
 positive integer number of floors. 
"""

def tower_builder(n_floors):
    floors=[]
    a = 0
    b = n_floors
    while a < b:
        s = '**'*a +'*'
        floors.append(s.center((b*2)-1,' '))
        a += 1
    return(floors)
