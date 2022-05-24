a='紅豆生南國，春來發幾枝?願君多采擷，此物最相思。'
b='春眠不覺曉，處處聞啼鳥，夜來風雨聲，花落知多少。'
a1=list(a)
b1=list(b)
r=[]
for i in a1:
    if (b1.count(i)>0):
        r.append(i)
    if r.count('，')!=0:
        r.remove('，')
    if r.count('。')!=0:
        r.remove('。')
print(r)