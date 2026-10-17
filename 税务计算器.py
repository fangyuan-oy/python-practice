salary = input()                   # salary 应发工资薪金所得
five_one_insurance_fund = input()  # five_one_insurance_fund  五险一金
exemption = input()                # exemption 个税免征额
try:
    a=float(salary)
    b=float(five_one_insurance_fund)
    c=float(exemption)
    d=a-b-c
    if a<=0:
        print("error")
    else:
        if d<=0:
            e=0
        elif d<=3000:
            e=d*0.03-0
        elif 3000<d<=12000:
            e=d*0.10-210
        elif 12000 <d<=25000:
            e=d*0.20-1410
        elif 25000<d<=35000:
            e=d*0.25-2660
        elif 35000<d<=55000:
            e=d*0.30-4410
        elif 55000<d<=80000:
            e=d*0.35-7160
        else:
            e=d*0.45-15160
        f=a-b-e
        print(f"应缴税款{e:.2f}元，实发工资{f:.2f}元。")
except ValueError:
    print("error")
