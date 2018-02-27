#4 milk can problem Michael Crozier

#maxium for each can
max = (40, 40, 5, 4)
max40a = max[0]
max40b = max[1]
max5 = max[2]
max4 = max[3]

#visted states
visited = {}

#solution path
path = []

def get_all_states(state):
  # Let the 4 cans be called a,b,c,d
  a = state[0]
  b = state[1]
  c = state[2]
  d = state[3]
  #found solution
  if (c==2 and d==2):
      path.append(state)
      return True

  #if current state was visited before
  if ((a,b,c,d) in visited or (b,a,c,d) in visited):
      return False

  visited[(a,b,c,d)] = 1

  #empty can a
  if (a>0):
      #pour a into b
      if (a+b<=max40b):
          if (get_all_states((0,a+b,c,d))):
              path.append(state)
              return True
      else:
          if (get_all_states((a-(max40b-b), max40b, c, d))):
              path.append(state)
              return True
      #pour a into c
      if (a+c<=max5):
          if (get_all_states((0,b,a+c, d))):
              path.append(state)
              return True
      else:
          if (get_all_states((a-(max5-c), b, max5, d))):
              path.append(state)
              return True
      #pour a into d 
      if (a+d<=max4):
          if (get_all_states((0, b, c, a+d))):
              path.append(state)
              return True
      else:
          if (get_all_states((a-(max4-d), b, c, max4))):
              path.append(state)
              return True
  #empty can b
  if (b>0):
      #pour b into a
      if (a+b<=max40a):
          if (get_all_states((a+b, 0, c, d))):
              path.append(state)
              return True
      else:
          if (get_all_states((max40a, b-(max40a-a), c, d))):
              path.append(state)
              return True
      #pour b into c
      if (b+c<=max5):
          if (get_all_states((a, 0, b+c, d))):
              path.append(state)
              return True
      else:
          if (get_all_states((a, b-(max5-c), max5, d))):
              path.append(state)
              return True
      #pour b into d
      if (b+d<=max4):
          if (get_all_states((a, 0, c, b+d))):
              path.append(state)
              return True
      else:
          if (get_all_states((a, b-(max4-d), c, max4))):
              path.append(state)
              return True

  #empty can c
  if (c>0):
      #pour c into a
      if (a+c<=max40a):
          if (get_all_states((a+c, b, 0, d ))):
              path.append(state)
              return True
      else:
          if (get_all_states((max40a, b, c-(max40a-a), d))):
              path.append(state)
              return True
      #pour c into b
      if (b+c<=max40b):
          if (get_all_states((a, b+c, 0, d))):
              path.append(state)
              return True
      else:
          if (get_all_states((a, max40b, c-(max40b-b), d))):
              path.append(state)
              return True
      #pour c into d
      if (c+d<=max4):
          if (get_all_states((a, b, 0, c+d))):
              path.append(state)
              return True
      else:
          if (get_all_states((a, b, c-(max4-d), max4))):
              path.append(state)
              return True
   #empty can d
  if (d>0):
      #pour d into a
      if (a+d<=max40a):
          if (get_all_states((a+d, b, c, 0 ))):
              path.append(state)
              return True
      else:
          if (get_all_states((max40a, b, c, d-(max40a-a)))):
              path.append(state)
              return True
      #pour d into b
      if (b+d<=max40b):

          if (get_all_states((a, b+d, c, 0))):
              path.append(state)
              return True
      else:
          if (get_all_states((a, max40b, c, d-(max40b-b)))):
              path.append(state)
              return True
      #pour d into c
      if (c+d<=max5):
          if (get_all_states((a, b, c+d, 0))):
              path.append(state)
              return True
      else:
          if (get_all_states((a, b, max5, d-(max5-c)))):
              path.append(state)
              return True
  return False

initial_state = (40,40,0,0)
get_all_states(initial_state)
path.reverse()
j = 0;
for i in path:
  print("turn number:")
  print(j)
  print(i)
  j = j + 1
print("Total number of states:")
print(len(visited) + 1)
