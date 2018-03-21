import sys
import random

answer = random.randrange(0,9)

guess = None

while(guess != answer): # 可能會是 True 也有可能會是 False
  sys.stdout.write("guess the number: ")
  sys.stdout.flush()
  guess = int(sys.stdin.readline())

print("你猜中了！")
