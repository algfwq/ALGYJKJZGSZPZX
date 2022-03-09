# -*- coding: gbk-*-
"""
* 作者：王若宇
* 时间：2022/1/25 14:00
* 功能：打包Python软件包用于发布到pypi.org
* 说明：请看读我.txt，库发布后可使用学而思库管理工具下载
"""
import sys

from setuptools import setup,find_packages
#from xes import AIspeak

if __name__ == '__main__':
    sys.argv += ["sdist"]
setup(
    name='要发布的库名',
    version='版本号',
    packages=find_packages(),
    url='网址',
    license='MIT License',
    author='账号',
    author_email='邮箱',
    description='库的短介绍',
    long_description='库的长介绍',
    requires=[]
)

