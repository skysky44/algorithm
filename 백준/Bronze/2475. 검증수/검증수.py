def verification(a,b,c,d,e):
    return (a**2+b**2+c**2+d**2+e**2)%10

a,b,c,d,e = map(int, input().split())
print(verification(a,b,c,d,e))