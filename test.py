from random import sample

import pandas as pd

df = pd.read_csv('Mashups.csv', encoding = 'unicode_escape', engine ='python')
df= df[['MashupName','MemberAPIs']]
mashup=df.values

new_mashup=[]
for i in range(len(mashup)):
    apis=mashup[i][1].split(' @@@ ')
    if len(apis)!=1:
        new_mashup.append(mashup[i])

api_count=0
api_list=[]
interaction=0
mashup=new_mashup
for i in range(len(mashup)):
    apis=mashup[i][1].split(' @@@ ')
    for j in range(len(apis)):
        interaction+=1
        if apis[j] not in api_list:
            api_count+=1
            api_list.append(apis[j])
# 生成user_list
with open('user_list.txt','w',encoding='utf-8')as f:
    f.write('org_id remap_id\n')
    for i in range(len(mashup)):
        f.write(mashup[i][0] + ' ' + str(i) + '\n')
f.close()
df.to_csv('d:/Users/chen_lib/Desktop/fenci_result.txt',sep='\t',index=False)

# 生成item_list
# with open('item_list.txt','w',encoding='utf-8')as f:
#     f.write('org_id remap_id\n')
#     for i in range(len(api_list)):
#         f.write(api_list[i]+' '+str(i)+'\n')
# f.close()

test_api=0
interaction_test=0
test_list=[]

train_api=0
interaction_train=0
train_list=[]


# 用百分之八十的数据作training data，剩下的作testing data
ftest = open("test.txt","w",encoding='utf-8')
ftrain = open("train.txt","w",encoding='utf-8')
for i in range(len(mashup)):
    ftest.write(str(i)+' ')
    ftrain.write(str(i)+' ')
    apis = mashup[i][1].split(' @@@ ')

    train = sample(apis, int(len(apis)*0.8))
    for j in range(len(train)):
        interaction_train+=1
        if train[j] not in train_list:
            train_api+=1
            train_list.append(train[j])
        if j == len(train)-1 :
            ftrain.write(str(api_list.index(train[j]))+'\n')
        else:
            ftrain.write(str(api_list.index(train[j]))+' ')

    test = list(set(apis)-set(train))
    for k in range(len(test)):
        interaction_test += 1
        if test[k] not in test_list:
            test_api+=1
            test_list.append(test[k])
        if k == len(test)-1 :
            ftest.write(str(api_list.index(test[k]))+'\n')
        else:
            ftest.write(str(api_list.index(test[k]))+' ')
ftrain.close()
ftest.close()
print(interaction_train)
print(interaction_test)
print(train_api)
print(test_api)
