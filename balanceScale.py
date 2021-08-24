from sklearn import linear_model as lm
import pandas as pd
import numpy as np

# 把txt类型转换为numpy
path = '/Users/snszz/PycharmProjects/AVFL/RVFL_datasets/UCI/'
balance_path = 'Balance_Scale/balance-scale.data'
balance_scale = pd.read_csv(path + balance_path, sep=',', header=None, encoding='utf-8')
print(balance_scale)

#