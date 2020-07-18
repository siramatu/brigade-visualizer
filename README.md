# bert-as-server の使い方

## requirements

- tensorflow => 1.10, (2 系だと動かないかもです)

## 手順

(参考) https://qiita.com/shimaokasonse/items/97d971cd4a65eee43735

1. brigade-visualizer と同じ階層に bert-as-service(https://github.com/hanxiao/bert-as-service)をクローン
2. bert-as-service の中に、bert-jp ディレクトリを作成し日本語 bert の事前学習済みモデル(https://drive.google.com/drive/folders/1Zsm9DD40lrUVu6iAnIuTH2ODIkh-WM-O)の中身をダウンロードしてくる
3. 上述の Qiita 記事にあるように、ファイル名を変更したり設定ファイルを作成したりライブラリをインストールしたりする

   - tensorflow-gpu はなくても動きます
     bert-as-service/bert-jp の中で

   ```
       mv model.ckpt-1400000.index bert_model.ckpt.index
       mv model.ckpt-1400000.meta bert_model.ckpt.meta
       mv model.ckpt-1400000.data-00000-of-00001 bert_model.ckpt.data-00000-of-00001
       cut -f1 wiki-ja.vocab | sed -e "1 s/<unk>/[UNK]/g" > vocab.txt
       pip install --upgrade
       pip install tensorflow-gpu
       pip install bert-serving-server
       pip install bert-serving-client
   ```

   bert-as-service/bert_config.json

   ```
   {
       "attention_probs_dropout_prob" : 0.1,
       "hidden_act" : "gelu",
       "hidden_dropout_prob" : 0.1,
       "hidden_size" : 768,
       "initializer_range" : 0.02,
       "intermediate_size" : 3072,
       "max_position_embeddings" : 512,
       "num_attention_heads" : 12,
       "num_hidden_layers" : 12,
       "type_vocab_size" : 2,
       "vocab_size" : 32000
   }
   ```

4. bert-as-service の中で

   ```
   bert-serving-start -model_dir ./bert-jp -num_worker=4
   ```

   を実行する。(立ち上がりまで 5 分くらいかかるかもです)
   ここでエラーが起こる場合は tensorflow のバージョンなどを確認してください

5. brigade-visualizer に戻って、client.py を実行する
