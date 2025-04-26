# QuizCardsGeneratorWeb

このアプリは  🔗 [https://github.com/gakutensoku1976/QuizCardsGenerator](https://github.com/gakutensoku1976/QuizCardsGenerator)  
で公開されている本体アプリ **QuizCardsGenerator** を実行する際に最適なパラメータ（文字色、縁取り色、画像補正など）を検討するための支援ツールです。

**QuizCardsGeneratorWeb** は、背景画像に、タイトル・問題文・答えを自由にレイアウトし、文字色や縁取り色、画像の明るさ・コントラスト・ぼかしを調整してパラメータを検討できます。

このアプリは以下で公開されています：  
🔗 [https://quizcardsgeneratorweb.streamlit.app/](https://quizcardsgeneratorweb.streamlit.app/)

## 特長

- 背景画像を自由にアップロード可能
- タイトル・問題文・答えのテキストを個別に入力
- テキストの「文字色」「縁取り色」をカラーピッカーで指定
- 画像の明るさ、コントラスト、ぼかし効果をリアルタイム調整
- 背景画像を必須とし、設定されるまで操作できない安全設計
- 作成したクイズカードをその場でプレビュー可能
- 本体アプリ用の最適なパラメータを事前にシミュレーション可能

## インストール方法

ローカルで実行するには、以下のコマンドで必要なパッケージをインストールしてください。

```bash
pip install streamlit pillow
```

さらに、アプリ内で日本語フォントを使用しています。  
**ipaexg.ttf** というフォントファイルをソースコードと同じフォルダに配置してください。

（※ `ipaexg.ttf` は [IPAフォント公式サイト](https://moji.or.jp/ipafont/) 等からダウンロード可能です）

## 使い方

1. コマンドラインでアプリを起動します。

```bash
streamlit run main_app.py
```

2. サイドバーから背景画像をアップロードします。（jpg / jpeg / png）
3. タイトル、問題文、答えを入力します。
4. 文字色・縁取り色、画像の明るさ・コントラスト・ぼかしを調整します。
5. 自動的にプレビュー画像が更新されます。
6. 調整後のパラメータを、本体アプリへの設定に活用してください。

## ソース構成

- `main_app.py`：アプリ本体
- `ipaexg.ttf`（別途準備） ：日本語用 TrueType フォント

## ライセンス

このプロジェクトは MIT ライセンスのもとで公開されています。  
