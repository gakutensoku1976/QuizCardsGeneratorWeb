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

## 使い方

1. コマンドラインでアプリを起動します。

```bash
streamlit run main_app.py
```

2. サイドバーから背景画像をアップロードします。（jpg / jpeg / png）
3. タイトル、問題文、答えを入力します。
4. フォントを選択します。
5. 文字色・縁取り色、画像の明るさ・コントラスト・ぼかしを調整します。
6. 自動的にプレビュー画像が更新されます。
7. 調整後のパラメータを、本体アプリへの設定に活用してください。

## ライセンス

このプロジェクトは MIT ライセンスのもとで公開されています。  

## フォントライセンス情報

本アプリでは、[Open Font License.](https://openfontlicense.org/)で公開されているフォントを同梱しています。

- [Noto Sans Japanese](https://fonts.google.com/noto/specimen/Noto+Sans+JP/license?lang=ja_Jpan)
- [BIZ UDPGothic](https://fonts.google.com/specimen/BIZ+UDPGothic/license?query=BIZ+UDP&lang=ja_Jpan)
- [Kosugi Maru](https://fonts.google.com/specimen/Kosugi+Maru/license?query=Kosugi+Maru&lang=ja_Jpan)