a=input('請輸入正整數:')
b=len(a)
c=0
for i in range(0,int(b)):
    for s in range(i+1,int(b)+1):
        d=int(a[i:s])
        if d%2 !=0:
            if d!= int(a):
                if d>int(c):
                    c=a[i:s]
if c==0:
    c='No prime found'
print('子字串中最大的質數值為:',c)
