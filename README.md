# poke-scripts

ポケットモンスターソード・シールドでPCから入力を行うPythonスクリプトたち

## 現在わかっているバグ

- たまご孵化
  - 初めのボックスだけ25匹埋めて次にいってしまう
  - サイクルが低いポケモンはたまごが見つかっていないにもかかわらず卵を受け取りに行ってしまう
  - cycle20以外のポケモンがだいたいうまく孵化させられない

## 事前準備

### 準備物

- USB搭載のマイクロコンピュータ（CPUにatmega32u4 を搭載したもの）
  - 参考 [Arduino Leonald互換マイコン(Amazon)](https://www.amazon.co.jp/dp/B07NKSMPFK/ref=cm_sw_r_tw_dp_U_x_o2LlEbZMNDEN7)
- USBシリアル変換アダプタ
  - 参考 [FT232RQ USBシリアル変換モジュールキット(秋月電子通商)](http://akizukidenshi.com/catalog/g/gK-09951/)
- Switchとマイコンをつなぐケーブル(どちらか)
  - microUSB to Type-AケーブルでSwitchのドックにつなぐ
  - microUSB to Type-CケーブルでSwitchに直接つなぐ
- PCとマイコンをつなぐケーブル
  - microUSB to Type-Aケーブル
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

### 日付をひたすら変えるだけ (day_canger.py)

指定された回数分だけ日付を変えてくれる乱数用のツール．  
そのうち何日分進んだかとか表示できるようにします．

#### 条件

- 現在の日付と時刻にカーソルを合わせる
- 一度Aを押すとOKにカーソルが合うようになっていること

使用方法:

- `$ python3 daychanger.py <USB接続ポート>`
  - `--count <日数>`  : 何日進めるか(デフォルト30日)

### IDくじを無限に引き続ける (drawid.py)

ランクマ後，日付を無限に変えられることを利用した無限IDくじ  
月が替わるタイミングで一度だけ引けないがそのあと処理に復帰できるようにしています．

#### 条件

- ランクマに1戦以上潜った後で時渡バグが使える状態である
- ポケモンセンターのロトムPCに話しかけられる場所にいる
  - ロトムPCとポケセンのお姉さんの間にある柱のすこし右あたりがよい

使用方法:

- `$ python3 drawid.py <USB接続ポート>`

### 経験値アメ集め (candy_collect.py)

ねがいのかたまりがある限りひたすら同じ巣穴でレイドバトルし続ける．  
巣穴から出てきたポケモンはすべて捕まえない．

レイドが終わるターン数は敵によって変わってしまうため不確定．  
なので敵と戦うのもかたまりを投げるのもレイドに入るのにも全部同じ関数を使っています．  
敵と戦うためになぜか一度手持ちを見に行くのはそのせい．
ちょっと時間がかかる．

ねがいのかたまりが無くなっても変なとこ行かない安全仕様

お勧めはストーンズ原野のほのおの巣穴でエラガミのみを覚えさせたウオノラゴン

#### 条件

- 巣穴の手前に立っている
  - 上に進んでAで話しかけられる状態
  - 柱はたっていてもいなくてもよい
- 手持ちの先頭
  - 巣穴から出てくるポケモンを倒せる
  - 覚えている技が一つだけ
- 十分にねがいのかたまりを持っている
- 自転車にのっていない

使用方法:

- `$ python3 candy_collect.py <USB接続ポート>`

### 木の実集め (correct_nuts.py)

VSバグで日付が変換できるのを利用してひたすら木の実を集める．  
努力値下げる木の実や食べ残しを量産したい人むけ

揺らすのを1回だけにしてホシガリスが落ちてくるのを防いでいる

#### 条件

- 木の実の目の前に立っている
  - 上をに進むと木にぶつかる状態
- 日付を変えられる状態
  - ランクマッチに潜った直後
  - Switchの日付設定が手動で合わせる状態
- 自転車にのっていない

使用方法:

- `$ python3 collect_nuts.py <USB接続ポート>`
