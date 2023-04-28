A ,B = map(int, input().split())

if A == 0:
    if B >= 45:
        print(0, B - 45)
    else :
        print(23, 60 - (45 - B)) 
else :
    if B >= 45:
        print(A, B - 45)
    else :
        print(A-1, 60 - (45 - B))