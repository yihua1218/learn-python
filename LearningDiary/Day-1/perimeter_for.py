import sys
import math

def perimeter(d):
  return d * math.pi

def round_area(d):
  # 
  # 
  # 
  ans = ((d / 2) ** 2) * math.pi
  return ans


sys.stdout.write("Input: ")
sys.stdout.flush()
n = int(sys.stdin.readline())

for i in range(1,n+1):
  print("直徑：", i)
  diameter = float(i)
  print("圓周長：", perimeter(diameter))
  print("圓面積：", round_area(diameter))
