a=int(input('請輸入一個正整數(<10):'))+1

for i in range(a):
    for s in range(i):
        print(i+(i*s) , end=' ')
    print()