
import numpy as np

A=np.array([[1,5,3,2],[1/5,1,2,1/3],[1/3,1/2,1,2],[1/2,3,1/2,1]])

###按列归一化

ASum = np.sum(A,axis=0)#按列求和

n,_=A.shape # 获取A的行数

stand_A=A/ASum # stand_A是归一化的新矩阵

print(stand_A)

###

ASumr = np.sum(stand_A, axis=1) # ASumr为按行求和后

print(ASumr)

weights =ASumr / n  # weights为最后的权重向量

print(weights)









