import sys

sys.stdout.write("a: ")
sys.stdout.flush()
a = int(sys.stdin.readline())

sys.stdout.write("b: ")
sys.stdout.flush()
b = int(sys.stdin.readline())

print("\n")
print(a, "x", b)
print("\n")

# 外迴圈
for i in range(0,a):
  # 內迴圈
  # range(0, b)
  # 假設 b = 3
  # range(0, 3) => 0, 1, 2
  # range(x, y) 的意思是，產生從 x 開始的整數陣列，到小於 y 為止
  # range(5, 9) => 5, 6, 7, 8
  for j in range(0,b):
    # 在系統的標準輸出裝置，寫入 "*"
    # 預設的系統標準輸出裝置是終端機
    # sys 系統類別
    # stdout 標準輸出裝置
    # write 寫入
    sys.stdout.write("*")
  sys.stdout.write("\n")

sys.stdout.write("\n")

