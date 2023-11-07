import sys

input = sys.stdin.readline


def find(a):
    if a == parent[a]:  # 자신이 루트노드면 자신을 반환
        return a
    parent[a] = find(parent[a])  # 루트노드를 찾음 (ex. 1의 루트가 1이고 3의 루트가 1이고 4의 루트가 3일 때: 4를 넣으면 3에 갔다가 1까지 감)
    # a의 부모를 find(parent[a])로 바꿔줌(3의 부모를 find(3의 루트노드)로 바꿔줌)
    return parent[a]


def union(a, b):
    a = find(a)
    b = find(b)
    # a , b의 루트노드를 찾아줌
    # 둘 중 작은 수를 큰 수의 루트 노드로 설정
    if b < a:
        parent[a] = b
    else:
        parent[b] = a


n = int(input())
m = int(input())
arr = []
parent = [i for i in range(n + 1)]
res = 0
for i in range(m):
    a, b, c = map(int, input().split())
    arr.append((c,a,b))

arr.sort(key=lambda x: x[0])
for c, a, b in arr:
    if find(a) != find(b):  # 루트가 같으면 사이클이 형성 되어서 안가도 됨
        union(a, b)
        res += c
print(res)

# 풀이 참고, 크루스칼 알고리즘, 최소 스패닝 트리
# 크루스칼 설명 : https://chanhuiseok.github.io/posts/algo-33/

# Union & Find 활용
# Disjoint Set (서로소 집합) 을 표현하는 자료구조
#서로 다른 두 집합을 병합하는 Union 연산, 집합 원소가 어떤 집합에 속해있는지 찾는 Find 연산을 지원 
