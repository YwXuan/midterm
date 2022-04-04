m=int(input('輸入月份'))
d=int(input('輸入日期'))
s=(m*2|d)%3
if s==0:
    print('普通')
elif s==1:
    print('吉')
elif s==2:
    print('大吉')
elif m>12 or d<1 or m<1 or d>31:
    print('輸入錯誤')