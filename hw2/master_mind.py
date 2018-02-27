#Michael Crozier Master Mind Game
from random import *

combos = []
colors = ['R','B','O','W']
def setAllCombos():
  for i in colors:
    for j in colors:
      for k in colors:
        combos.append(i+j+k)

def getAnswer():
  answer = input("X's and O's?")
  return answer

def changeTurns():
  playing = 1
  combo = ''
  answer = ''
  while (playing == 1):
    combo = guess()
    answer = getAnswer()
    playing = narrowDown(combo, answer)
    if (len(combos) == 1):
      playing = 0
      combo = combos[0]
  print ('The answer is ' + combo)

def guess():
  r = randint(0,len(combos)-1)
  print(combos[r])
  return combos.pop(r)

def narrowDown(combo, answer):
  a = combo[0]
  b = combo[1]
  c = combo[2]
  if (answer == ''):
    i = 0
    while (i < len(combos)):
      if ((a in combos[i]) or (b in combos[i]) or (c in combos[i])):
        del(combos[i])
      else:
        i += 1
    return 1
  elif (answer == 'o'):
    if (a != b and a != c and b != c):
      i = 0
      while (i < len(combos)):
        if (((a in combos[i] and a not in combos[i][0]) and
            (b not in combos[i]) and (c not in combos[i])) or
            ((b in combos[i] and b not in combos[i][1]) and
            (a not in combos[i]) and (c not in combos[i])) or
            ((c in combos[i] and c not in combos[i][2]) and
            (a not in combos[i]) and (b not in combos[i]))):
          i += 1
        else:
          del(combos[i])
    elif (a == b and a != c):
      i = 0
      while (i < len(combos)):
        if ((a not in combos[i] and c in combos[i] and c not in combos[i][2]) or
            (a not in combos[i][0] and a not in combos[i][1] and a in combos[i][2] and
             c not in combos[i])):
          i += 1
        else:
          del(combos[i])
    elif (a == c and a != b):
      i = 0
      while (i < len(combos)):
        if ((a not in combos[i] and b in combos[i] and b not in combos[i][1]) or
            (a not in combos[i][0] and a not in combos[i][2] and a in combos[i][1] and
             b not in combos[i])):
          i += 1
        else:
          del(combos[i])
    elif (b == c and a != b):
      i = 0
      while (i < len(combos)):
        if ((b not in combos[i] and a in combos[i] and a not in combos[i][0]) or
            (b not in combos[i][1] and b not in combos[i][2] and b in combos[i][0] and
             a not in combos[i])):
          i += 1
        else:
          del(combos[i])
    return 1
  elif (answer == 'x'):
    i = 0
    while (i < len(combos)):
      if ((a in combos[i][0]) and not (b in combos[i][1] and c in combos[i][2]) or
          (b in combos[i][1]) and not (a in combos[i][1] and c in combos[i][2]) or
          (c in combos[i][2]) and not (a in combos[i][1] and b in combos[i][2])):
         i += 1
      else:
        del(combos[i])
    return 1
  elif (answer == 'xx'):
    i = 0
    while (i < len(combos)):
      if ((a in combos[i][0] and b in combos[i][1] and c not in combos[i][2]) or
          (a not in combos[i][0] and b in combos[i][1] and c in combos[i][2]) or
          (a in combos[i][0] and b not in combos[i][1] and c in combos[i][2])):
         i += 1
      else:
        del(combos[i])
    return 1
  elif (answer == 'oo'):
    if (a != b and a != c and b != c):
      i = 0
      while (i < len(combos)):
        if (((a in combos[i] and a not in combos[i][0]) and 
             (b in combos[i] and b not in combos[i][1]) and c not in combos[i]) or
            ((b in combos[i] and b not in combos[i][1]) and
             (c in combos[i] and c not in combos[i][2]) and a not in combos[i]) or
            ((a in combos[i] and a not in combos[i][0]) and
             (c in combos[i] and c not in combos[i][2]) and b not in combos[i])):
           i += 1
        else:
          del(combos[i])
    elif (a == b and a != c):
      i = 0
      while (i < len(combos)):
        if ((a in combos[i] and a not in combos[i][0] and a not in combos[i][1]) and
            (c in combos[i] and c not in combos[i][2])):
           i += 1
        else:
          del(combos[i])
    elif (a == c and a != b):
      i = 0
      while (i < len(combos)):
        if ((a in combos[i] and a not in combos[i][0] and a not in combos[i][2]) and
            (b in combos[i] and b not in combos[i][1])):
           i += 1
        else:
          del(combos[i])
    elif (b == c and a != b):
      i = 0
      while (i < len(combos)):
        if ((b in combos[i] and b not in combos[i][1] and b not in combos[i][2]) and
            (a in combos[i] and a not in combos[i][0])):
           i += 1
        else:
          del(combos[i])
    return 1
  elif (answer == 'xo' or answer == 'ox'):
    if (a != b and a != c and b != c):
      i = 0
      while (i < len(combos)):
        if ((a in combos[i][0] and
           ((b in combos[i] and b not in combos[i][1] and c not in combos[i]) or
            (c in combos[i] and c not in combos[i][2] and b not in combos[i]))) or
            (b in combos[i][1] and
           ((a in combos[i] and a not in combos[i][0] and c not in combos[i]) or
            (c in combos[i] and c not in combos[i][2] and a not in combos[i]))) or
            (c in combos[i][2] and
           ((a in combos[i] and a not in combos[i][0] and b not in combos[i]) or
            (b in combos[i] and b not in combos[i][1] and a not in combos[i])))):
           i += 1
        else:
          del(combos[i])
    elif (a == b and a != c):
      i = 0
      while (i < len(combos)):
        if ((a in combos[i][0] and a not in combos[i][1] and
             b in combos[i][2] and b not in combos[i][1] and c not in combos[i]) or
            (a in combos[i][0] and a not in combos[i][1] and
             c in combos[i][1] and c not in combos[i][2] and b not in combos[i]) or
            (b in combos[i][1] and b not in combos[i][0] and
             a in combos[i][2] and a not in combos[i][0] and c not in combos[i]) or
            (b in combos[i][1] and b not in combos[i][0] and
             c in combos[i][0] and c not in combos[i][2])):
           i += 1
        else:
          del(combos[i])
    elif (a == c and a != b):
      i = 0
      while (i < len(combos)):
        if ((a in combos[i][0] and a not in combos[i][2] and
             b in combos[i][2] and b not in combos[i][1] and c not in combos[i]) or
            (a in combos[i][0] and a not in combos[i][2] and
             c in combos[i][1] and c not in combos[i][2] and b not in combos[i]) or
            (c in combos[i][2] and c not in combos[i][1] and
             b in combos[i][0] and b not in combos[i][1] and a not in combos[i]) or
            (c in combos[i][2] and c not in combos[i][1] and
             a in combos[i][1] and a not in combos[i][0])):
           i += 1
        else:
          del(combos[i])
    elif (b == c and a != b):
      i = 0
      while (i < len(combos)):
        if ((b in combos[i][1] and b not in combos[i][2] and
             c in combos[i][0] and c not in combos[i][2] and a not in combos[i]) or
            (b in combos[i][1] and b not in combos[i][2] and
             a in combos[i][2] and a not in combos[i][0] and c not in combos[i]) or
            (c in combos[i][2] and c not in combos[i][1] and
             b in combos[i][0] and b not in combos[i][1] and a not in combos[i]) or
            (c in combos[i][2] and c not in combos[i][1] and
             a in combos[i][1] and a not in combos[i][0])):
           i += 1
        else:
          del(combos[i])
    return 1
  elif (answer == 'oox' or answer == 'oxo' or answer == 'xoo'):
    i = 0
    while (i < len(combos)):
      if ((a in combos[i][0] and b in combos[i][2] and c in combos[i][1]) or
          (a in combos[i][2] and b in combos[i][1] and c in combos[i][0]) or
          (a in combos[i][1] and b in combos[i][0] and c in combos[i][2])):
         i += 1
      else:
        del(combos[i])
    return 1
  elif (answer == 'xxx'):
    return 0
  elif (answer == 'ooo'):
    i = 0
    while (i < len(combos)):
      if ((a in combos[i]) and (b in combos[i]) and (c in combos[i])):
         i += 1
      else:
        del(combos[i])
    return 1

setAllCombos()

changeTurns()
