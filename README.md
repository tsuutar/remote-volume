# remote-volume

スマホから PC の音量を操作

## Overview

少し離れたところに PC がある場合、音量調整がめんどくさいのでスマホから操作する。

## Usage

- `run.py` を実行

```
.\.venv\Scripts\activate.bat
python run.py
```

- 以下の URL へスマホからアクセスし、画面上のボタンをタップ

```
http://<Your PC IP>:5000/
```

<img src="https://github.com/tsuutar/remote-volume/assets/302372/4791a209-d41e-41bd-b717-331a387e7dd6" width="45%">

- 終了は `Ctrl + C` を押す

## Install

```
python -m venv .venv
.\.venv\Scripts\activate.bat
pip install -r requirements.txt
```

## Requirements

- Windows 10 or later
- Python 3
- スマホと PC は同一ネットワークにあること
- PC 側のファイアウォール設定で TCP ポート 5000 を許可しておくこと
