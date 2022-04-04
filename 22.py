look_in=['123',['456',9000],'456',['789',5000],'789',['888',6000],'336',['558',10000],'775',['666',12000],'566',['221',7000]]
inp=int(input(' 輸入查詢組數N為:'))
for i in range(0,inp):
    look=input('輸入第'+str(i+1)+'組').split(' ')
    if look[0] in look_in:
        if look_in[look_in.index(look[0])+1][0]==look[1]:
            print('餘額:',look_in[look_in.index(look[0])+1][1])
        else:
            print('密碼錯誤')
    else:
        print('無此帳號')
