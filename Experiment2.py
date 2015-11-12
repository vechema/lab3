import sys

def smallest(list):
  if len(list) == 0:
    raise ValueError("Cannot call largest on empty list")
  min = sys.maxint # "smallest" possible int
  for index in range(len(list)):
    if (list[index] < min):
      min = list[index]
  return min