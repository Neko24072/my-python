print("คะแนนสอบ")
x = float(input("ใส่คะแนนสอบ: "))
if x >= 80 and x <= 100:
    print("เกรดA")
elif x >= 70 and x < 80:
    print("เกรดB")
elif x >= 60 and x < 70:
    print("เกรดC")
elif x >= 50 and x < 60:
    print("เกรดD")
elif x < 50 and x >= 0:
    print("เกรดF")
else:
    print("กรุณาป้อนคะแนนใหม่ให้ถูกต้อง")
