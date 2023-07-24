# 추억 점수
from collections import defaultdict


def solution(name, yearning, photo):
    result = []

    score_dict = defaultdict(int)
    for a, b in zip(name, yearning):  # 이름:스코어 딕셔너리
        score_dict[a] = b

    for case in photo:
        tmp = 0  # 케이스별로 점수 초기화
        for idx in range(len(case)):
            # defaultdict 사용으로 이름이 없으면 자동으로 0으로 초기화되어 점수 상승 없음
            tmp += score_dict[case[idx]]
        result.append(tmp)

    return result