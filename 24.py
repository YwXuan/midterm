# aa=[[60,50,30],[100,10,90],[80,40,20]]
aa=[[],[],[]]
# cc=[60,50,30,100,10,90,80,40,20]
cc=[]
c=int(input('請輸入字串大小'))
# c=3
for i in range(c):
    bb=input('').split(' ')
    for s in range(c):
        aa[i].insert(s,int(bb[s]))
    for n in range(c):
        cc.append(int(bb[n]))
cc.sort(reverse=True)
a=cc[0]+cc[1]+cc[2]
print('最大值:',a)
print('位置為',end='')
for s in range(3):
    if aa[s].count(cc[0])>0:
        print('(%s,%s)'%(s+1,aa[s].index(cc[0])+1),end=',')
    if aa[s].count(cc[1])>0:
        print('(%s,%s)'%(s+1,aa[s].index(cc[1])+1),end=',')
    if aa[s].count(cc[2])>0:
        print('(%s,%s)'%(s+1,aa[s].index(cc[2])+1),end='')
        
