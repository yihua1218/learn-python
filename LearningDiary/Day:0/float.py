import sys

sys.stdout.write("a: ")
sys.stdout.flush()
a = float(sys.stdin.readline())

sys.stdout.write("b: ")
sys.stdout.flush()
b = float(sys.stdin.readline())

print("\n")
print("\n")
print("a x b:", a * b)
