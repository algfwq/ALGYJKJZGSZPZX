import os
print("python程序自动打包系统")
print("程序正在安装依赖库，请确保pip库为最新版本，如果依赖库安装失败，程序则无法使用")
os.system("pip install pyinstaller")
print("1.无图标封装  2.带图标封装（请确保图片后缀为ico）")
print("提示：ico格式在线转换器：https://convertio.co/zh/ico-converter/")
ms = input("请选择模式（1或2）：")
if ms == "1":
    mc = input("请输入您的Python程序名称：")
    zd = input("是否允许弹出终端？1.是  2.否：")
    if zd == "1":
        dm = "pyinstaller -F " + mc + ".py"
        os.system(dm)
    if zd == "2":
        dm = "pyinstaller -F "+ mc + ".py" + " -w"
        os.system(dm)
    print("您的exe程序被保存在dist文件夹中！！！")
    print("感谢使用打包系统，官网：https://site-5888287-8893-396.mystrikingly.com/")
if ms == "2":
    mc = input("请输入您的Python程序名称：")
    tp = input("请输入您的图片名：")
    zd = input("是否允许弹出终端？1.是  2.否：")
    if zd == "1":
        tp = tp + ".ico"
        dm = "pyinstaller -F " + mc + ".py" + " -i " + tp
        os.system(dm)
    if zd == "2":
        tp = tp + ".ico"
        dm = "pyinstaller -F " + mc + ".py" + " -i " + tp + " -w"
        os.system(dm)
    print("您的exe程序被保存在dist文件夹中！！！")
    print("感谢使用打包系统，官网：https://site-5888287-8893-396.mystrikingly.com/")

