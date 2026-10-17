total_amount=0.0
count=0
print("欢迎使用收银系统")

while True:
    user_input=input("请输入价格：(按q退出)")

    if user_input=="q":
        break

    try:
        money=float(user_input)
        total_amount+=money
        count+=1
        print(f"当前收入金额：{total_amount:.2f}元")

    except valueeError:
        print("输入非法，请重新输入：")

print(f"今日办理{count}笔业务，收入为{total_amount:.2f}元")
