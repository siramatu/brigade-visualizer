## ファイル
- bert.ipynb: アンケート結果を使って類似度計算
- bert_using_crawling.ipynb: クローリングしたWeb記事を使って類似度計算
- brigade_enq.csv: アンケート結果のCSV

## 手順
1. bert_using_crawling.ipynbの
```repository_dir = '/content/drive/MyDrive/research/brigade-visualizer/source_code/'```を自分の環境にあわせて適宜編集。
repository_dirの直下にdataというディレクトリが作られる
1. クローリングしたWeb記事のデータ（https://drive.google.com/drive/folders/1CJM4aGf9h6shnBxsK24Ylagdiv5TXGBc?usp=sharing ）をdataディレクトリ直下に置く
1. 上から順に実行していく

## 動作
- 現状では、各記事の先頭512トークンだけ使っている
- 各記事のベクトルを平均化したものをブリゲードのベクトルにした
