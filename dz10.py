import pandas as pd
import random

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})
data.head()

######################   Решение   #########################################
categories = list(set(lst))
one_hot_data = pd.DataFrame(0, columns=categories, index=data.index)
for i, category in enumerate(categories):
    one_hot_data[category] = (data['whoAmI'] == category).astype(int)
data_one_hot = pd.concat([data, one_hot_data], axis=1)
data_one_hot.drop('whoAmI', axis=1, inplace=True)
data_one_hot.head()
print(one_hot_data)