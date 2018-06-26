## ndarray数组的操作
### ndarray的元素类型
|数据类型|说明|
|-|-|
|bool|布尔类型,Ture或False|
|intc|与c语言中的int类型一致,一般是int32或int64|
|intp|用于索引的整数,与c语言中的size_t一致,int32或int64|
|int8|字节长度的整数,取值: [-128, 127]|
|int16|16字节长度的整数,取值: [-32768, 32767]|
|int16|32字节长度的整数,取值: [-2^31, 2^31-1]|
|int32|64字节长度的整数,取值: [-2^63, 2^63-1]|
|uint8|8位无符号整数,取值: [0, 255]|
|uint16|16位无符号整数,取值: [0, 65535]|
|uint16|16位无符号整数,取值: [0, 2^32-1]|
|uint32|32位无符号整数,取值: [0, 2^64-1]|
|float16|16位半精度浮点数: 1位符号位,5位指数,10位尾数|
|float16|16位半精度浮点数: 1位符号位,8位指数,16位尾数|
|float32|32位半精度浮点数: 1位符号位,11位指数,52位尾数|
|complex64|复数类型,实部和虚部都是32位浮点数|
|complex128|复数类型,实部和虚部都是64位浮点数|

### ndarray对象的属性
|属性|说明|
|-|-|
|.ndim|秩,即轴的数量或维度的数量|
|.shape|查看ndarray对象的形状.对于矩阵,n行m列|
|.size|ndarray对象的个数,相当于.shape中n*m的值|
|.dtype|ndarray对象的元素类型|
|.itemsize|ndarray对象中每个元素的大小,以字节为单位|

### ndarray数组的创建方法
|函数|说明|
|-|-|
|.arange(n)|类似rang()函数,返回ndarray类型,元素从0到n-1|
|.ones(shape)|根据shape生成一个全1数组,shape是元组类型|
|.zeros(shape)|根据shape生成一个全0数组,shape是元组类型|
|.full(shape,val)|根据shape生成一个数组,每个值都是val|
|.eye(n)|创建一个正方的n*n单位矩阵,对角线为1,其余为0|
|.ones_like(a)|根据数组a的形状生成一个全1数组|
|.zeros_like(a)|根据数组a的形状生成一个全0数组|
|.full_like(a, val)|根据数组a的形状生成一个数组, 每个元素值都是val|
|.linspace()|根据起止数据等间距地填充数据,形成数组|
|.concatenate()|将两个或多个数组合并成一个新的数组|

### ndarray数组的维度变换
|方法|说明|
|-|-|
|.reshape(shape)|不改变数组元素,返回一个shape形状的数组,`原数组不变`|
|.resize(shape)|与 .reshape()功能一致,`但修改原数组`|
|.swapaxes(ax1, ax2)|将数组n个维度中两个维度进行调换|
|.flatten()\|.ravel() |(两个函数有区别)将数组进行展平为一维数组,原数组不变|
|.hsplit(a, k)|k须被a整除(展示这样理解)沿`横轴`分割数组(不好理解,建议多练习)|
|.vsplit(a, k)|k须被a整除(展示这样理解)沿`竖轴`分割数组(不好理解,建议多练习)|
### ndarray数组的类型变换
    new_a = a.astype(new_type)
.astype() 方法一定会创建新的数组(原始数据的一个拷贝),即两个类型一致

### ndarray数组向列表转换
    ls = a.tolist()

## ndarray数组的运算
### 数组与标量的运算
数组与标量之间的运算作用于数组的每一个元素
### 数组与数组的运算
- `a-b` `a+b` `a*b`
是将a,b看作数组,进行运算
- `np.dot(a,b)` `np.mat(a) * np.mat(b)`
则是将a,b看作矩阵,注意运算规则

### 数组的矩阵运算(将数组看作矩阵)

|函数|说明|
|-|-|
|a.T|矩阵的转置|
|a.linalg.inv(a)|矩阵求逆|

### numpy中的一元函数
对ndarray中的数据执行元素级运算的函数

|函数|说明|
|-|-|
|np.abs(x)|np.fabs(x)|计算数组各元素的绝对值|
|np.sqrt(x)|计算数组各元素的平方根|
|np.square(x)|计算数组各元素的平方|
|np.power(x, n)|计算数组各元素的n次方|
|np.log(x)|np.log10(x)|np.log2(x)|计算数组各元素的自然对数,10底对数和2底对数|
|np.ceil(x)|np.floor(x)|计算数组各元素的ceiling值或floor值|
|np.rint(x)|计算数组各元素的四舍五入值|
|np.modf(x)|将数组各元素的小数和整数部分以两个独立的数组形式返回
|np.cos(x) np.cosh(x) np.sin(x) np.sinh(x) np.tan(x) np.tanh()|计算数组各元素的普通型和双曲型三角形函数|
|np.exp(x)|计算数组各元素的指数值|
|np.sign(x)|计算数组各元素的符号值, 1(+), 0 , -1(-)|

### numpy中的二元函数
|函数|说明|
|-|-|
|+ - * / **|两个数组各元素进行对应的运算|
|np.maximum(x,y) np.fmax() np.miniumum(x,y) np.fmin()|元素级的最大值/最小值计算|
|np.mod(x,y)|元素级的模运算|
|np.copysign(x,y)|将数组y中各元素的符号赋值给数组x对应元素|
|> < >= <= == !=| 算术比较,产生布尔型数组|
|np.vstack((a,b))|垂直拼合数组(可以想象成b放在a下面)|
|np.hstack((a,b))|水平拼合数组(可以想象成b放在a右边)|

## numpy中的数据读取
### 一维或二维的数据存取
CSV (Comma-Separated Value, 逗号分隔值)是一种常见的文件格式,用来存储批量数据
#### numpy中将数据写入csv文件的方法为 np.savetxt()
    np.savetxt(frame, array, fmt='%.18e', delimiter=None)
- frame: 文件,字符串或产生器,可以是.gz或.bz2的压缩文件
- array: 存入文件的数组
- fmt: 写入文件的格式,例如: `%d` `%.2f` `%.18e`
- delimiter: 分割字符串,默认是任何空格

#### numpy读入csv文件数据到数组中的方法为 np.loadtxt()
    np.loadtxt(frame, dtype=np.float, delimiter=None, unpack=False)
- frame: 文件,字符串或产生器,可以是.gz或.bz2的压缩文件
- dtype: 数据类型,可选
- delimiter: 分割字符串,默认是任何空格
- unpack: 如果True, 读入属性分别写入不同的变量

### 多维度(任意维度)的数据存取
存储

    .tofile(frame, sep='', format='%s')

- frame: 文件,字符串
- sep: 数据分割字符串,如果是空串,写入文件为二进制
- format: 写入数据的格式

读取

    .fromfile(frame, dtype=float, count=-1, sep='')
- frame: 文件,字符串
- dtype: 读取的数据类型
- count: 读入元素个数, -1表示读入全部文件
- sep: 数据分割字符串,如果是空串,写入文件为二进制

### numpy的便捷文件存取
存储

    np.save(fname, array) 或 np.savez(fname, array)

- fname: 文件名,以.npy为扩展名, 压缩扩展名为.npz
- aray: 数组变量

读取

    np.load(fname)
- fname: 文件名,以.npy为扩展名, 压缩扩展名为.npz
