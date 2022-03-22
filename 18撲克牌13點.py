a = input('輸入五張牌(空格分開)').split(' ')
poker = {'A':1,'J':11,'Q':12,'K':13,"1":1,"2":2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10}
sum = poker.get(a[0])+poker.get(a[1])+poker.get(a[2])+poker.get(a[3])+poker.get(a[4])
print('sum:',sum)


