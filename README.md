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

[私のリリースする場所]:[3]
からインストールできます,zipファイルですね.
すべて展開してからでないと実行時にエラー出ます.
インストールしたファイルのdist以下のmain.exeをダブルクリックすると実行可能です.
windowsにセキュリティーエラーの警告がされるかもしれません.

動かし方
---

| コマンド | 動作 |
| :------------ | :------------------------------------------- |
| 'start' | シュミレーション開始 ,最初はSpaceキーを押さないといけない |
| 'stop','pause'  | 一時停止,どっちのコマンドでも同じ動作 |
| 'exit','quit' | シュミレーションの終了 |
| 'clear'           | すべてのセルの状態を死にする |
| 'random'| セルの状態をランダムにする | 
| 'grider' | ライフゲームにおけるグライダーを左上に一つ作成|

その他
---
各セルをクリックするとセルの状態を変更できます。
'pause'コマンドを使用してからでないと,変更が実感できないかもというのも周りのセルが死んでいたら
そのセルはすぐに死ぬから.

[1]:https://github.com/DYGV/pygame_textinput
[2]:https://github.com/DYGV
[3]:https://github.com/yoshiyuki-140/game_of_life/releases