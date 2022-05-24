m={'1':72,'2':62,'3':82,'4':44,'5':60,'A':55,'B':68}
meal=list(input('請選擇主餐及升級的套餐'))
drink=input('是否升級大杯飲料')
chip=input('是否換成大薯')
money=0
for i in meal:
    money += m.get(i)
if drink=='是' or drink=='Y':
    money += 7
if chip=='是' or chip=='Y':
    money+=13

print('總共為{}元'.format(money))