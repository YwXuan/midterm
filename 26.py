
while True:
    n = input('輸入字串(end結束):')
    
    if n=='end':
        print('end')
        break
    else:
        while True:
            a = input('檢測的字串')
            n1 = list(n)
            t=n1.count(a)
            print('字元',a,'出現次數為',t)
            break
            