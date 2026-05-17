'''
n=int(input())
while(n<101):
    print(n,end=" ")
    n=n+1
#print even numbers 10-40
n=10
while(n<41):
    print(n,end=" ")
    n=n+2

#print odd numbers 1-50
n=1
while(n<51):
    print(n,end=" ")
    n=n+2

#print which is even or odd in a list
li=[1,2,3,4,5,6,7,8,9,10]
i=0
while(i<len(i)):
    if li[i]%2==0:
        print(li[i],"is even")
    else:
        print(li[i],"is odd")
    i=i+1

#print sum of even numbers upto n
n=int(input())
sum,i=0
while(i<=n):
    if i%2==0:
        sum+=i
    i=i+1
print(sum)

#find the sum of integers from n to m
n=int(input())
m=int(input())
sum=0
while(n<=m):
    if n%2==0:
        sum=sum+n
    n=n+1
print(sum)
'''
#method2
n,m=map(int,input().split())
sum=0
if n%2==0:
    while(n<=m):
        sum+=n
        n+=2
else:
    n+=1
    while(n<=m):
        sum+=n
        n+=2
        
print(sum)