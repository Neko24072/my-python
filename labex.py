def dee(a,z):
    f = a
    print("ปีที่ \t เงินต้น \t \t ดอกเบี้ย")
    for i in range(z):
        a *= 3/100
        #print("ดอกเบี้ย: %.2f" % a)
        f += a
        
        print("%d \t %.2f \t %.2f " % (i+1,f,a ))
        a = f
    return f
        
a = int(input("จำนวนเงินต้น: "))
z = int(input("ระยะเวลาที่ฝาก(ปี): "))
print("จำนวนเงินฝากทั้งหมด: %.2f" % dee(a,z))

#f = f+(f*3/100)
 #       print("จำนวนเงินได้: %.2f" % f)
  #      if(i==b):
   #         return f
     #   return f