a = int(input("ใส่จำนวนรอบ: "))
c = 0
for i in range(a):
    b = int(input("ใส่ตัวเลข: "))
    c+=b
    print("All %d: " % (i+1) + str(c))