fruit={'蘋果':'紅色','香蕉':'黃色','葡萄':'紫色','藍莓':'藍色','橘子':'橘色'}
user=input('請輸入水果:')
ans=fruit.get(user)
print('{}是{}'.format(user,ans))