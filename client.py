import sentencepiece as spm
from bert_serving.client import BertClient
bc = BertClient(ip='0.0.0.0')

s = spm.SentencePieceProcessor()
s.Load('../bert-as-service/bert-jp/wiki-ja.model')


def parse(text):
    text = text.lower()
    return s.EncodeAsPieces(text)


texts = ['液体の水は、惑星上における生命の前提条件である。',
         '火星は地球型惑星に分類される。']

parsed_texts = list(map(parse, texts))

print(bc.encode(parsed_texts, is_tokenized=True))
