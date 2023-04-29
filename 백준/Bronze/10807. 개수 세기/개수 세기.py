A = int(input())
nums = list(map(int, input().split()))  # 정수 리스트
v = int(input())  # 찾으려는 정수

count = 0  # 찾으려는 정수의 개수를 저장할 변수

for num in nums:
    if num == v:
        count += 1

print(count)  # 찾으려는 정수의 개수 출력