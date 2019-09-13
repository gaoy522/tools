import base64
def encode1(string):
    ec = base64.b64encode(string.encode('utf-8'))
    print(str(ec,'utf-8'))
def decode1(key):
    dc = base64.b64decode(bytes(key,"utf-8").decode('utf-8'))
    print(str(dc,'utf-8'))

print("base64")
while(True):
    s=input("输入待加密/解密字符串:")
    base=input("加密输入1，解密输入2\n")
    
    try:
        if (base=="1"):
            encode1(s)
        elif(base=="2"):
            decode1(s)
    except:
        print("解密失败")
    print("######################")
