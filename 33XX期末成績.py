chin = int(input('國文:'))
eng = int(input('英文:'))
math = int(input('微積分:'))
pe = int(input('體育:'))
py = int(input('程式設計:'))
sum = {chin:'國文',eng:'英文',math:'微積分',pe:'體育',py:'程式設計'}
sum1 = 0
for score in sum:
    sum1 += score
print('平均成績:%.2f'%(sum1/len(sum)))
aa=list(sum.keys())
bb=[]
for i in aa:
    bb.append(int(i))
bb.sort
ma=sum.get(aa[0])
print('最低分數:',sum.get(aa[0]),aa[0])
print('最高分數:',sum.get(aa[4]),aa[4])

