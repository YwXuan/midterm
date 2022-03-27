x = float(input('請輸入x值'))
y = float(input('請輸入y值'))
c= int(x**2+y**2)
if x>0 and y>0:
    print("在第一象限，距離原點為根號",c)
elif x<0 and y>0:
    print('在第二象限，距離原點為根號',c)
elif x<0 and y<0 :
    print('在第三象限象限，距離原點為根號',c)
elif x>0 and y<0:
    print('在第四象限象限，距離原點為根號',c)
elif x==0 and y<0:
    print('在y軸下半平面，距離原點為根號',c)
elif x==0 and y>0:
    print('在y軸上半平面，距離原點為根號',c)
elif y==0 and x>0:
    print('在x軸右半平面，距離原點為根號',c)
elif y==0 and x<00:
    print('在x軸左半平面，距離原點為根號',c)
elif y==0 and x==0:
    print('在原點上')
else:
    print('打錯喔喔')

    