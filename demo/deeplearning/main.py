# -*- coding:utf-8 -*-

"""
/home/dfs/appilcations/python/virtualenvs/venvdl/bin/python3
workon venvdl
deactivate
rmvirtualenv venvdl

wget https://developer.download.nvidia.com/compute/machine-learning/repos/ubuntu1804/x86_64/libnvinfer7_7.1.3-1+cuda11.0_amd64.deb
"""

import tensorflow as tf

print(tf.add(1, 2))
print(tf.add([1, 2], [3, 4]))
print(tf.square(5))
print(tf.reduce_sum([1, 2, 3]))

# Operator overloading is also supported
print(tf.square(2) + tf.square(3))
