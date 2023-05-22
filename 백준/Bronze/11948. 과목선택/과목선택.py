num1=[]
num2=[]
sum_num=0

for i in range(4):
    n1=int(input(''))
    num1.append(n1)

for i in range(2):
    n2=int(input(''))
    num2.append(n2)

num1.remove(min(num1))

sum_num=sum(num1)+max(num2)
    
print(sum_num)

