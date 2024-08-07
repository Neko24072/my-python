def a(num):
    s = 0
    for i in range(num):
        p = int(input("รับราคาสินค้า%d: " % (i+1)))
        s += p
    return s

def Tax(s):
    vat = (s*7)/100
    return vat

def x(s):
    z = (((s+((s*7)/100))*5)/100)
    return z

def total(a,b,c):
    t = a + b - c
    return t

num = int(input("จำนวนสินค้า "))
s = a(num)
print("ราคารวม: %.2f" % s)
print("ภาษี7%%: %.2f" % Tax(s))
print("ส่วนลด5%%: %.2f" % x(s))
print("รวมเป็นเงิน: %.2f" % total(s, Tax(s), x(s)))