import sys
input = sys.stdin.readline

M, N = map(int, input().split())


array = [True for i in range(N+1)]  # 2부터 N까지 소수 판별 리스트
array[0] = False
array[1] = False
for i in range(2, int(N**(1/2))+1):
    if array[i] == True:  # i가 소수인 경우
        # i제외 i의 배수 지우기
        j = 2
        while i*j <= N:
            array[i*j] = False
            j += 1
# M부터 N까지 소수 출력
for i in range(M, N+1):
    if array[i]:
        print(i)
