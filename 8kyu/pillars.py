# A columnade is made of {num_pill} pillars. Each pillar is {width} cm wide
# and the distance between each pillar is {dist} metres. Return the total
# distance between the INTERNAL edges of the first and last pillar.

def pillars(num_pill, dist, width):
    if (num_pill > 1):
        return(((dist * 100) * (num_pill - 1)) + (width * (num_pill - 2)))
    else:
        return(0)
