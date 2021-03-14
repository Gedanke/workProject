# -*- coding: utf-8 -*-

from core.dealData import *

"""
将 original_path 路径的txt文件，以 separator 为分割符，以 attribute_name 为列名(含标签)
使用 TransformData 类，得到与txt文件同一路径下的csv文件
"""


original_path = "../originalDataSet/abalone/abalone.txt"
separator = " "
attribute_name = [
    "Label", "Length", "Diam", "Height", "Whole", "Shucked", "Viscera", "Shell", "Rings"
]


def fun1():
    """
    使用 TransformData 类，调用一次即可
    :return:
    """
    t = TransformData(original_path, separator, attribute_name)
    '''使用 mine_deal() 或者 standard_data() 方法都可'''
    t.mine_deal()


if __name__ == "__main__":
    '''将 label 列移至最后一行'''
    # fun1()
