Chicken = int(input())
Coke, Beer = map(int, input().split())
Eat = Coke//2 + Beer

if Chicken >= Eat :
    print(Eat)
else :
    print(Chicken)