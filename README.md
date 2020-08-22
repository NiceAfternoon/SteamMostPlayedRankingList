# SteamMostPlayedRankingList
获取Steam游戏峰值玩家人数排名 (Top15)

## 使用方法
*确保您的计算机上已经安装了Python3*
```bash
$ git clone https://github.com/BlackSoilStudio/SteamMostPlayedRankingList.git
$ cd SteamMostPlayedRankingList
$ python3 main.py
```
如果提示缺少库，执行以下命令
```bash
$ pip3 install requests bs4 pyecharts lxml
```

程序会在data目录下生成包含前100名的列表的json文件，并在charts目录下生成包含前15名的图表的html文件

## Termux安装
如果您使用的是Termux，可能会遇到lxml库安装失败的问题  
执行以下命令
```bash
$ pkg install libxml2 libxslt clang
$ pip3 install cython
$ pip3 install lxml
```
安装过程中可能耗时较久，安心等待（最好保持前台运行，防止报错）
