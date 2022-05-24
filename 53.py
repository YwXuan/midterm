
n=int(input('請輸入n值:'))
data={}
for i in range(n):
    a=input('請輸入姓名:')
    b=input('請輸入電子郵件:')
    data[a]=b
s=input('請輸入要查詢電子郵件的姓名:')
print(s+'電子郵件帳號為'+data.get(s,'不存在'))