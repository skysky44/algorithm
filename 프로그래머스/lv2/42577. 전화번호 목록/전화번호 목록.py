def solution(phone_book):
    result = True
    phone_book.sort()
    for i in range(len(phone_book)-1):
        if phone_book[i+1][0:len(phone_book[i])] == phone_book[i]:
            result = False
            return result
    return result