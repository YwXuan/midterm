ch=int(input('輸入國文成績:'))
en=int(input('輸入英文成績:'))
ma=int(input('輸入微積分成績:'))
pe=int(input('輸入體育成績:'))
py=int(input('輸入程式設計成績:'))
dict1={'國文':ch,'英文':en,'微積分':ma,'體育':pe,'程式設計':py}
sum=(ch+en+ma+pe+py)/5
list=[ch,en,ma,pe,py]
max=0
min=100
for i in range(0,5): #尋找最高及最低分數
    if list[i]>max:
        max=list[i]
    if list[i]<min:
        min=list[i]
def get_key(aa): #利用分數找到科目
    for key,value in dict1.items():
        if aa == value:
            return key
print('平均分數:%.2f'%(sum))
print('最高分科目:'+get_key(max)+str(max)+'分')
print('最低分科目:'+get_key(min)+str(min)+'分')




# lissss=['國維','英文','數學']
# grade=[]
# dict={}
# for i in range(0,len(lissss)):
#     aa=int(input('輸入'+lissss[i]+'成績:'))
#     dict[lissss[i]]=aa
# print(dict)
# max=0
# min=100
# list1=[]
# for a,b in dict.items():
#     if b>max:
#         max=b
#         list1.insert(0,a)
#     if b<min:
#         min=b