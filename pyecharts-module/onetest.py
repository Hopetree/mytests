# -*- conding:utf-8 -*-

from configparser import ConfigParser

class TEST(object):
    def __init__(self):
        cf = ConfigParser()
        cf.read('config.ini',encoding='utf-8')
        self.ftitle = '数据来源：“龙华吧”91521条数据'

        self.bardata = cf.items('bardata')
        self.piedata = cf.items('piedata')
        self.sexpiedata = cf.items('sexpiedata')
        self.worldcloud = cf.items('worldcloud')
        self.linedata = cf.items('linedata')

    def bartest(self):
        from pyecharts import Bar
        bar = Bar('等级分布条形图',self.ftitle)
        # 利用自带的解析方法把列表解析成2个关联列表
        key,value = bar.cast(self.bardata)
        # is_datazoom_show = 参数是用来显示下滑筛选块的，默认假
        # is_label_show = 参数用来显示数值，默认假
        bar.add('等级分布',key,value,is_datazoom_show=False,is_label_show=True)
        # bar.show_config()
        bar.render("bartest.html")
        print('成功输出Bar测试网页')

    def pietest(self):
        from pyecharts import Pie
        pie = Pie('头衔分布饼形图',self.ftitle,height=600,title_pos='left')
        key,value = pie.cast(self.piedata)
        pie.add('人数',key,value,is_label_show=True,is_legend_show=False,radius=[30,70])
        pie.render('pietest.html')
        print('饼形图输出Pie测试网页')

    def sexpietest(self):
        from pyecharts import Pie
        pie = Pie('性别分布饼形图',self.ftitle,height=500)
        key,value = pie.cast(self.sexpiedata)
        pie.add('人数',key,value,is_label_show=True,center=[50,55],rosetype='area')
        pie.render('sexpietest.html')
        print('性别饼形图输出成功')

    def worldcloudtest(self):
        from pyecharts import WordCloud
        import random
        wd = WordCloud('回帖数词云图')
        key,value = wd.cast(self.worldcloud)
        shapes = ['circle', 'cardioid', 'diamond', 'triangle-forward', 'triangle', 'pentagon', 'star']
        wd.add('',key,value,shape=shapes[0])
        wd.render('worldcloudtest.html')
        print('词云图测试成功')

    def linetest(self):
        from pyecharts import Line
        line = Line('发帖时间分布折线图',self.ftitle)
        key,value = line.cast(self.linedata)
        line.add('发帖人数',key,value,is_label_show=True,is_fill=True,area_opacity=0.3,is_smooth=True)
        line.render('linetest.html')
        print("折线图测试成功输出")


if __name__ == '__main__':
    test = TEST()
    test.bartest()
    test.pietest()
    test.sexpietest()
    test.worldcloudtest()
    test.linetest()