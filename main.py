# -*- coding: utf-8 -*-

import requests as r
from bs4 import BeautifulSoup
import json
import datetime
from pyecharts.charts import Bar
from pyecharts import options as opts

def main():
    
    url = "https://store.steampowered.com/stats"

    Today = datetime.date.today()

    res = r.get(url)
    print("\n状态码 Status Code: %d\n" % res.status_code)

    soup = BeautifulSoup(res.content.decode('utf-8'), 'lxml')

    AllGames = soup.find_all('tr', class_='player_count_row')
    GameList = []

    for Game in AllGames:
        Game.Name = Game.find('a', class_='gameLink').text.strip()
        Game.Player = Game.find('span', class_='currentServers').text.strip()
        GameList.append({
            "GameName": Game.Name,
            "GamePlayer": Game.Player
        })

    with open("data/%s.json" % Today, 'w', encoding='utf-8') as JsonFile:
        json.dump(GameList, JsonFile, ensure_ascii=False)

    print("成功写入文件 data/%s.json" % Today)
    print("Successfully wrote into data/%s.json\n" % Today)

    GameNameList = []
    GamePlayerList = []

    for Game in GameList:
        GameName = list(Game.values())[0]
        GamePlayer = int(list(Game.values())[1].replace(',', ''))
        GameNameList.append(GameName)
        GamePlayerList.append(GamePlayer)

    bar = (
        Bar()
        .add_xaxis(GameNameList[:15])
        .add_yaxis('峰值人数', GamePlayerList[:15])
        .set_global_opts(title_opts=opts.TitleOpts(
			title="Steam游戏峰值玩家人数Top15",
			subtitle=Today))
    )

    bar.render("charts/%s.html" % Today)

    print("成功写入文件 charts/%s.html" % Today)
    print("Successfully wrote into charts/%s.html\n" % Today)

if __name__ == "__main__":
    main()
