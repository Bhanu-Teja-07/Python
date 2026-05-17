#print even numbers from 20-40
for i in range(20,41):
    if i%2==0:
        print(i,end=" ")
    else:
        continue
print()
#method 2
print("Method 2")
for i in range(20,41,2):
    print(i,end=" ")
print()
#print numbers 1-100
for i in range(1,101):
    print(i,end=" ")
print()
    
#print sum of n natural numbers
n=int(input())
sum=0
for i in range(n+1):
    sum+=i
print(sum)

#print the sum of inetgers from n to m
n=int(input())
m=int(input())
sum=0
for i in range(n,m+1,):
    if i%2==0:
        sum=sum+i
print(sum)