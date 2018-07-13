## matplotlib.pyplot库

### plot()函数
>plt.plot(x, y, format_string, **kwargs)
- x : x轴数据,列表或数组,可选
- y : y轴数据,列表或数组
- format_string : 控制曲线的格式字符串,可选
- **kwargs : 第二组或更多(x, y, format_string)
    当绘制多条曲线,各条曲线的x不能省略

#### plot()函数中的format_string参数

控制曲线的格式字符串,可选由颜色字符,风格字符和标记字符组成

|颜色字符|说明|颜色字符|说明|
|-|-|-|-|
|'b'|蓝色|'m'|洋红色|
|'g'|绿色|'y'|黄色|
|'r'|红色|'k'|黑色|
|'c'|青绿色|'w'|白色|
|'#008000'|RGB某颜色|'0.8'|灰度值字符串|

|风格字符|说明|
|-|-|
|'-'|实线|
|'--'|破折线|
|'-.'|点划线|
|':'|虚线|
|''  ' '|无线条|

|标记字符|说明|标记字符|说明|标记字符|说明|
|-|-|-|-|-|-|
|'.'|点标记|'1'|下花三角标记|'h'|竖六边形标记|
|','|像素标记(极小点)|'2'|上花三角标记|'H'|横六边形标记|
|'o'|实心圈标记|'3'|左花三角标记|'+'|十字标记|
|'v'|倒三角标记|'4'|右花三角标记|'x'|x标记|
|'^'|上三角标记|'s'|实心方形标记|'D'|菱形标记|
|'>'|右三角标记|'p'|实心五角标记|'d'|瘦菱形标记|
|'<'|左三角标记|'*'|星形标记|'\|'|垂直线标记|

#### plot()函数中的 **kwargs 参数
***kwargs : 第二组或更多(x,y,format_string)
- color : 控制颜色,color='green'
- linestyle : 线条风格,linestyle='dashed'
- marker : 标记风格,marker='o'
- markerfacecolor : 标记颜色,markerfacecolor='blue'
- markersize : 标记尺寸,markersize=20
- ...

### pyplot的文本显示函数
|函数|说明|
|-|-|
|plt.xlabel()|对X轴增加文本标签|
|plt.ylabel()|对Y轴增加文本标签|
|plt.title()|对图形整体增加文本标签|
|plt.text()|在任意位置增加文本|
|plt.annotate()|在图形中增加带箭头的注解|

### pyplot的基础图标函数
|函数|说明|
|-|-|
|plt.plot(x, y, format_string, **kwargs)|绘制一个坐标图|
|plt.boxplot(data, notch, position)|绘制一个箱形图|
|plt.bar(left, height, width, bottom)|绘制一个条形图|
|plt.barh(width, bottom, left, height)|绘制一个横向条形图|
|plt.polar(theta, r)|绘制极坐标图|
|plt.pie(data, explode)|绘制饼图|
|plt.psd(x, NFFT=256, pad_to, Fs)|绘制功率谱密度图|
|plt.specgram(x, NFFT=256, pad_to, F)|绘制谱图|
|plt.cohere(x,y,NFFt=256, Fs|绘制X-Y的相关性函数|
|plt.scatter(x,y)|绘制散点图,其中 x和y 的长度相同|
|plt.step(x,y,where)|绘制布阶图|
|plt.hist(x,bins,normed)|绘制直方图(bins:直方的个数)|
|plt.contour(X,Y,Z,N)|绘制等值图|
|plt.vlines()|绘制垂直图|
|plt.stem(x,y,linefmt,markerfmt)|绘制柴火图|
|plt.plot_date()|绘制数据日期|
