
n = input('請輸入由0~9的數字組成的N個數字字串(1<=N<=7)(請以,分隔):')
list1 = list(n.split(','))
min =sorted(list1) #排序字串做法
max=sorted(min,reverse=True) #反轉字串
m1 =int(''.join(min)) #合併字串用法
m2 =int(''.join(max))
print(m2-m1)