aa=int(input('輸入一正整數:'))
if aa%2==0 and aa%11==0 and aa%5!=0 and aa%7!=0:
    print(str(aa)+' 為新公倍數?: YES')
else:
    print(str(aa)+' 為新公倍數?: NO')