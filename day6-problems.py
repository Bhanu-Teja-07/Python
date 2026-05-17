'''
#length of number
n=int(input())
while n>0:
    n=n//10
    count+=1
print(count)

#sum of digits in a number
n=int(input())
s=0
d=0
while n>0:
    d=n%10
    n=n//10
    s+=d
print(s)

#reverse of a number
num=int(input())
rev=0
rem=0
while num>0:
    rem=num%10
    rev=rev*10+rem
    num//=10
print(rev)

# palindrome or not
n=int(input())
temp=n
rem=0
rev=0
while n>0:
    rem=n%10
    rev=rev*10+rem
    n//=10
if rev==temp:
    print("palindrome")
else:
    print("not palindrome")

#armstrong number
n=int(input())
arm=0
rev=0
while n>0:
    rem=n%10
    arm+=(rem ** 3)
    n//=10
print(arm)
'''
#perfect number
n=int(input())
su=0
for i in range(1,n):
    if n%i==0:
        su+=i

if su==n:
    print("perfect number")
else:
    print("not perfect number")