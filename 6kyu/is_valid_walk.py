# Given an list of steps ('n','s','e','w'), find the list that is 10 steps long and
# ends where you started.

def is_valid_walk(steps):
  if (steps.count('n') == steps.count('s')):
    if (steps.count('e') == steps.count('w')):
      if(len(steps) == 10):
        return True
  else:
    return False
  return False

print(is_valid_walk(['n','s','n','s','n','s','n','s','n','s']))
print(is_valid_walk(['w','e','w','e','w','e','w','e','w','e','w','e']))
print(is_valid_walk(['w']))
print(is_valid_walk(['n','n','n','s','n','s','n','s','n','s']))
