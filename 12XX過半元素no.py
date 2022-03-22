from typing import Counter


n = input('輸入一整數序列(空格區分)')
n1=n.split(' ')
a = Counter(n1)
c=list(a.values)[0]
d=len(n1)
e=list(a.keys)[0]
if c>=d/2:
    print('過半元素:',e)
else:
    print('過半元素:NO')