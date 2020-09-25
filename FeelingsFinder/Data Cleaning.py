
import pandas as pd
dataset=pd.read_csv("post.csv")
cl1=open("client1.txt","w")
cl2=open("client2.txt","w")
cl3=open("client3.txt","w")
dataset.head()list=dataset[['user_id','content']]
x=list['user_id']
y=list['content']
x_list=x.tolist()
y_list=y.tolist()
p=[]
q=[]
r=[]
i=0
for w in x_list:
    if w==1:
        cl1.write("{")
        cl1.write(y_list[i])
        cl1.write("}    \n")
        i+=1
    elif w==2:
        cl2.write(" {")
        cl2.write(y_list[i])
        cl2.write("}    \n")
        i+=1
    else:
        cl3.write("{")
        cl3.write(y_list[i])
        cl3.write("}     \n")
        i+=1
        




