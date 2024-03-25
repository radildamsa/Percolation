from random import randint

def generator():
  RandomNumbers = randint(10, 100)
  if RandomNumbers % 6 == 0 :
    return "";
  return RandomNumbers

