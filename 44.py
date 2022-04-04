t=int(input('班級數量'))
v=[]
for i in range(0,t):
    a=int(input(i+1))
    v.append(a)
v.sort()
v.reverse()
print('購買數量:',v[0])
