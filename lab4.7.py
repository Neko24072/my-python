#หาพท.สามเหลี่ยม 1/2*ฐาน*สูง
def Triangle(b, h):
    a = 1/2*b*h
    print("all: %.2f" % a)
    return a

x = float(input("ใส่ฐาน: "))
y = float(input("ใส่สูง: "))
print("all: %.2f" % Triangle(x,y))