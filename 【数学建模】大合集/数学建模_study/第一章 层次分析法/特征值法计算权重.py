
import numpy as np

A=np.array([[1,5,3,2],[1/5,1,2,1/3],[1/3,1/2,1,2],[1/2,3,1/2,1]])

eig_val,eig_vec=np.linalg.eig(A) #eig_val是特征值，eig_vec是特征向量——必须用于方阵

#找出最大特征值的 索引
print(eig_vec)

max_index=np.argmax(eig_val)

max_vec=eig_vec[:,max_index]

##特征向量归一化

weights=max_vec/np.sum(max_vec)

print(weights)





