# 親骨肉判斷
inp=input('請輸入測試的資料量:')
# inp=['1']
for i in range(0,int(inp[0])):
    inp1=input('第'+str(i+1)+'個').split(' ')
    # inp1=['o','a','b']
    if inp1[0]=='O' or inp1[0]=='o':
        if inp1[1]=='O' or inp1[1]=='o':
            if inp1[2]=='O' or inp1[2]=='o':
                print('Yes')
            else:
                print('Impossible')
        elif inp1[1]=='a' or inp1[1]=='A':
            if inp1[2]=='O' or inp1[2]=='o' or inp1[2]=='A' or inp1[2]=='a':
                print('Yes')
            else:
                print('Impossible')
        elif inp1[1]=='b' or inp1[1]=='B':
            if inp1[2]=='O' or inp1[2]=='o' or inp1[2]=='b' or inp1[2]=='B':
                print('Yes')
            else:
                print('Impossible')
        elif inp1[1]=='ab' or inp1[1]=='AB':
            if inp1[2]=='A' or inp1[2]=='a' or inp1[2]=='b' or inp1[2]=='B':
                print('Yes')
            else:
                print('Impossible')
    elif inp1[0]=='A' or inp1[0]=='a':
        if inp1[1]=='A' or inp1[1]=='a':
            if inp1[2]=='O' or inp1[2]=='o' or inp1[2]=='a' or inp1[2]=='A':
                print('Yes')
            else:
                print('Impossible')
        elif inp1[1]=='b' or inp1[1]=='B':
            if inp1[2]=='O' or inp1[2]=='o' or inp1[2]=='a' or inp1[2]=='A' or inp1[2]=='b' or inp1[2]=='B' or inp1[2]=='ab' or inp1[2]=='AB':
                print('Yes')
            else:
                print('Impossible')
        elif inp1[1]=='ab' or inp1[1]=='AB':
            if inp1[2]=='a' or inp1[2]=='A' or inp1[2]=='b' or inp1[2]=='B' or inp1[2]=='ab' or inp1[2]=='AB':
                print('Yes')
            else:
                print('Impossible')
    elif inp1[0]=='B' or inp1[0]=='b':
        if inp1[1]=='b' or inp1[1]=='B':
            if inp1[2]=='O' or inp1[2]=='o' or inp1[2]=='b' or inp1[2]=='B' :
                print('Yes')
            else:
                print('Impossible')
        elif inp1[1]=='ab' or inp1[1]=='AB':
            if inp1[2]=='a' or inp1[2]=='A' or inp1[2]=='b' or inp1[2]=='B' or inp1[2]=='ab' or inp1[2]=='AB':
                print('Yes')
            else:
                print('Impossible')
    elif inp1[0]=='AB' or inp1[0]=='ab':
        if inp1[1]=='ab' or inp1[1]=='AB':
            if inp1[2]=='a' or inp1[2]=='A' or inp1[2]=='b' or inp1[2]=='B' or inp1[2]=='ab' or inp1[2]=='AB':
                print('Yes')
            else:
                print('Impossible')
    else:
        print('輸入錯誤')