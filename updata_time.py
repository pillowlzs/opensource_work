import matplotlib.pyplot as plt
import pandas as pd

# 读取文件
df = pd.read_csv('releases_info.csv')

# 提取版本和对应时间列的数据
version_column = 'Tag Name'
time_column = 'Published at'
data = df[[version_column, time_column]].values.tolist()

# 将数据转换为 DataFrame
df = pd.DataFrame(data, columns=['Version', 'Release_Time'])

# 将 Release_Time 列转换为 datetime 类型
df['Release_Time'] = pd.to_datetime(df['Release_Time'])

# 按发布时间排序
df = df.sort_values(by='Release_Time')

# 设置图片清晰度
plt.rcParams['figure.dpi'] = 300

# 设置画布大小
plt.figure(figsize=(12, 8))

# 绘制版本发布时间线
plt.plot(df['Release_Time'], df['Version'], marker='o', linestyle='-', color='b')

# 添加数据标签
for x, y in zip(df['Release_Time'], df['Version']):
    plt.annotate(y, (x, y), textcoords='offset points', xytext=(0,10), ha='center')

# 设置图表标题和坐标轴标签
plt.title('Plotly time route')
plt.xlabel('time')
plt.xticks(rotation=45)
plt.ylabel('number')

# 显示图表
plt.tight_layout()
plt.show()