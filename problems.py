#palindrome
n=int(input())
a=n
sum = 0
while (n>0):
    l = n%10
    sum = (sum * 10) + l
    n=n//10
return (sum==a) #true or false

#reversethenumber
n = 123456
r = 0
while (n>0):
    l = n % 10
    r = (r*10) + l
    n = n // 10
print(r)

#factorial
n = int(input())
f = 1
for i in range(1,n+1):
    f = f * i
print(f)

#prime_number
n = int(input("n "))
for i in range(2, n + 1):
    f = 0
    for j in range(2, i):
        if i % j == 0:
            f = f + 1
    if f == 0:
        print(i,end=" ")
print("")

