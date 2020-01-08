## Python数据可视化分析常用函数

#### pandas库
|pandas函数|简单说明|示例|
|-|-|-|
| df[column_name].hist()| 直方图|[查看API](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.hist.html)|
|df[column_name].plot.density() | 密度图|[查看API](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.plot.density.html)|

#### matplotlib库

|matplotlib函数|简单说明|示例|
|-|-|-|
|plt.scatter()|散点图(将两个数值变量的值显示为二维空间中的笛卡尔坐标)|[查看API](https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.scatter.html)|

#### seaborn库
|seaborn函数|简单说明|示例|
|-|-|-|
|seaborn.displot()|同时显示直方图和密度图|[查看API](https://seaborn.pydata.org/generated/seaborn.distplot.html)|
|seaborn.boxplot() |箱形图|[查看API](https://seaborn.pydata.org/generated/seaborn.boxplot.html)|
|seaborn.violinplot() |提琴形图|[查看API](https://www.cntofu.com/book/172/docs/17.md)|
|seaborn.countplot()|条形图|[查看API](https://seaborn.pydata.org/generated/seaborn.countplot.html)|
|seaborn.heatmap|绘制矩形数据作为颜色编码矩阵|[查看API](https://seaborn.pydata.org/generated/seaborn.heatmap.html)|
|seaborn.jointplot()|Draw a plot of two variables with bivariate and univariate graphs(简单翻译就是同时绘制多种图)|[查看API](https://seaborn.pydata.org/generated/seaborn.jointplot.html)|
|seaborn.pairplot()| 散点图矩阵(这个amazing)|[查看API](https://seaborn.pydata.org/generated/seaborn.pairplot.html)|
|seaborn.lmplot()| 回归图|[查看API](https://seaborn.pydata.org/generated/seaborn.lmplot.html)|
|seaborn.catplot()|提供绘制多种图的接口|[查看API](https://www.bookstack.cn/read/seaborn-0.9/docs-13.md)|
|seaborn.countplot()| 针对类别变量的直方图|[查看API](https://www.bookstack.cn/read/seaborn-0.9/docs-21.md)|
