import numpy

data1 = [1,2,3,4]
data2 = [[1,2,3,9],[1,2,3,8]]
data3 = [[[1,2,3,4],[1,2,3,4]],[[1,2,3,4],[1,2,3,4]]]

# 数组属性测试
def test1():
    # ndim表示数组维度，列表的嵌套关系就是维度，一层嵌套就是一个维度
    # shape表示每个维度中元素的个数
    for d in [data1, data2, data3]:
        x = numpy.array(d)
        print(x.ndim,x.shape,x.dtype)

# 数组切片测试
def test2():
    # 返回一个一维数组而不是一个列表
    x = numpy.arange(5)
    print(x)
    y = numpy.array([[1,2,3,4],[4,5,6,7],[3,4,5,6]])
    # 对一个多维数组进行切片既可以用列表的方法，也可以用数组的切片方法
    print(y[1][2])
    print(y[1,2])

def test3():
    x = numpy.array([[1,2,3,4],[4,5,6,7],[3,4,5,6]])
    # 这个不是复制一个，所以会改变原数组
    t = x[0]
    print(t)
    t[0] = 8
    print(t,x)

    y = numpy.array([[1, 2, 3, 4], [4, 5, 6, 7], [3, 4, 5, 6]])
    # 这个是复制一个副本，不会改变原数组
    k = y[0].copy()
    print(k)
    k[0] = 9
    print(k,y)

# 条件索引测试
def test4():
    x = numpy.array([3, 2, 3, 1, 3, 0, 9])
    print(x>=3)
    print(x[(x>=3)])       # 但条件
    print(x[~(x>=3)])      # 否
    print(x[(x>1)&(x<4)])  # 并
    print((x>2)|(x==1))    # 或
    print(x[(x>2)|(x==1)|(x==0)])

    # 这个条件语句有点像Excel的IF用法
    y = numpy.array([1,2,3,4,5,6])
    p = numpy.where(y>3,"d","x")
    print(p)
    y1 = numpy.array([-1, -2, -3, -4,0,0])
    y2 = numpy.array([1, 2, 3, 4,8,9])
    xx = numpy.where(y > 2, y1, y2)  # 长度须匹配
    print(xx)

# 统计方法
def test5():
    x = numpy.array([[1,3,5,2,5],[2,4,5,6,7],[1,1,1,1,1]])
    # 求和
    print(x.sum())
    print(x.sum(axis=1),x.sum(axis=0)) # axis=1表示每行，axis=0表示每列

    print(x.max(axis=0),x.min(axis=0))

# test1()
# test2()
# test3()
# test4()
test5()