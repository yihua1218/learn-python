import sys
import random

answer = random.randrange(0,9)

sys.stdout.write("guess the number: ")
sys.stdout.flush()
guess = int(sys.stdin.readline())

if (guess == answer):
  print("你猜中了！")
else:
  print("你沒猜中。答案是", answer)
