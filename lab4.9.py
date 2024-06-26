#หาค่าBMI
def BMI(k,h):
    a = k/(h**2)
    print("all: %.2f" % a)
    return a

def re(a):
    if a < 18.5:
        print("ผอม")
    
    elif a >= 18.5 and a < 23:
        print("ปกติ")
    
    elif a >= 23 and a < 25:
        print("ท้วม")
    
    elif a >= 25 and a < 30:
        print("อ้วน")
    
    else: print("อ้วนมาก")

x = float(input("ใส่น้ำหนักกิโลกรัม: "))
y = float(input("ใส่สูงเเบบเมตร: "))
re(BMI(x,y))

