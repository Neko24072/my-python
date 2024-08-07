def f(c):
    F = ((9/5)*c)+32
    return F

def k(c):
    K = c + 273.15
    return K

c = float(input("ใส่อุณหภูมิองศาC: "))
print("อุณหภูมิ %.2f องศาF" % f(c))
print("อุณหภูมิ %.2f องศาK" % k(c))