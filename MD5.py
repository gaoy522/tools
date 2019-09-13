import hashlib

def md5(string):
    h=hashlib.md5(string.encode("utf-8")).hexdigest()
    print('md5小32位:'+h)
    print('md5大32位:'+h.upper())

print("md5")
while(True):
    string=input("输入需要md5的值:")
    md5(string)
