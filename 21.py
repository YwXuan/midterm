stu=[['123','Tom','DTGD'],['456','Cat','CSIE'],['789','Nana','ASIE'],['321','Lim','DBA'],['654','Won','FDD']]
inp1=input('輸入查詢學號')
a=0
for i in range(len(stu)):
    if stu[i].count(inp1)>0:
        print(stu[i][0],end=' ')
        print(stu[i][1],end=' ')
        print(stu[i][2],end=' ')
    elif stu[i].count(inp1)==0:
        a+=1
    elif a>=5:
        print('not exist')
