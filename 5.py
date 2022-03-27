m = int(input('請輸入階層值M:'))
n=1
total=1
while total<=m:
    total*=n
    n+=1
print('超過M為',m,'的最小階層值為',n-1)
