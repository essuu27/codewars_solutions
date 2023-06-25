# Implement the function which takes an array containing the names
# of people that like an item. 

def likes(names):
  y = len(names)
  outstr = " likes this" if (y < 2) else " like this"

  if y == 0:
    namestr = 'no one'
  elif y > 2:
    exlikers = names[2] if (y == 3) else f"{str(y - 2)} others"
    namestr = f"{names[0]}, {names[1]} and {exlikers}"
  else:
    namestr = names[0]
    if y == 2:
      namestr += f' and {names[1]}'
  namestr += outstr

  return(namestr)