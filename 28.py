aa=[]
for i in range(2):
    a=input('{}'.format(i+1)).split(' ')
    for s in range(2):
        aa.append(float(a[s]))
print(round(aa[0],1),round(aa[2],1))
print(round(aa[1],1),round(aa[3],1))