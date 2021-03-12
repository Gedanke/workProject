# -*- coding:utf-8 -*-


from sklearn.datasets import load_iris
import pandas
import seaborn

iris = load_iris()


def show_data_msg():
    """
    :return:
    """
    '''dict_keys(['data', 'target', 'frame', 'target_names', 'DESCR', 'feature_names', 'filename'])'''
    key = iris.keys()
    '''150,4'''
    n_samples, n_features = iris.data.shape
    '''['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)']'''
    feature_names = iris.feature_names
    '''(150,)'''
    target_shape = iris.target.shape
    '''['setosa' 'versicolor' 'virginica']'''
    target_names = iris.target_names


def show_data():
    """
    :return:
    """
    iris_data = pandas.DataFrame(iris.data, columns=iris.feature_names)
    iris_data["species"] = iris.target_names[iris.target]
    iris_data.head(3).append(iris_data.tail(3))
    seaborn.pairplot(iris_data, hue='species', palette='husl');


if __name__ == '__main__':
    """https://mp.weixin.qq.com/s/I29o97pdFqUX0WZfo8rRjg"""
    # show_data_msg()
    # show_data()
