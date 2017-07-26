# -*- conding:utf-8 -*-

from configparser import ConfigParser
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from scipy.misc import imread

class TEST(object):
    def __init__(self,dataname,fontname,photoname,savename):
        self.dataname = dataname
        self.fontname = fontname
        self.photoname = photoname
        self.savename = savename
    def get_wc(self):
        cf = ConfigParser()
        cf.read(self.dataname,encoding='utf-8')
        lis = cf.items('wcdata')
        dic = {i[0]:int(i[1]) for i in lis}
        colors = imread(self.photoname)
        wc = WordCloud(background_color='white',mask=colors,font_path=self.fontname,max_font_size=100)
        wc.generate_from_frequencies(dic)
        plt.imshow(wc)
        plt.axis('off')
        wc.to_file(self.savename)
        print('get the photo {} !'.format(self.savename))



if __name__ == '__main__':
    test = TEST(dataname=r'basedata.ini',fontname=r'兰亭黑GBK.TTF',photoname='jielun.jpg',savename='wordcloud.jpg')
    test.get_wc()



