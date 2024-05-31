my_arr = [5, 1, 3, 4, 1]
score = 0

counts = [my_arr.count(x) for x in range(6)]



"""
Three 1's => 1000 points
 Three 6's =>  600 points
 Three 5's =>  500 points
 Three 4's =>  400 points
 Three 3's =>  300 points
 Three 2's =>  200 points
 One   1   =>  100 points
 One   5   =>   50 point
"""