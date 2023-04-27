A = int(input())
B = int(input())

B100 = int(B // 100)
B10 = (B - 100 * B100) // 10
B1 = B - 100 * B100 - 10 * B10

C1 = A * B1
C2 = A * B10
C3 = A * B100
C4 = C1 + C2 * 10 + C3 * 100

print(C1)
print(C2)
print(C3)
print(C4)