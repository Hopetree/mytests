# -*- coding: utf-8 -*-
#
# Created by: https://github.com/Hopetree
#
# Created data: 2017/7/26

import pandas as pd
import matplotlib.pyplot as plt
import pymongo
import seaborn as sns


# plt.style.use('ggplot')  # 设置图表风格
sns.set_style('darkgrid', {'font.sans-serif': ['SimHei', 'Arial']})  # 设置字体，防止中文报错

df = pd.read_excel('【生意参谋】商品效果-2017-07-25-2017-07-25.xls', encoding='gbk', header=0)
# 清洗数据
data = df[['商品id', '仓库类型', '分类', '浏览量', '访客数', '平均停留时长', '详情页跳出率', '支付金额', '支付转化率']]
data = data[data.浏览量 > 100]  # 只要浏览量大于100的
data['详情页跳出率'] = data.详情页跳出率.str.strip('%').astype(float) / 100  # 将百分比转换成浮点数，最后做完统计计算后可以还原
data['支付转化率'] = data.支付转化率.str.strip('%').astype(float) / 100


# 链接数据库
def test1():
    client = pymongo.MongoClient(host="localhost", port=27017)
    db = client['spiderdata']
    table = db['数据分析_深圳']
    df = pd.DataFrame(list(table.find()))  # 读取数据库信息并生成表
    print(df.count())
    print(df.head())


# 图表测试-箱线图
def test2():
    # print(df.tail(3).values)
    # print(df.describe())
    # print(df.head()) #前5行信息
    # print(data.info)
    # print(data.详情页跳出率)
    # column,key参数都可以是列表也可以是字符串
    data.boxplot(column=['浏览量', '访客数'], by=['仓库类型', '分类'], figsize=(8, 6))  # 使用箱线图
    data.boxplot(column=['详情页跳出率', '支付转化率'], by='分类')
    plt.xlabel('设置x轴标题')  # x的标题默认是by字段
    # plt.ylabel('设置y轴标题')
    # plt.title("这是标题")  # 标题默认是column字段
    plt.show()

# 条形图
def test3():
    # bins参数表示条形的个数
    data.hist(['浏览量','访客数'],bins=20,figsize=(8,6))
    # 保存图片必须在展示之前，不然就是一个空白
    plt.savefig(filename='test.png')
    plt.show()

# 用sns来作图，箱线图，参数好像更好理解
def test4():
    sns.boxplot(x='分类',y='浏览量',data=data)
    # data.boxplot('浏览量',by='分类')
    plt.show()

def test5():
    data.cumsum(0).plot()
    plt.show()


if __name__ == '__main__':
    # test1()
    # test2()
    # test3()
    # test4()
    test5()
