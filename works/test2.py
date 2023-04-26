

import jieba
from jieba.analyse import extract_tags



# 导入相关库
import pandas as pd
import jieba

# 读取数据
data = pd.read_excel(r'E:\评论\店透视_评论分析_100005527962.xlsx')

# 查看数据
data.head()
# 生成分词
data['cut'] = data['首次评价'].apply(lambda x : list(jieba.cut(x)))

print(data.head())

# 读取停用词数据
stopwords = pd.read_csv('StopwordsCN.txt', encoding='utf8', names=['stopword'], index_col=False)

print(stopwords.head())
# 转化词列表
stop_list = stopwords['stopword'].tolist()

# 去除停用词
data['cut'] = data['首次评价'].apply(lambda x : [i for i in jieba.cut(x) if i not in stop_list])

print(data.head(10))


# 将所有的分词合并
words = []

for content in data['cut']:
    words.extend(content)
# 创建分词数据框
corpus = pd.DataFrame(words, columns=['word'])
corpus['cnt'] = 1

# 分组统计
g = corpus.groupby(['word']).agg({'cnt': 'count'}).sort_values('cnt', ascending=False)

print(g.head(70))
print(type(g))
g = pd.DataFrame(g)
g.to_csv(r'E:\评论\评论分析3.xls',encoding='utf-8-sig')


