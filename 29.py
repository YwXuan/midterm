#洗刷刷
a= input('甲方的數字:')
b= input('乙方的數字:')
print('洗刷刷結果:',end='')
for i in range(0,len(a)):
    c=a[0+i:1+i]
    d=b[0+i:1+i]
    if d=='1' and c=='5':
        print('輸',end='')
    elif d=='2' and c=='1':
        print('輸',end='')
    elif d=='3' and c=='2':
        print('輸',end='')
    elif d=='4' and c=='3':
        print('輸',end='')
    elif d=='5' and c=='4':
        print('輸',end='')
    elif d=='5' and c=='1':
        print('贏',end='')
    elif d=='1' and c=='2':
        print('贏',end='')
    elif d=='2' and c=='3':
        print('贏',end='')
    elif d=='3' and c=='4':
        print('贏',end='')
    elif d=='4' and c=='5':
        print('贏',end='')
    else:
        print('和',end='')