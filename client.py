import numpy as np
import parser
import sentencepiece as spm
import MeCab
from bert_serving.client import BertClient
bc = BertClient(ip='0.0.0.0')


s = spm.SentencePieceProcessor()
s.Load('../bert-as-service/bert-jp/wiki-ja.model')


def parse(text):
    text = text.lower()
    return s.EncodeAsPieces(text)


def mplg(doc):
    '''
    str->str
    文書から名詞だけを抽出する
    '''
    word_list = ""
    m = MeCab.Tagger()
    m_doc = m.parse(doc)
    for row in m_doc.split("\n"):
        word = row.split("\t")[0]  # タブ区切りになっている１つ目を取り出す。ここには形態素が格納されている
        if word == "EOS":
            break
        else:
            pos = row.split("\t")[1]  # タブ区切りになっている2つ目を取り出す。ここには品詞が格納されている
            slice = pos[:2]
            if slice == "名詞":
                word_list = word_list + " " + word
    return word_list


urls = {
    'Sapporo': 'http://www.codeforsapporo.org/',
    'Muroran': 'https://ja.localwiki.org/mr/Code_for_Muroran',
    'Hakodate': 'https://codeforhakodate.org/',
    'Aomori': 'https://codeforaomori.wixsite.com/site',
    'Akita': 'https://code4akita.org/',
    'Sendai': 'https://code4sendai.org/',
    'Aizu': 'http://aizu.io/',
    'Niigata': 'https://www.codeforniigata.org/',
    'Ibaraki': 'https://codeforibaraki.org/',
    'Saitama': 'http://www.code4saitama.org/',
    'Kumagaya': 'http://code4kumagaya.org/',
    'Toda': 'https://codefortoda.org/',
    'Ichikawa': 'http://codeforichikawa.org/',
    'Chiba': 'http://www.code4chiba.org/',
    'Nagareyama': 'http://www.code-for-nagareyama.org/',
    'Funabashi': 'http://code4funabashi.org/',
    'Matsudo': 'https://code4matsudo.org/',
    'Tokyo': 'https://codefor.tokyo/',
    'Adachi': 'https://code4adachi.org/',
    'Shinagawa': 'https://code4shinagawa.org/',
    'Chuo': 'http://c4chuo.mystrikingly.com/',
    'Hachioji': 'http://code4hachioji.org/',
    'OpenKawasaki': 'https://www.openkawasaki.org/',
    'Takaoka': 'http://code4takaoka.org/',
    'Kanazawa': 'http://codeforkanazawa.org/',
    'Aichi': 'https://www.code4aichi.org/',
    'Nagoya': 'https://code4.nagoya/',
    'Uzura': 'https://uzura.org/',
    'Gifu': 'https://codeforgifu.jp/',
    'Kusatsu': 'https://codeforkusatsu.org/',
    'Nara': 'http://code4nara.org/',
    'YamatoKoriyama': 'https://code4yk.jimdofree.com/',
    'Ikoma': 'https://www.code4ikoma.org/',
    'Osaka': 'https://code4.osaka/',
    'Amagasaki': 'https://c4ama.wordpress.com/',
    'Kobe': 'https://codeforkobe.github.io/',
    'Tamba': 'https://opendata.tamba.city/',
    'Kurashiki': 'http://code4kurashiki.org/',
    'Hiroshima': 'https://www.code4hiroshima.org/',
    'Kitakyusyu': 'https://www.code4kitakyushu.org/',
    'Kurume': 'http://code4kurume.org/',
    'Saga': 'http://code4saga.org/',
    'Okinawa': 'https://code4okinawa.org/'
}

tech_keywords = [
    'GIS・位置空間情報',
    'IoT',
    'SNS',
    'Wikipedia・Wikidata',
    'オープンデータ',
    'グラレコ・ファシリテーション',
    'ゲーム',
    'スマートスピーカー',
    'チャットボット',
    'ドローン',
    'ノーコード',
    'プログラミング',
    'ロボット',
    '可視化',
    '機械学習',
    '通信（5G, LoRa）'
]

social_issue_keywords = [
    'COVID-19',
    'LGBTQ・ジェンダー',
    'SDGs',
    'まちづくり',
    '異文化交流',
    '医療',
    '宇宙',
    '河川',
    '環境',
    '観光',
    '官民協働',
    '教育',
    '漁業',
    '教育',
    '健康',
    '交通',
    '公園',
    '公共施設',
    '高齢者支援',
    '港湾',
    '産業',
    '市民活動連携・地域活動連携',
    '子育て',
    '住宅',
    '障害者支援',
    '上下水道',
    '食',
    '政治',
    '生活',
    '地域アーカイブ',
    '都市計画',
    '土地',
    '道路',
    '農業',
    '福祉',
    '文化',
    '防災',
    '防犯',
    '林業'
]


if __name__ == "__main__":
    # ブリゲードのurlから取得の場合
    data = list(urls.items())
    docs = [parser.parse(name_url[1]) for name_url in data]
    texts = []
    # texts = tech_keywords #tech_keywordsの場合
    # texts = social_issue_keywords #社会課題keywordsの場合
    for i, doc in enumerate(docs):
        texts.append(mplg(doc))
    parsed_texts = list(map(parse, texts))
    vecs = bc.encode(parsed_texts, is_tokenized=True)
    np.save('./data/brigade_homepages', vecs)
