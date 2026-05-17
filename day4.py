#find if the number is positive even, negative even or positive odd and negative odd

num=int(input())
if num>=0 and num%2==0:
    print("positive even")
elif num<0 and num%2==0:
    print("negative even")
elif num>=0 and num%2!=0:
    print("positive odd")
else:
    print("negative odd")

#find the greatest of three numbers
a,b,c=map(int,input().split())
if a>b and a>c:
    print("a is greatest")
elif b>a and b>c:
    print("b is greatest")
else:
    print("c is greatest")