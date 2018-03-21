import sys
import random

answer = random.randrange(0,9)

while(True):  # 條件永遠成立 True，迴圈永遠執行
  sys.stdout.write("guess the number: ")
  sys.stdout.flush()
  guess = int(sys.stdin.readline())
  if (guess == answer):
    break

print("你猜中了！")
