#Michael Crozier hw3 decision tree

from random import shuffle
import math

#hard codes set of 25 example cases, there are 5 successful cases and 20 not successful ones
examples = [[1,1,0,0,1,0,0],[1,1,0,0,1,1,0],[1,1,0,0,1,1,1],[1,1,0,1,1,0,0],[1,1,0,1,0,0,0],[0,0,0,0,0,0,0],[0,0,0,1,0,0,0],[0,0,0,2,0,0,0],[0,1,0,2,1,1,1],[0,1,0,2,0,1,1],[0,1,0,2,0,0,0],[0,1,1,2,1,1,1],[0,1,1,1,1,0,1],[0,0,1,1,0,1,0],[0,0,1,0,1,0,1],[0,1,1,1,1,1,0],[0,0,0,0,1,0,0],[0,1,0,1,1,1,0],[0,1,0,1,0,0,1],[0,1,0,1,0,1,0],[0,1,1,0,1,0,0],[0,1,1,0,0,0,0],[0,1,1,0,1,1,1],[0,1,1,0,1,1,0],[0,1,1,0,0,1,0]]

#six attributes
attributes = [1,2,3,4,5,6]
attributeNames = ["Like it?","Done Before?","Panels?","REALLY good?","Take a long time?","Colour?"]
#eventual decision 'tree' Not very user friendly as it just lists the choices and leaf 'yes' and 'no's
#going down the left side node first and traveling back up once it reaches a leaf.
nodesAndLeaves = []

#get a random sample of 20 to build the tree.
shuffle(examples)
smallerList = []
for i in range(0, 20):
  smallerList.append(examples[i])

#get the other 5 or the test set
testList = []
for i in range(20, 25):
  testList.append(examples[i])

#get the entropy of a set given so many that say yes to an option, and so many that say no to
#an option. Only used for the parent initial entropy where a and b are a no and yes final
#answer respectively
def monoEntropy(a, b):
  probA = a/(a+b)
  probB = b/(a+b)

  if (probA != 0):
    probA = -(probA)*math.log(probA,2)
  if (probA != 0):
    probB = -(probB)*math.log(probB,2)

  entropy = probA + probB
  return entropy

#entropy with two sets
def binaryEntropy(a1, b1, a2, b2):
  if ((a1 == 0 and b1 == 0) or (a2 == 0 and b2 == 0)):
    #the decision made no difference, so the entropy can just be 1
    #since the parent entropy minus 1 will be negative, and lose the max comparison
    return 1
  weightOne = (a1+b1)/(a1+b1+a2+b2)
  weightTwo = (a2+b2)/(a1+b1+a2+b2)

  probOneA = a1/(a1+b1)
  probOneB = b1/(a1+b1)
  probTwoA = a2/(a2+b2)
  probTwoB = b2/(a2+b2)

  if (probOneA != 0):
    probOneA = -(probOneA)*math.log(probOneA,2)
  if (probOneB != 0):
    probOneB = -(probOneB)*math.log(probOneB,2)
  if (probTwoA != 0):
    probTwoA = -(probTwoA)*math.log(probTwoA,2)
  if (probTwoB != 0):
    probTwoB = -(probTwoB)*math.log(probTwoB,2)

  entropyOne = probOneA + probOneB
  entropyTwo = probTwoA + probTwoB
  entropy    = weightOne*entropyOne + weightTwo*entropyTwo
  return entropy

#entropy with three sets
def tertiaryEntropy(a1, b1, a2, b2, a3, b3):
  if ((a1 == 0 and b1 == 0) or (a2 == 0 and b2 == 0) or (a3 == 0 and b3 == 0)):
    #same as binary entropy
    return 1
  weightOne   = (a1+b1)/(a1+b1+a2+b2+a3+b3)
  weightTwo   = (a2+b2)/(a1+b1+a2+b2+a3+b3)
  weightThree = (a3+b3)/(a1+b1+a2+b2+a3+b3)

  probOneA   = a1/(a1+b1)
  probOneB   = b1/(a1+b1)
  probTwoA   = a2/(a2+b2)
  probTwoB   = b2/(a2+b2)
  probThreeA = a3/(a3+b3)
  probThreeB = b3/(a3+b3)

  if (probOneA != 0):
    probOneA = -(probOneA)*math.log(probOneA,2)
  if (probOneB != 0):
    probOneB = -(probOneB)*math.log(probOneB,2)
  if (probTwoA != 0):
    probTwoA = -(probTwoA)*math.log(probTwoA,2)
  if (probTwoB != 0):
    probTwoB = -(probTwoB)*math.log(probTwoB,2)
  if (probThreeA != 0):
    probThreeA = -(probThreeA)*math.log(probThreeA,2)
  if (probThreeB != 0):
    probThreeB = -(probThreeBA)*math.log(probThreeB,2)

  entropyOne   = probOneA + probOneB
  entropyTwo   = probTwoA + probTwoB
  entropyThree = probThreeA + probThreeB
  entropy      = weightOne*entropyOne + weightTwo*entropyTwo + weightThree*entropyThree
  return entropy

#Builds the entrie decision tree by comparing the current 'node's' entropy with the potential
#entropy of sub sets by looping through all the attributes. The attribute that gives the best
#information gain is set to be the next decision, and the function is called again recursively
#going down the left side, and then the right doing the same comparison as above, but with
#fewer available options each time because the last ones are already taken. If the current set
#of cases are all 'yes' or all 'no' then it becomes a leaf 'node' with that value and returns.
#If there is a case where there are no more attributes to look at, and there is still not a 
#consensus between cases, then it sets that 'node' to a leaf with a majority rule vote on what
#the value is. If it is a tie, then it is 'yes'.
def buildDecisionTree(cases):
  print("THE START BOYO")
  print(nodesAndLeaves)
  print(cases)
  a = 0
  b = 0
  for i in cases:
    if (i[0] == 0):
      a += 1
    else:
      b += 1
  if (a == 0):
    nodesAndLeaves.append("Yes")
    print(nodesAndLeaves)
    return 0
  if (b == 0):
    nodesAndLeaves.append("No")
    print(nodesAndLeaves)
    return 1
  parentEntropy = monoEntropy(a,b)
  maxInformationChange = 0
  bestAttribute = 0
  bestOne = []
  bestTwo = []
  bestThree = []
  for i in attributes:
    splitOne = []
    splitOneA = 0
    splitOneB = 0
    splitTwo = []
    splitTwoA = 0
    splitTwoB = 0
    if (i == 3):
      splitThree = []
      splitThreeA = 0
      splitThreeB = 0
      for j in cases:
        if (j[i] == 0):
          splitOne.append(j)
          if (j[0] == 0):
            splitOneA += 1
          else:
            splitOneB += 1
        elif (j[i] == 1):
          splitTwo.append(j)
          if (j[0] == 0):
            splitTwoA += 1
          else:
            splitTwoB += 1
        else:
          splitThree.append(j)
          if (j[0] == 0):
            splitThreeA += 1
          else:
            splitThreeB += 1
      entropy = tertiaryEntropy(splitOneA, splitOneB, splitTwoA, splitTwoB, splitThreeA, splitThreeB)
    else:
      for j in cases:
        if (j[i] == 0):
          splitOne.append(j)
          if (j[0] == 0):
            splitOneA += 1
          else:
            splitOneB += 1
        else:
          splitTwo.append(j)
          if (j[0] == 0):
            splitTwoA += 1
          else:
            splitTwoB += 1
      entropy = binaryEntropy(splitOneA, splitOneB, splitTwoA, splitTwoB)
    informationChange = parentEntropy - entropy
    if (informationChange > maxInformationChange):
      maxInformationChange = informationChange
      bestAttribute = i
      bestOne = splitOne
      bestTwo = splitTwo
      if (bestAttribute == 3):
        bestThree = splitThree
  print(bestAttribute)
  print(attributes)
  if (bestAttribute == 3):
    nodesAndLeaves.append(attributeNames[bestAttribute-1])
    attributes.remove(bestAttribute)

    buildDecisionTree(bestOne)
    buildDecisionTree(bestTwo)
    buildDecisionTree(bestThree)
  elif (bestAttribute == 0):
    if (a > b):
      nodesAndLeaves.append("No")
    else:
      nodesAndLeaves.append("Yes")
  else:
    nodesAndLeaves.append(attributeNames[bestAttribute-1])
    attributes.remove(bestAttribute)

    buildDecisionTree(bestOne)
    buildDecisionTree(bestTwo)
  return 1

#build the tree and print out the test list for manual testing
buildDecisionTree(smallerList)

print(testList)
