# poke-scripts

ポケットモンスターソード・シールドでPCから入力を行うPythonスクリプトたち

## 事前準備

### 準備物

- USB搭載のマイクロコンピュータ（CPUにatmega32u4 を搭載したもの）
  - 参考 [Arduino Leonald互換マイコン(Amazon)](https://www.amazon.co.jp/dp/B07NKSMPFK/ref=cm_sw_r_tw_dp_U_x_o2LlEbZMNDEN7)
- USBシリアル変換アダプタ
  - 参考 [FT232RQ USBシリアル変換モジュールキット(秋月電子通商)](http://akizukidenshi.com/catalog/g/gK-09951/)
- Switchとマイコンをつなぐケーブル(どちらか)
  - microUSB to Type-AケーブルでSwitchのドックにつなぐ
  - microUSB to Type-CケーブルでSwitchに直接つなぐ
- [itiB/Switch-Fightstick](https://github.com/itiB/Switch-Fightstick)
  - Fork元のEbithさんのに加えジョイコン左右同時に入力する機能が(~~無理やり~~)付け加えられています
- Python 3.6以上

### itib/Switch-Fightstick のインストール

そのうちWindowsを例に書きます...

### ダウンロード

```bash
$ git clone https://github.com/itiB/poke-scripts
```

### アップデート

```bash
$ git pull
```

## 使い方

### たまご自動孵化 (auto_hatch.py)

#### 条件

- 手持ちポケモンがほのおのからだのポケモン一匹のみ
- ハシノマはらっぱにいる
- Xボタンで表示されるメニューがデフォルトのままである
  - 下段一番左がマップ，上段左から二番目がポケモン
- メニューのカーソルがマップになっている
- 自転車に乗った状態でフィールドにいる
- ボックスに十分な空きがあること

使用方法:

- `$ python3 auto_hatch.py <USB接続ポート>`
  - `--count <孵化数>`  : 何匹孵化させるか設定する(デフォルト60匹)
  - `--cycle <孵化サイクル>`    : 孵化サイクル(デフォルト20)
    - 孵化対象のポケモンのタマゴ歩数によって変更 (<https://yakkun.com/swsh/zukan/> を参照)

