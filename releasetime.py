import pandas as pd
import plotly.express as px

# 1. 读取CSV文件
df = pd.read_csv(r'E:\04college\opensource\releases_info.csv')  # 使用文件的正确路径

# 2. 确保 'Published at' 列为日期类型，保持时区信息
df['Published at'] = pd.to_datetime(df['Published at'], errors='coerce', utc=True)

# 3. 按月进行分组，统计每个月发布的版本数
# 先将日期转换为 Period，再将其转换为 datetime，并本地化为 UTC 时区
df['release_month'] = df['Published at'].dt.to_period('M').dt.start_time

# 4. 统计每个月的版本数量
release_count = df.groupby('release_month').size().reset_index(name='release_count')

# 5. 生成完整的月份列表（从最早的日期到最新的日期）
start_date = df['Published at'].min().replace(day=1)  # 最早的日期的月份
end_date = df['Published at'].max().replace(day=1)  # 最新的日期的月份
all_months = pd.date_range(start=start_date, end=end_date, freq='MS', tz='UTC')

# 6. 创建一个包含所有月份的DataFrame
all_months_df = pd.DataFrame(all_months, columns=['release_month'])

# 7. 通过 .normalize() 去除时分秒部分，确保精度一致
all_months_df['release_month'] = all_months_df['release_month'].dt.normalize()

# 打印数据框查看结果
print("All Months DataFrame:")
print(all_months_df.head())  # 打印前5行

print("Release Count DataFrame:")
print(release_count.head())  # 打印前5行

# 8. 确保 release_count['release_month'] 也精确到年月部分，并且本地化为 UTC 时区
release_count['release_month'] = release_count['release_month'].dt.tz_localize('UTC')

# 9. 将版本发布数据与所有月份数据合并，确保没有发布版本的月份填充为0
release_count_full = pd.merge(all_months_df, release_count, on='release_month', how='left').fillna(0)

# 10. 使用plotly绘制可视化
fig = px.line(release_count_full,
              x='release_month', 
              y='release_count',
              title='Plotly Version Releases Over Time',
              labels={'release_month': 'Release Month', 'release_count': 'Number of Releases'},
              line_shape='linear',
              markers=True)

# 11. 美化图表
fig.update_traces(line=dict(color='royalblue', width=4),
                  marker=dict(size=8, color='red', symbol='circle'))
fig.update_layout(
    title_font_size=20,
    xaxis_title_font_size=14,
    yaxis_title_font_size=14,
    plot_bgcolor='white',
    xaxis=dict(tickangle=45),
    yaxis=dict(
        showgrid=True, 
        gridwidth=1, 
        gridcolor='lightgray', 
        rangemode='tozero'  # 强制纵轴从0开始
    ),
    template='plotly_dark'
)

# 12. 展示图表
fig.show()
