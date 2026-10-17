'''a=eval(input("请输入一个年份："))

if a%4==0 and a%100!=0:
    print("闰年")
elif a%400==0:
    print("闰年")
else:
    print("平年")'''


a=eval(input())
b=eval(input())
c=eval(input())

if a+b>c and a+c>b and c+b>a:
    print("构成")
else:
    print("不构成")
