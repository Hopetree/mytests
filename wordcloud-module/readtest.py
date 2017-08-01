# -*- coding: utf-8 -*-

from wordcloud import WordCloud
import matplotlib.pyplot as plt
from scipy.misc import imread
import jieba
import jieba.analyse
from collections import Counter
import time

class wordtool(object):
    def __init__(self,txtname='book.txt',wordnum=150,wordflag=None,picname='jielun.jpg',savetxt='mywords.txt',
                 fontname='兰亭黑GBK.TTF',savename='test.png'):
        self.txtname = txtname
        self.wordnum = wordnum
        self.wordflag = wordflag
        self.savetxt = savetxt
        self.picname = picname
        self.fontname = fontname
        self.savename = savename
        self.set = set()
        self.counter = Counter()
        self.badword = r"[\/\\\:\*\?\"\<\>\|\.\*\+\-\(\)\"\'\（\）\！\？\“\”\,\。\；\：\{\}\{\}\=\%\*\~\·\......\`]"

    def readtxt(self):
        with open(self.txtname,'rb') as f:
            lines = f.readlines()
        return lines

    def get_words(self):
        lines = self.readtxt()
        for line in lines:
            word_list = jieba.posseg.cut(line.strip())
            for each_word in word_list:
                # 不分词性的时候
                if self.wordflag == None:
                    if each_word.word not in self.badword:
                        if each_word.word in self.set:
                            self.counter[each_word.word] += 1
                        else:
                            self.set.add(each_word.word)
                # 需要区分词性的时候
                else:
                    if self.wordflag == 'eng':   # 英文词不区分大小写
                        theword = each_word.word.title()
                    else:
                        theword = each_word.word
                    theflag = each_word.flag
                    if theflag == self.wordflag:
                        if theword in self.set:
                            self.counter[theword] += 1
                        else:
                            self.set.add(theword)
        LIST = sorted(self.counter.items(),key=lambda a:a[1],reverse=True)
        mywords = LIST[0:self.wordnum]
        with open (self.savetxt,'w') as f:
            for each in mywords:
                f.write('{}:{}'.format(each[0],each[1])+'\n')
        print(mywords)
        return mywords

    def get_cloud(self):
        word_dic = dict(self.get_words())
        colors = imread(self.picname)
        wc = WordCloud(background_color='white', mask=colors, font_path=self.fontname, max_font_size=150)
        wc.generate_from_frequencies(word_dic)
        plt.imshow(wc)
        plt.axis('off')
        wc.to_file(self.savename)
        print('get the photo {} !'.format(self.savename))



if __name__ == '__main__':
    t = time.time()
    w = wordtool(txtname='三国演义.txt',wordflag=None)
    # w.readtxt()
    # w.get_wordcloud()
    w.get_cloud()
    print("运行结束，总耗时：{:.2f}秒".format(float(time.time()-t)))