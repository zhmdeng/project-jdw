# 导入模块
from wordcloud import WordCloud
import pandas as pd
# 文本数据
# text = 'he speak you most bueatiful time Is he first meeting you'
# data = pd.read_csv(r'E:\评论\table.xls',encoding='utf-8-sig')
data = pd.read_excel(r'E:\评论\店透视_评论分析_100005527962.xlsx')
# 准备禁用词，需要为set类型
stopwords = pd.read_csv('StopwordsCN.txt', encoding='utf8',index_col=False)
# 设置参数，创建WordCloud对象
wc = WordCloud(
    width=200,                  # 设置宽为400px
    height=150,                 # 设置高为300px
    background_color='white',    # 设置背景颜色为白色
    stopwords=stopwords,         # 设置禁用词，在生成的词云中不会出现set集合中的词
    max_font_size=100,
    min_font_size=10,
    max_words=10,
    scale=2
)
# 根据文本数据生成词云
print(wc)
wc.generate(data['首次评价'])
# 保存词云文件
wc.to_file('img.jpg')