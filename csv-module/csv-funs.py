# -*- coding: utf-8 -*-
import csv

def not_use_csv(file='not_use_csv.csv'):
    with open(file,'w') as f:
        fieldnames = ['number', 'string', 'money', 'date', 'float', 'percentage']
        s = ','.join(fieldnames)+'\n'
        for i in range(4):
            f.write(s)
        # 如果字符串中有逗号，就会被分隔开
        fieldnames_1 = ["'012345", 'string,一个分隔符', 'money', 'date', 'float', 'percentage']
        f.write(','.join(fieldnames_1)+'\n')

def csv_for_list(file='for_list.csv'):
    with open(file,'w',newline='') as f:
        fieldnames = ['number', 'string', 'money', 'date', 'float', 'percentage']
        writer = csv.writer(f)
        writer.writerow(fieldnames)
        list_1 = ['01234567','a-zA-Z,字符串','129.00','1990-10','129.89','45%']
        writer.writerow(list_1)
        writer.writerows([list_1,list_1,list_1])

def csv_for_dict(file='for_dict.csv'):
    with open(file,'w',newline='') as f:
        # 表头信息
        fieldnames = ['number','string','money','date','float','percentage']
        # 写入模式
        writer = csv.DictWriter(f,fieldnames=fieldnames)
        # 写入表头
        writer.writeheader()

        dic_1 = {
            'number':'0123456',
            'string':'a-zA-Z,字符串',
            'money':'129.00',
            'date':'1990-10-4',
            'float':'12.99',
            'percentage':'89%'
        }
        writer.writerow(dic_1)
        writer.writerows([dic_1,dic_1,dic_1])


if __name__ == '__main__':
    not_use_csv()
    csv_for_list()
    csv_for_dict()

