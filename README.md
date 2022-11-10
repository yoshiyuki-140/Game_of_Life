game_of_life
===

内容
---

pythonのpygameというモジュールでConway's LifeGameを作成しました.
工大際で出品するのがノルマだと思っていたので、作ってしまった.

使用したモジュールなど
---

| モジュール名 | バージョン | 作者 | 
| :---------------- | :---- | :------------------------ |   
| pygame            | 1.9.6 | -                         |
| [pygame_textinput][1]  | -     | ['Eisuke Okazaki'様][2]   |

インストール & 実行
---

- Linux : Ubuntu 20.04.5 LTS (my environment)

```sh
# Install
sudo apt update && sudo apt upgrade -y
sudo apt install git python3 python3-pygame
git clone https://github.com/yoshiyuki-140/game_of_life.git
# 実行
cd src
python3 main.py
# なんかほかにインストールするべきだったような...
```

- Windows : windows 11

[私のリポジトリ]:[3]
からインストールできます,
インストールしたファイルのdist以下のmain.exeをダブルクリックすると実行可能です
windowsにセキュリティーエラーの警告がされるかもしれません

コマンド
---

START           : Space,'start'

STOP            : 'pause','stop'

END             : 'exit','quit'

clear           : 'clear'

randomInit      : 'random'

create grider   : 'grider'

GUI動作
---

各セルをクリックするとセルの状態を変更できます。
'pause'コマンドを使用してからでないと、見えないかも

[1]:https://github.com/DYGV/pygame_textinput
[2]:https://github.com/DYGV
[3]:https://github.com/yoshiyuki-140/game_of_life/releases