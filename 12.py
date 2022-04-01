n=input('輸入一整數序列為：').split(' ')
aa={}
c=0
d=0
for i in range(0,len(n)):
    cc={n[i]:n.count(n[i])}
    aa.update(cc)
for a,b in aa.items():
    if b>c and b>(len(n)//2):
        c=b
        d=a
if d==0:
    d='no'
print('過半元素：',d)
