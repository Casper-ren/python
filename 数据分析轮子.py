# -*- coding: utf-8 -*-
"""
Created on Fri Sep 16  2022
数据分析工具库
@author: Casper
"""



"""
通过箱线图处理离群值
"""
def boxplot_fill(col):
 # 计算iqr：数据四分之三分位值与四分之一分位值的差
 iqr = col.quantile(0.75)-col.quantile(0.25)
 # 根据iqr计算异常值判断阈值
 u_th = col.quantile(0.75) + 1.5*iqr # 上界
 l_th = col.quantile(0.25) - 1.5*iqr # 下界
 # 定义转换函数：如果数字大于上界则用上界值填充，小于下界则用下界值填充。
 def box_trans(x):
  if x > u_th:
   return u_th
  elif x < l_th:
   return l_th
  else:
   return x
 return col.map(box_trans)



"""
空值处理
"""
df.user_name.fillna('notlogin', inplace=True)
df.department.fillna(df.department.mode()[0], inplace=True)
df.fillna(method='ffill')#method='ffill'或'pad'，表示用前一个非缺失值去填充该缺失值，语法为；

df.fillna(method='bflii')#method ='bflii'或'backfill'，表示用下一个非缺失值填充该缺失值，语法为

"""
查看哪些特征是数字特征，哪些是类别特征，类别特征中有多少不同的类别
"""
# 数值特征
numeric_features = df.select_dtypes(include=[np.number])
print(numeric_features.columns)
# 类型特征
categorical_features = df.select_dtypes(include=[np.object])
print(categorical_features.columns)
for cat_fea in categorical_features:
    print(cat_fea + "的特征分布如下：")
    print("{}特征有个{}不同的值".format(cat_fea, df[cat_fea].nunique()))
    print(df[cat_fea].value_counts())


"""
如果类别不多，转为one-hot 类别太多直接数值，全部数值的话可能需要归一化
"""
outlist=['ip_transform','device_num_transform']
for cat_fea in categorical_features :
    if cat_fea not in outlist:
        df1=pd.get_dummies(df[cat_fea])
        df = pd.concat([df, df1], axis=1)
        df.drop(columns = cat_fea, inplace=True)
from sklearn.preprocessing import LabelEncoder
for feat in outlist:
   lab = LabelEncoder()
   df[feat] = lab.fit_transform(df[feat])


"""
看各种特征方差
"""
features = [f for f in df.columns if f not in ['user_name','id','is_risk' ]]
from sklearn.feature_selection import VarianceThreshold
selector = VarianceThreshold(threshold=0)#默认threshold=0.0
selector.fit_transform(df[features])
# 查看各个特征的方差,
selector.variances_ ,len(selector.variances_)
# 特征对应方差
all_used_features_dict = dict(zip(features,selector.variances_ ))
