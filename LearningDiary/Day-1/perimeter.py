import sys
import math

def perimeter(d):
  return d * math.pi

def round_area(d):
  return ((d / 2) ** 2) * math.pi

sys.stdout.write("輸入直徑: ")
sys.stdout.flush()
diameter = float(sys.stdin.readline())

print("圓周長：", perimeter(diameter))
print("圓面積：", round_area(diameter))
