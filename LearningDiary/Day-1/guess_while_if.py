import sys
import random

answer = random.randrange(0,9)

result = False

while(result == False):
  sys.stdout.write("guess the number: ")
  sys.stdout.flush()
  guess = int(sys.stdin.readline())
  if (guess == answer):
    print("你猜中了！")
    result = True
  else:
    print("你沒猜中。")
    result = False
