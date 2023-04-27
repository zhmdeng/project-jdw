


import pandas as pd
import jieba


data = pd.read_excel(r'E:\评论\店透视_评论分析_100005527962.xlsx')


data.head()

data['cut'] = data['首次评价'].apply(lambda x : list(jieba.cut(x)))

print(data.head())


stopwords = pd.read_csv('StopwordsCN.txt', encoding='utf8', names=['stopword'], index_col=False)

print(stopwords.head())

stop_list = stopwords['stopword'].tolist()


data['cut'] = data['首次评价'].apply(lambda x : [i for i in jieba.cut(x) if i not in stop_list])

print(data.head(10))


# 将所有的分词合并
words = []

for content in data['cut']:
    words.extend(content)
# 创建分词数据框
corpus = pd.DataFrame(words, columns=['word'])
corpus['cnt'] = 1


g = corpus.groupby(['word']).agg({'cnt': 'count'}).sort_values('cnt', ascending=False)

print(g.head(70))
print(type(g))
g = pd.DataFrame(g)
g.to_csv(r'E:\评论\评论分析3.xls',encoding='utf-8-sig')


