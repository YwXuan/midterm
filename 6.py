
# list1 = input('請輸入由0~9的數字組成的N個數字字串(1<=N<=7)(請以,分隔):').split(',')
list1=['1','7','4','9','3','5']
min =sorted(list1) #排序字串做法
print(type(min))
max=sorted(min,reverse=True) #反轉字串
m1 =int(''.join(min)) #合併字串用法
m2 =int(''.join(max))
print(m2-m1)