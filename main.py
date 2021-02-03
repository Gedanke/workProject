# -*- coding:utf-8 -*-


import pip
from subprocess import call
from pip._internal.utils.misc import get_installed_distributions
import jieba

#
# seg_list = jieba.cut("我来到北京清华大学", cut_all=True, HMM=False)
# print("Full Mode: " + "/ ".join(seg_list))  # 全模式


if __name__ == '__main__':
    for dist in get_installed_distributions():
        call('/usr/bin/python3 -m pip install --upgrade ' + dist.project_name, shell=True)
