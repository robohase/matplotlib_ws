# matplotlib_ws
<b>＊勉強用リポジトリ</b><br>

matplotlibの使い方を学ぶリポジトリ
最終的にラズパイのvcgencmdコマンドで取得したCSVデータをグラフとしてプロットしたい。

# 動作環境
- Ubuntu 22.04.4 LTS
- Python 3.10.12

# install
```bash
cd ~
git clone https://github.com/robohase/matplotlib_ws.git
cd ~/matplotlib_ws
python3 -m venv matplotlib_venv
. matplotlib_venv/bin/activate #仮想環境を有効化
pip3 install -r requirements.txt
```

# 実行例
```bash
python3 2.py
```

# ラズパイのvcgencmdコマンドで取得したCSVデータをグラフとしてプロット
CSVへの温度記録
```bash
python3 get_temp.py
```
書き出したCSVをグラフにプロット
```bash
python3 view_csv.py
```

# Deactivate
```bash
deactivate #仮想環境を無効化
```


