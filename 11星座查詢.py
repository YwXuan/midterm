md = input('請輸入月及日(用空格分開)')
b= md.split(' ')
m=int(b[0])
d=int(b[1])
if (m == 1) and (d>=1) and (d<=20):
    a='魔羯'
elif (m == 12) and (d>=22) and (d<=31):
    a='魔羯'
elif (m == 1) and (d>=21) and (d<=31):
    a='水瓶'
elif (m == 2) and (d>=1) and (d<=18):
    a='水瓶'
elif (m == 2) and (d>=19) and (d<=29):
    a='雙魚'
elif (m == 3) and (d>=1) and (d<=20):
    a='雙魚'
elif (m == 3) and (d>=21) and (d<=31):
    a='牡羊'
elif (m == 4) and (d>=1) and (d<=20):
    a='牡羊'
elif (m == 4) and (d>=21) and (d<=30):
    a='金牛'
elif (m == 5) and (d>=1) and (d<=21):
    a='金牛'
elif (m == 5) and (d>=22) and (d<=31):
    a='雙子'
elif (m == 6) and (d>=1) and (d<=21):
    a='雙子'
elif (m == 6) and (d>=22) and (d<=30):
    a='巨蟹'
elif (m == 7) and (d>=1) and (d<=22):
    a='巨蟹'
elif (m == 7) and (d>=23) and (d<=31):
    a='獅子'
elif (m == 8) and (d>=1) and (d<=23):
    a='獅子'
elif (m == 8) and (d>=24) and (d<=31):
    a='處女'
elif (m == 9) and (d>=1) and (d<=23):
    a='處女'
elif (m == 9) and (d>=24) and (d<=30):
    a='天秤'
elif (m == 10) and (d>=1) and (d<=23):
    a='天秤'
elif (m == 10) and (d>=24) and (d<=30):
    a='天蠍'
elif (m == 11) and (d>=1) and (d<=22):
    a='天蠍'
elif (m == 12) and (d>=21) and (d<=31):
    a='射手'
elif (m == 11) and (d>=1) and (d<=23):
    a='射手'
else:
    print('輸入錯誤')
print('星座為:',a)