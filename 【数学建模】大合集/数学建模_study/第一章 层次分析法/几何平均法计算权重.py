
import numpy as np

A=np.array([[1,5,3,2],
            [1/5,1,2,1/3],
            [1/3,1/2,1,2],
            [1/2,3,1/2,1]])

n,_=A.shape

prod_A=np.prod(A,axis=1)

prod_A_n=np.power(prod_A,1/n)

#归一化

re_prod_A= prod_A_n / np.sum(prod_A_n)

#展示权重结果

print(re_prod_A)






