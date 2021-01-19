# -*- coding:utf-8 -*-

import pandas
import numpy


def txt():
    lines = open("t.txt", "r").readlines()

    for line in lines:
        line = line.strip("\n")
        print(line)


def test1():
    df2 = pandas.DataFrame(numpy.random.randint(80, 120, size=(4, 2)),
                           columns=['girl', 'boy'],
                           index=pandas.MultiIndex.from_product([['English', 'Chinese'],
                                                                 ['like', 'dislike']]))
    print(df2)
    df2.to_csv("demo.csv")


def test2():
    # 手动去重，针对同一输入特征，标签不一致的一些样本，采用手动groupby，得到一个带有多个标签的样本。
    df = pandas.DataFrame({'key1': list('aabba'),
                           'key2': ['one', 'two', 'one', 'two', 'one'],
                           'data1': numpy.random.randn(5)})
    Xcols = ['key1', 'key2']
    df1 = df[Xcols].drop_duplicates().reset_index(drop=True)
    df1['data1'] = numpy.nan
    df1.set_index(Xcols, inplace=True)
    for name, group in df.groupby(Xcols):
        df1.loc[name, 'data1'] = ('&').join(str(x) for x in group.data1.values)
    df1 = df1.reset_index()
    df1.data1 = df1.data1.str.split('&')
    print(df1)


def test3():
    data_dict = {
        "yusuanshu": [2, 2, 4, 2, 2, 6],
        "juesuanshu": [2, 2, 5, 2, 3, 8],
        "baifengbi": [1, 0.15, 0.8, 1, 0.67, 0.75],
        "beizhu": ["a", "b", "c", "", "e", ""]
    }
    index = [
        ["A", "A", "B", "B", "B", "C"],
        ["", "AA", "", "BB", "BB", ""]
    ]
    data = pandas.DataFrame(data_dict, index=index)
    print(data)


if __name__ == "__main__":
    """"""
    # test1()
    # test2()
    test3()
