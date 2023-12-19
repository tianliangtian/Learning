# Numpy
## 1 Numpy概述
### 1.1 概念
NumPy(Numerical Python) 是 Python 语言的一个扩展程序库，支持大量的维度数组与矩阵运算，此外也针对数组运算提供大量的数学函数库。
### 1.2 对象
NumPy中的核心对象是ndarray，ndarray可以看成数组，存放同类元素。NumPy里面所有的函数都是围绕ndarray展开的
### 1.3 功能

## 2 数组
### 2.1 数组属性
NumPy 数组的维数称为秩（rank），秩就是轴的数量，即数组的维度，一维数组的秩为 1，二维数组的秩为 2，以此类推。
在 NumPy中，每一个线性的数组称为是一个轴（axis），也就是维度（dimensions）。比如说，二维数组相当于是两个一维数组，其中第一个一维数组中每个元素又是一个一维数组。所以一维数组就是 NumPy 中的轴（axis），第一个轴相当于是底层数组，第二个轴是底层数组里的数组。而轴的数量——秩，就是数组的维数。
NumPy 的数组中比较重要 ndarray 对象属性有：
* `ndarray.ndim`：秩，即轴的数量或维度的数量
* `ndarray.shape`：数组的维度，对于矩阵，n 行 m 列
* `ndarray.size`：数组元素的总个数，相当于 .shape 中 n*m 的值
* `ndarray.dtype`：ndarray 对象的元素类型
* `ndarray.itemsize`：ndarray 对象中每个元素的大小，以字节为单位
* `ndarray.flags`：ndarray 对象的内存信息
* `ndarray.real`：ndarray元素的实部
* `ndarray.imag`：ndarray 元素的虚部
* `ndarray.data`：包含实际数组元素的缓冲区
### 2.2 数组创建
#### 2.2.1 利用列表生成
```python
>>> import numpy as np
>>> lst = [1, 2, 3, 4]
>>> nd1 = np.array(lst)
>>> print(nd1, type(nd1))
[1 2 3 4] <class 'numpy.ndarray'>
```
#### 2.2.2 利用random模块生成
##### np.random.rand()
```python
 arr1 = np.random.rand(4, 3, 2)
```
* 0到1***均匀分布***，shape: 4\*3\*2
##### np.random.randn()
```python
 arr2 = np.random.randn(4, 3, 2)
```
* ***标准正态分布***，shape: 4\*3\*2
##### np.random.randint()
```python
arr3 = np.random.randint(low, high=None, size=None, dtype=’l’)
```
* 返回$[low,high)$间均匀分布整数，维度为size的数组。dtype为数据类型，默认的数据类型是np.int
* high没有填写时，默认生成随机数的范围是$[0，low)$
如：
```python
arr3 = np.random.randint(-5,5,size=(2,2))
```
##### np.random.uniform()
```python
np.random.uniform(0, 10, 2)
```
* 生成$[low,high)$间均匀分布浮点数，维度为size的数组，与`randint`类似
##### 生成$[0,1)$间浮点数
* numpy.random.random_sample(size=None)
* numpy.random.random(size=None)
* numpy.random.ranf(size=None)
* numpy.random.sample(size=None)
```python
np.random.random_sample(size=(2,2))
np.random.random(size=(2,2))
np.random.ranf(size=(2,2))
np.random.sample(size=(2,2))
```
##### numpy.random.seed()
* 为生成的随机数指定种子，使生成可预测
* 当我们设置相同的seed，每次生成的随机数相同。如果不设置seed，则每次会生成不同的随机数
#### 创建特定形状数组
function|description
:---------------:|:------------:
np.zeros((3,4))|创建 3 x 4 的元素全为0的数组
np.ones((3,4))|创建 3 x 4 的元素全为1的数组
np.empty((3,4))|创建 3 x 4 的空数组，空数组中的值不是0，而是未初始化的垃圾值
np.eye(5)|创建 5 x 5 的矩阵，对角线元素为1，其余为0
np.full((3,5), 666)|创建 3 x 5 的数组，数组中的值均为666

#### 从已有数组创建
##### numpy.asarray
```python
numpy.asarray(a, dtype = None, order = None)
```
* a：任意形式的输入参数，可以是，列表, 列表的元组, 元组, 元组的元组, 元组的列表，多维数组
* order：可选，有"C"和"F"两个选项,分别代表，行优先和列优先，决定在计算机内存中的存储元素的顺序。
```python
>>> import numpy as np
>>> x = [(1,2,3),(4,6,0)]
>>> a = np.asarray(x)
>>> a
array([[1, 2, 3],
       [4, 6, 0]])
```
##### numpy.frombuffer
numpy.frombuffer 用于实现动态数组。
numpy.frombuffer 接受 buffer 输入参数，以流的形式读入转化成 ndarray 对象。
```python
numpy.frombuffer(buffer, dtype = float, count = -1, offset = 0)
```
> ***注意***：buffer 是字符串的时候，Python3 默认 str 是 Unicode 类型，所以要转成 bytestring ，在原 str 前加上 b。

* buffer：可以是任意对象，会以流的形式读入
* dtype：返回数组的数据类型，可选
* count：读取的数据数量，默认为-1，读取所有数据
* offset：读取的起始位置，默认为0
```python
>>> s = b'Hello World'
>>> a = np.frombuffer(s, dtype = 'S1')
>>> a
array([b'H', b'e', b'l', b'l', b'o', b' ', b'W', b'o', b'r', b'l', b'd'],
      dtype='|S1')
```
#### 从数值范围创建
##### numpy.arange
```python
numpy.arange(start, stop, step, dtype)
```
* start：起始值，默认为0
* stop：终止值（不包含）
* step：步长，默认为1
* dtype：返回ndarray的数据类型，如果没有提供，则会使用输入数据的类型
```python
>>> x = np.arange(5)
>>> x
array([0, 1, 2, 3, 4])
```
```python
>>> x = np.arange(10,20,2,dtype=float)
>>> x
array([10., 12., 14., 16., 18.])
```
##### numpy.linspace
用于创建一个由等差数列构成的一维数组
```python
np.linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None)
```
* start：起始值
* stop：终止值，若endpoint为true，则该值包含于数列中
* num：要生成的等步长的样本数量，默认为50
* retstep：如果为 True 时，生成的数组中会显示间距，反之不显示
```python
>>> a = np.linspace(1,1,10)
>>> a
array([1., 1., 1., 1., 1., 1., 1., 1., 1., 1.])
```
```python
>>> a = np.linspace(10, 20, 5, endpoint = False, retstep = True)
>>> a
(array([10., 12., 14., 16., 18.]), 2.0)
```
##### numpy.logspace
用于创建一个等比数列
```python
np.logspace(start, stop, num=50, endpoint=True, base=10.0, dtype=None)
```
* start：序列的起始值为：base ** start
* stop：序列的终止值为：base ** stop。如果endpoint为true，该值包含于数列中
* base：log的底数
```python
>>> a = np.logspace(1,5,num=10,base=10)
>>> a
array([1.00000000e+01, 2.78255940e+01, 7.74263683e+01, 2.15443469e+02,
       5.99484250e+02, 1.66810054e+03, 4.64158883e+03, 1.29154967e+04,
       3.59381366e+04, 1.00000000e+05])
```
```python
>>> a = np.logspace(1,10,num=10,base=2)
>>> a
array([   2.,    4.,    8.,   16.,   32.,   64.,  128.,  256.,  512.,
       1024.])
```
## 函数
### 数学函数
#### 三角函数
`np.sin()`, `np.cos()`, `np.tan()` 返回不同弧度的三角函数值。
如果是角度需要乘 `np.pi/180` 转换为弧度
支持以列表、数组等作为参数。
```python
>>> a = np.array([0, 30, 45, 60, 90])
>>> print(np.sin(a * np.pi / 180))
[0.         0.5        0.70710678 0.8660254  1.        ]
```
`np.arcsin()`, `np.arccos()`, `np.arctan()` 函数返回给定角度的反三角函数
`np.degrees()` 函数将弧度转换为角度
#### 舍入函数
`numpy.around()` 函数返回指定数字的四舍五入值
```python
numpy.around(a,decimals)
```
* a: 数组
* decimals: 舍入的小数位数。 默认值为0。 如果为负，整数将四舍五入到小数点左侧的位置
```python
>>> a = np.array([1.2, 0.258, 55.26, 132, 23.2])
>>> print(np.around(a))
[  1.   0.  55. 132.  23.]
>>> print(np.around(a, decimals = 1))
[  1.2   0.3  55.3 132.   23.2]
>>> print(np.around(a, decimals = -1))
[  0.   0.  60. 130.  20.]
```
`np.floor()` 返回小于或者等于指定表达式的最大整数，即向下取整
`np.ceil()` 返回大于或者等于指定表达式的最小整数，即向上取整