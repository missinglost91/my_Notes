import torch
import torch.nn as nn
import math

class SelfAttention(nn.Module):
    def __init__(self, d_model, n_heads, dropout=0.1):
        super().__init__()
        self.dropout = nn.Dropout(dropout) #对 10% 的神经元随机失活，避免过拟合
        self.softmax =  nn.Softmax(dim=-1) # 对最后一个维度进行softmax，将输出转换为概率分布
    d