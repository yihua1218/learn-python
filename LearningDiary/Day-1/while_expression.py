import sys
import random

answer = random.randrange(0,9)

while(True):
  sys.stdout.write("A: ")
  sys.stdout.flush()
  a = int(sys.stdin.readline())
  sys.stdout.write("B: ")
  sys.stdout.flush()
  b = int(sys.stdin.readline())
  print("A == B:", a == b)
  if (a == b and a == 99):
    break

