#Michael Crozier HW4 Perceptron Training

import math
import random

inputValues = [1,1,1]
inputWeights = [1,1,1]
rate = 0.004
count = 0

for i in range(0,3):
  inputWeights[i] = random.uniform(-1.0, 1.0)

err = 0;
inputSum = 0
foundOutput = 0
correctOutput = 0

while count <= 8000:
  for i in range(0,3):
    inputValues[i] = random.randint(0,1)
    inputSum += inputValues[i]*inputWeights[i]
  inputSum += -1

  if (inputSum > 0):
    foundOutput = 1
  else:
    foundOutput = 0

  if (inputValues[0] == 1 and inputValues[2] == 1):
    correctOutput = 1
  else:
    correctOutput = 0

  err = correctOutput - foundOutput
  if (err != 0):
    sigmoidalPrime = (1/(1+math.exp(-inputSum)))*(1 - (1/(1+math.exp(-inputSum))))
    for i in range(0,3):
      inputWeights[i] = inputWeights[i] + (rate*err*sigmoidalPrime*inputValues[i])
  if (count%250 == 0):
    print("Sample Number: ", count)
    print("new weights: ", inputWeights)
  
  foundOutput = 0
  count += 1
  inputSum = 0

