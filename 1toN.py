import sys

sys.stdout.write("N: ")
sys.stdout.flush()
n = int(sys.stdin.readline())

for i in range(1,n+1):
  print(i)

print("\n")