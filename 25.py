n=input('請輸入考試次數及學生數:').split(' ')
per=input('請輸入'+str(n[0])+'次考試所占的比率').split(' ')
sum=0
for i in range(0,int(n[1])):
    stu = input('輸入'+'第'+str(i+1)+'位的'+n[0]+'次成績').split(' ')
    for s in range(0,int(n[0])):
        sum=sum+int(stu[s])*float(per[s])
sum=sum/int(n[1])
print('全班的總平均值為:%.2f'%(sum))


