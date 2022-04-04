from operator import le
from random import randrange


all=set(['John','Mary','Tina','Fiona','Claire','Eva','Ben','Bill','Bert'])
en=set(['John','Mary','Fiona','Claire','Ben','Bill'])
ma=set(['Mary','Fiona','Claire','Eva','Ben'])
# an1=[]
# an2=[]
# an3=[]
# for s in range(0,len(all)):
#     if all[s] not in ma:
#         an2.append(all[s])
#     for i in range(0,len(ma)):
#         if ma[i] in en:
#             an1.append(ma[i])
#     for a in range(0,len(en)):
#         if en[a] in an2:
#             an3.append(en[a])
print('英文數學都及格:',(en&ma))
print('數學不及格:',(all-ma))
print('英文及格且數學不及格:',en&(all-ma))