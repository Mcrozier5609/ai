#Michael Crozier SIM game

used = {}
points = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

inputValid = 0
while (inputValid == 0):
  playerColor = input('Are you playing Red (R), or Blue (B)?:')
  if (playerColor != 'R' and playerColor != 'B'):
    print ('Invalid color, try again')
  else:
    inputValid = 1
if (playerColor == 'R'):
  computerColor = 'B'
else:
  computerColor = 'R'
print ('You are', playerColor)
print ('I am', computerColor)

def checkEnd(v1, v2, color):
  i = 0
  j = 0
  for i in points:
    if (v1 != points[j] and v2 != points[j]):
      if (((v1, points[j], color) in used and (v2, points[j], color) in used) or
          ((points[j], v1, color) in used and (points[j], v2, color) in used) or
          ((v1, points[j], color) in used and (points[j], v2, color) in used) or
          ((points[j], v1, color) in used and (v2, points[j], color) in used)):
        return 1
    j += 1
  return 0

def checkNeighbor(v1, v2, color):
  i = 0
  j = 0
  for i in points:
    if (v1 != points[j] and v2 != points[j]):
      if (((v1, points[j], color) in used or (v2, points[j], color) in used) or
          ((points[j], v1, color) in used or (points[j], v2, color) in used)):
        return 1
    j += 1
  return 0

def checkValid(v1, v2):
  if (v1 != v2 and (v1, v2, 'R') not in used and (v1, v2, 'B') not in used and
      (v2, v1, 'R') not in used and (v2, v1, 'B') not in used):
    return 1
  else:
      return 0

def startTurn():
  turn = 'R'
  end = 0
  while (end == 0):
    if (playerColor == turn):
      end = playerTurn()
      if (turn == 'R'):
        turn = 'B'
      else:
        turn = 'R'
    else:
      end = computerTurn()
      if (turn == 'R'):
        turn = 'B'
      else:
        turn = 'R'
  if(playerColor == turn):
    print('You won! You beat the computer!')
  else:
    print('You lost. The computer beat you!')

def playerTurn():
  print ('Player Turn')
  valid = 0
  while (valid == 0):
    edges = input('See used edges? (Y, N):')
    if(edges == 'Y' or edges == 'y'):
      printEdges()
    v1 = input('Select the first point(A-H):')
    v2 = input('Select the second point(A-H):')
    valid = checkValid(v1,v2)
    if (valid == 0):
      print ('Edge already in use, or invalid input. Try again.')
  used[(v1, v2, playerColor)] = 1
  return checkEnd(v1, v2, playerColor)

def computerTurn():
  print ('Computer Turn')
  v1 = ''
  v1meh = ''
  v1Lose = ''
  v2 = ''
  v2meh = ''
  v2Lose = ''
  i = 0
  j = 0
  for i in points:
    for j in points:
      if(checkValid(i,j)):
        v1Lose = i
        v2Lose = j
        if(checkEnd(i,j,computerColor) == 0):
          v1meh = i
          v2meh = j
          if(checkNeighbor(i,j,computerColor) == 0):
            v1 = i
            v2 = j
  if (v1 != '' and v2 != ''):
    used[(v1,v2,computerColor)] = 1
    print('v1')
  elif(v1meh != '' and v2meh != ''):
    v1 = v1meh
    v2 = v2meh
    print('meh')
    used[(v1,v2,computerColor)] = 1
  else:
    v1 = v1Lose
    v2 = v2Lose
    print('lose')
    used[(v1,v2,computerColor)] = 1
  print('('+v1+', '+v2+', '+computerColor+')')
  return checkEnd(v1, v2, computerColor)

def printEdges():
  i = 0
  for i in used:
    print(i)

startTurn()
