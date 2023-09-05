n, k = map(int, input().split())
num_list = list(map(int, input().split()))
result = []

for i in range(0, n-k+1):
    result.append(sum(num_list[i:i+k]))
    
print(max(result))