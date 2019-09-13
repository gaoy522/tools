def change(num,start):
    start=int(start)
    bin2=bin(int(num, start))
    oct8=oct(int(num, start))
    str10=str(int(num, start))
    hex16=hex(int(num, start))
    
    print("2进制为:"+bin2)
    print("8进制为:"+oct8)
    print("10进制为:"+str10)
    print("16进制为:"+hex16)

num=input("请输入数值:")
start=int(input("请输入原进制:"))
change(num,start)
