## numpy的统计函数
numpy直接提供的统计类函数
### numpy的统计函数(1)
|函数|说明|
|-|-|
|sum(a, axis=None)|根据给定轴axis计算数组a相关元素之和, axis整数或元组|
|mean(a, axis=None)|根据给定轴axis计算数组a相关元素的期望, axis整数或元组|
|average(a, axis=None, weights=None)|根据给定轴axis计算数组a相关元素的加权平均值, axis整数或元组|
|std(a, axis=None)|根据给定轴axis计算数组a相关元素的标准差, axis整数或元组|
|var(a, axis=None)|根据给定轴axis计算数组a相关元素的方差, axis整数或元组|
 
 **axis = None 是统计函数的标配参数**


### numpy的统计函数(2)
|函数|说明|
|-|-|
|min(a) max(a)|计算数组a中元素的最小大值|
|argmin(a) argmax(a)|计算数组a中元素最小值,最大值的降一维后下标|
|unravel_index(index, shape)|根据shape将一维下标index转换成多维下标|
|ptp(a)|计算数组a中元素最大值与最小值的差|
|median(a)|计算数组a中元素的中位数(中值)|

### numpy的统计函数(3)
|函数|说明|
|-|-|
|