num=[]
for i in range(10):
    num.append(int(input('請輸入第{}個數字'.format(i+1))))
num.sort()
print('最小的三個數字:',num[2::-1])
num.reverse()
print('最大的三個數字:',num[0:3])