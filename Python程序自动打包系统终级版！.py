import os
print("python程序自动打包系统")
os.system("pip install pyinstaller")
mc = input("请输入您的Python程序名称：")
dm = "pyinstaller -F "+mc+".py"
os.system(dm)
print("您的exe程序被保存在dist文件夹中！！！")
print("程序会在一分钟后关闭！")
from time import*
sleep(60)