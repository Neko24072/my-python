print("หาค่าBMI")

x = float(input("ใส่น้ำหนักแบบกิโลกรัม: "))

y = float(input("ใส่สูงแบบเซนติเมตร: "))

z = x/(y/100*y/100)

print("ค่าBMI %.2f" %z)

if z < 18.5:
    print("ผอม")
    
elif z >= 18.5 and z < 23:
    print("ปกติ")
    
elif z >= 23 and z < 25:
    print("ท้วม")
    
elif z >= 25 and z < 30:
    print("อ้วน")
    
else: print("อ้วนมาก")


