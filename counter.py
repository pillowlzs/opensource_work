import re
import pandas as pd
from nltk.tokenize import word_tokenize
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import nltk

# 下载punkt资源，用于英文分词
nltk.download('punkt')

# 读取停用词文件，每行一个停用词，存储为列表
with open('stopwords.txt', 'r') as f:
    stopwords = [line.strip() for line in f.readlines()]

# 存储错误信息和出现次数的字典
error_dict = {}

# 逐行读取文件内容
with open('releases_info.txt', 'r') as file:
    for line in file:
        # 检查是否包含 "Fixed" 关键字
        if 'Fixed' in line:
            # 使用正则表达式提取错误描述部分
            match = re.search(r'Fixed.*', line)
            if match:
                error_description = match.group(0)[6:].strip()
                # 英文分词
                words = word_tokenize(error_description.lower())
                for word in words:
                    # 过滤停用词
                    if word not in stopwords:
                        # 更新错误信息字典
                        if word in error_dict:
                            error_dict[word] += 1
                        else:
                            error_dict[word] = 1

# 将错误信息和出现次数转换为 DataFrame
df = pd.DataFrame(list(error_dict.items()), columns=['Error', 'Frequency'])

# 生成词云图
wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(error_dict)

# 绘制词云图
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()

# 输出统计结果表格
print(df)