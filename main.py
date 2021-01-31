# -*- coding:utf-8 -*-


import pip
from subprocess import call
from pip._internal.utils.misc import get_installed_distributions

if __name__ == '__main__':
    for dist in get_installed_distributions():
        call('/usr/bin/python3 -m pip install --upgrade ' + dist.project_name, shell=True)
