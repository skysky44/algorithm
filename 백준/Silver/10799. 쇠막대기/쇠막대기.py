# 쇠막대기
bars = input()
# 레이저만 구분
bars = bars.replace('()', 'R')

stack = []
total_bar = 0
current_bar = 0
razer = 0


for i in bars:

    if i == 'R':
        razer += 1
        total_bar += current_bar

    elif i == '(':
        if len(stack) == 0:
            current_bar = 0
            razer = 0
        stack.append(i)
        total_bar += 1
        current_bar += 1
    elif i == ')':
        stack.pop()
        current_bar -= 1

print(total_bar)
