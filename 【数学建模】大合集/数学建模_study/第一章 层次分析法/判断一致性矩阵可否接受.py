import numpy as np
# pandas数据清洗计算 matplotlib绘图库

A=np.array([[1,5,3,2],
            [1/5,1,2,1/3],
            [1/3,1/2,1,2],
            [1/2,3,1/2,1]])

n=A.shape[0] # 输出共有几行

print(n)

m=A.shape[1] # 输出共有几列

print(m)

eig_val,eig_vec=np.linalg.eig(A) #eig_val是特征值，eig_vec是特征向量——必须用于方阵

Max_eig =max(eig_val) #求最大特征值

print(Max_eig)

CI=(Max_eig - n )/(n-1) #求CI
RI=[0,0.00001,0.58,0.90,1.12,1.24,1.32,1.41,1.45] #这里RI最多支持 n=15

print("CI=",CI)
print("RI=",RI)

CR=CI/RI[n-1]

print("CR=",CR)

if CR<0.10:
    print("一致性可以接受")

else:
    print("需要修改")
