a=['飢餓遊戲3','解憂雜貨店','怪獸與牠門的產地','哈利波特6','我的阿富汗筆友','祈念之樹','樓下的房客','小王子']
b=['房思琪的初戀樂園','等一個人咖啡','鬼滅之刃14','神農嘗百草','麥田捕手','老人與海','傲慢與偏見','與神同行']
user=input('請輸入欲租借的書籍:')
for i in a :
    if user==i:
        print('在書架A的第'+str(a.index(user)+1)+'本')
for i in b :
    if user==i:
        print('在書架B的第'+str(b.index(user)+1)+'本')
if a.count(user)==0 and b.count(user)==0:
    print('查無此書籍')