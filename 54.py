route=float(input('請輸入路程公里數(km)'))
money=75
if (route>1.5):
    b=route-1.5
    c=b//0.25
    money+=c*5
    if b-c*0.25!=0:
        money+=5
        
print('所需車資為:',int(money))
