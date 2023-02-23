while True:
    str = input()
    stack = []
    if str == '.':
        break
    else:
        for i in str:
            if i in ['(', '[']:
                stack.append(i)
            elif i == ')':
                if stack:
                    check = stack.pop()
                    if check == '(':
                        pass
                    else:
                        print('no')
                        break
                else:
                    print('no')
                    break
            elif i == ']':
                if stack:
                    check = stack.pop()
                    if check == '[':
                        pass
                    else:
                        print('no')
                        break
                else:
                    print('no')
                    break
            else:
                pass
        else:
            if len(stack) == 0:
                print('yes')
            else:
                print('no')
