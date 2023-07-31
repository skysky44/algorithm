# 암호 만들기
L, C = map(int, input().split())  # 암호 L개, C개 총 알파벳
strings = list(map(str, input().split()))
sorted_strs = sorted(strings)
vowel = ['a', 'e', 'i', 'o', 'u']
result = ''


def backtracking(result, start):
    vowel_cnt = 0
    if len(result) == L:
        for i in result:
            if i in vowel:
                vowel_cnt += 1
        if vowel_cnt > 0 and (len(result) - vowel_cnt > 1):
            print(result)
        return
    else:
        for i in range(start, C):
            if not result or (result[-1] < sorted_strs[i]):
                result = result + sorted_strs[i]
                backtracking(result, start+1)
                result = result[0:-1]


backtracking(result, 0)

