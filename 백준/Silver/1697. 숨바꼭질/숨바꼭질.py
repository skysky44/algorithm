from collections import deque
import sys
input = sys.stdin.readline
n, k = map(int, input().split())  # n 수빈 k 동생 위치


# 방문한 위치를 기록
visited = [False] * 100001


def bfs(start, target):
    queue = deque([(start, 0)])  # 위치와 이동 횟수를 함께 큐에 저장
    visited[start] = True

    while queue:
        position, steps = queue.popleft()

        if position == target:
            return steps

        # 가능한 다음 위치들을 생성
        next_positions = [position - 1, position + 1, position * 2]

        for next_pos in next_positions:
            if 0 <= next_pos <= 100000 and not visited[next_pos]:
                visited[next_pos] = True
                queue.append((next_pos, steps + 1))


result = bfs(n, k)
print(result)