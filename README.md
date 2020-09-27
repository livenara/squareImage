# squareImage
長方形画像を枠を足して正方形にする。


## 画像変換

|変換前|(初期設定)|変換後|
|:---:|:---:|:---:|
|170px*256px|→|190px*190px|
|![Before](https://github.com/livenara/squareImage/blob/main/ReadMeImage/BeforeLenna.jpg?raw=true)|→|![After](https://github.com/livenara/squareImage/blob/main/ReadMeImage/AfterLenna.jpg?raw=true)|


## 使い方

PILによる画像変換。
横長でも縦長でも正方形に

+ サイズ指定
+ 追加背景色
+ 枠と枠の太さと枠色 (追加機能)

テスト画像ファイルを入れています。
そのまま実行できます。


### バージョン

Python 3.7で作成

### 必要なモジュール

PIL

```
$ pip install pillow
```

### Githubからコードをクローンする

任意のフォルダへ移動しGithubからコードをクローンする。

```
cd <任意のフォルダ>
git clone https://github.com/livenara/squareImage.git
```

### 実行

```
$ <任意のフォルダ>> python main.py
```

img/Lenna.jpg が saveImg/Lenna.jpg に変換されて出力されます。
