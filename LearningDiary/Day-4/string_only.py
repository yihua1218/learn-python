import sys

def input_string(a):
  try:
    int(a)
  except ValueError:
    print("win")
  else:
    print("string only")


sys.stdout.write("input text or number: ")
sys.stdout.flush()
guess = sys.stdin.readline()
input_string(guess)
