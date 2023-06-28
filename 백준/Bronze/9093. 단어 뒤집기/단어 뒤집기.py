import sys

N = int(sys.stdin.readline())

for i in range(N):
  arr = list(sys.stdin.readline().split())
  arrN = len(arr)
  for i in range(arrN):
    arr[i] = arr[i][::-1]
  
  for i in range(arrN):
    print(arr[i] + ' ', end='')