# SteamMostPlayedRankingList
获取Steam游戏峰值玩家人数排名 (Top15)

使用方法
*确保您的计算机上已经安装了Python3*
```bash
$ git clone https://github.com/BlackSoilStudio/SteamMostPlayedRankingList.git
$ cd SteamMostPlayedRankingList
$ python3 main.py
```
如果提示缺少库，执行以下命令
```bash
$ pip3 install requests bs4 pyecharts
```

程序会在data目录下生成包含前100名的列表的json文件，并在charts目录下生成包含前15名的图表的html文件
