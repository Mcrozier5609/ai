#Michael Crozier HW4 Schelling neighborhood

import random

neighborhood = [0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]

random.shuffle(neighborhood)
unhappies = 1
count = 1

def checkSatisfaction(i):
  buddies = 0
  dissatisfied = 0
  if (neighborhood[i] != 0):
    if (i == 0):
      if (neighborhood[58] == neighborhood[i]):
        buddies += 1
      if (neighborhood[59] == neighborhood[i]):
        buddies += 1
      if (neighborhood[i+1] == neighborhood[i]):
        buddies += 1
      if (neighborhood[i+2] == neighborhood[i]):
        buddies += 1
    if (i == 1):
      if (neighborhood[59] == neighborhood[i]):
        buddies += 1
      if (neighborhood[i-1] == neighborhood[i]):
        buddies += 1
      if (neighborhood[i+1] == neighborhood[i]):
        buddies += 1
      if (neighborhood[i+2] == neighborhood[i]):
        buddies += 1
    if (i == 58):
      if (neighborhood[i-2] == neighborhood[i]):
        buddies += 1
      if (neighborhood[i-1] == neighborhood[i]):
        buddies += 1
      if (neighborhood[i+1] == neighborhood[i]):
        buddies += 1
      if (neighborhood[0] == neighborhood[i]):
        buddies += 1
    if (i == 59):
      if (neighborhood[i-2] == neighborhood[i]):
        buddies += 1
      if (neighborhood[i-1] == neighborhood[i]):
        buddies += 1
      if (neighborhood[0] == neighborhood[i]):
        buddies += 1
      if (neighborhood[1] == neighborhood[i]):
        buddies += 1
    if (i > 1 and i < 58):
      if (neighborhood[i-2] == neighborhood[i]):
        buddies += 1
      if (neighborhood[i-1] == neighborhood[i]):
        buddies += 1
      if (neighborhood[i+1] == neighborhood[i]):
        buddies += 1
      if (neighborhood[i+2] == neighborhood[i]):
        buddies += 1
    if (buddies < 2):
      dissatisfied += 1
    return dissatisfied

while (unhappies != 0 and count < 401):
  unhappies = 0
  for i in range(0,60):
    if (checkSatisfaction(i)):
      unhappies += 1
    
  if (unhappies > 0):
    check = 1
    r1 = 0
    r1 = 0
    while (check == 1):
      unpleasents = 0
      r1 = random.randint(0,59)
      if (neighborhood[r1] != 0):
        unpleasents = checkSatisfaction(r1)
        if (unpleasents > 0):
          check = 0
    
    check = 1
    while (check == 1):
      r2 = random.randint(0,59)
      if (neighborhood[r2] == 0):
        check = 0
    neighborhood[r2] = neighborhood[r1]
    neighborhood[r1] = 0

  if (count%20 == 0 or unhappies == 0):
    print(count)
    print(neighborhood)
  count += 1
