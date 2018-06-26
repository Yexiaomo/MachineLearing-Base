## numpy的随机数函数子库
numpy的random子库-->np.random.*
### np.random的随机数函数

|函数|说明|
|-|-|
|rand(d0, d1, ..., dn)|根据d0-dn创建随机数数组, 浮点数, [0,1), 均匀分布|
|randn(d0, d1, ..., dn)|根据d0-dn创建随机数数组, 标准正态分布|
|randint(low[, high, shape])|根据shape创建随机整数或整数数组,范围是[low,high)|
|random(size=None)|return floats or `ndarray of floats Array of random floats`  of shapesize|

### random的随机数生成器

|函数|说明|
|-|-|
|seed(s)|随机数种子,s是给定的种子值|

### random的排列函数

|函数|说明|
|-|-|
|shuffle(a)|根据数组a的第1轴(第一列)进行随机排列,改变数组a|
|permutation(a)|根据数组a的第1轴产生一个新的乱序数组,不改变数组a|
|choice(a[, size, replace, p])|从一维数组a中以概率p抽取抽取元素,形成size形状新的数组,replace表示是否可以重用元素,默认为True|

### random的分布函数

|函数|说明|
|-|-|
|uniform(low, high, size)|产生具有均匀分布的数组,low起始值,high结束值,size形状|
|normal(loc, scale, size)|产生具有正态分布的数组,loc均值,scale标准差,size形状|
|poisson(lam, size)|产生具有泊松分布的数组, lam随机事件发生率,size形状|
