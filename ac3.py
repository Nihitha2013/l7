print("enter marks of 3 subjects:")
m1=int(input())
m2=int(input())
m3=int(input())
t=m1+m2+m3
a=t/3

if a>81 and a<=100:
    print("grade A")

elif a<80 and a>=100:
    print("grade B")
elif a<50 and a>=35:
    print("grade C")
else:
    print ("fail")
