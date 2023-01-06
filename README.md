# mypkg
 ロボットシステム学の練習リポジトリ 課題2

# talker,listener
 countupトピックを通してtalkerからlistenerにメッセージを送る
## インストール方法
 下記のコマンドを入力しインストールが完了していることを確認する  
```
$ git clone https://github.com/yukisato1481/mypkg.git
$ cd mypkg
$ ls
LICENSE  README.md  launch  mypkg  package.xml  resource  setup.cfg  setup.py  test
```
## 入出力例
* 端末１に入力  
```
$ ros2 run mypkg listener
```  
* 端末２に入力  
```
$ ros2 run mypkg talker
```  
* 端末１にて出力  
```
[INFO] [1672422918.080772800] [listener]: Listen: 0
[INFO] [1672422918.572537800] [listener]: Listen: 1
[INFO] [1672422919.072751600] [listener]: Listen: 2
[INFO] [1672422919.572661700] [listener]: Listen: 3
[INFO] [1672422920.072029700] [listener]: Listen: 4
[INFO] [1672422920.572088900] [listener]: Listen: 5
[INFO] [1672422921.072431400] [listener]: Listen: 6
[INFO] [1672422921.572671800] [listener]: Listen: 7
[INFO] [1672422922.072556200] [listener]: Listen: 8
[INFO] [1672422922.572563300] [listener]: Listen: 9
``` 

# launch
 talkerとlistenerを同時に立ち上げる

## 入出力例
```
$ ros2 launch mypkg talk_listen.launch.py
[INFO] [launch]: All log files can be found below /home/sato/.ros/log/2023-01-06-22-10-34-768650-DESKTOP-U7FB1AD-670
[INFO] [launch]: Default logging verbosity is set to INFO
[INFO] [talker-1]: process started with pid [672]
[INFO] [listener-2]: process started with pid [674]
[listener-2] [INFO] [1673010635.774429600] [listener]: Listen: 0
[listener-2] [INFO] [1673010636.262852100] [listener]: Listen: 1
[listener-2] [INFO] [1673010636.762967900] [listener]: Listen: 2
[listener-2] [INFO] [1673010637.262296000] [listener]: Listen: 3
[listener-2] [INFO] [1673010637.763140400] [listener]: Listen: 4
[listener-2] [INFO] [1673010638.262904100] [listener]: Listen: 5
[listener-2] [INFO] [1673010638.762961100] [listener]: Listen: 6
[listener-2] [INFO] [1673010639.263078900] [listener]: Listen: 7
[listener-2] [INFO] [1673010639.762975600] [listener]: Listen: 8
[listener-2] [INFO] [1673010640.262833000] [listener]: Listen: 9
```
## 環境
 * Ubuntu 20.04.5 LTS
 * ROS2 foxy
## ライセンス
 * このソフトウェアパッケージは，3条項BSDライセンスの下，再頒布および使用が許可されます．
 * © 2022 YUki Sato
