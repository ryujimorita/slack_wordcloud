import csv
import MeCab
import sys
import re
from collections import Counter

# テキストファイル読み込み
with open('<ファイルのパス>', encoding='utf-8') as f:
    data = f.read()

# パース
mecab = MeCab.Tagger('/usr/local/lib/mecab/dic/mecab-ipadic-neologd/')
parse = mecab.parse(data)
lines = parse.split('\n')
items = (re.split('[\t,]', line) for line in lines)


# 動詞をリストに格納
words = [item[0]
for item in items:
    if (item[0] not in ('EOS', '', 't', 'ー') and
    item[1] == '名詞' and item[2] == '一般')]

# 頻度順に出力
counter = Counter(words)
header = ['word','count']

# データをCSVに書き出し
with open('sample_slack.csv','w',newline='',encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    for word, count in counter.most_common():
        writer.writerow([word,count])
