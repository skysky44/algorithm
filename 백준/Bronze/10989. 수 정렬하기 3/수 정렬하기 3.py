import sys  # 메모리 초과 발생
input = sys.stdin.readline
N = int(input())
nums = [0 for _ in range(10001)]  # 미리 리스트를 만들어 줌. 인덱스 활용
for _ in range(N):
    n = int(input())
    nums[n] += 1
for i in range(10001):
    if nums[i] != 0:
        for _ in range(nums[i]):
            print(i)
