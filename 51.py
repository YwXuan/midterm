# user='春眠不覺曉，處處聞啼鳥。夜來風雨聲，花落知多少。春眠不覺曉，處處聞啼鳥。夜來風雨聲，花落知多少。'
user=input("請輸入自傳")
a=list(user)
r=[]
for i in a:
    if (user.count(i)>1):
        if (r.count(i)==0):
            r.append(i)     
    if (r.count('。')!=0):
        r.remove('。')
    if (r.count('，')!=0):
        r.remove('，')
print(r)