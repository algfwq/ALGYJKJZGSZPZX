# -*- coding: gbk-*-
"""
* ���ߣ�������
* ʱ�䣺2022/1/25 14:00
* ���ܣ����Python��������ڷ�����pypi.org
* ˵�����뿴����.txt���ⷢ�����ʹ��ѧ��˼�����������
"""
import sys

from setuptools import setup,find_packages
#from xes import AIspeak

if __name__ == '__main__':
    sys.argv += ["sdist"]
setup(
    name='Ҫ�����Ŀ���',
    version='�汾��',
    packages=find_packages(),
    url='��ַ',
    license='MIT License',
    author='�˺�',
    author_email='����',
    description='��Ķ̽���',
    long_description='��ĳ�����',
    requires=[]
)

