def top_3_words(intext: str):
  valids = list(map(chr, range(97, 123))) + ['\'']
  words = {}
  for z in intext.split(' '):
    x = ''
    for c in z.lower():
      if c in valids:
        x = x + c

    if len(x) > 0:
      y = words.get(x, 0)
      words[x] = y + 1

  out_words = sorted(words.items(), key=lambda x:x[1], reverse=True)[0:3]
  out_arr=[]
  for x in out_words:
    out_arr.append(x[0])
  return(out_arr) 

test_str = "'"
print(top_3_words(test_str))
