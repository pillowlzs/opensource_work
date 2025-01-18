import plotly.graph_objects as go
import numpy as np
import pandas as pd

# 假设我们有一个DataFrame，包含两个特征'feature1'和'feature2'
# 这里我们使用随机数据作为示例
np.random.seed(0)
data = pd.DataFrame({
    'feature1': np.random.randn(1000),
    'feature2': np.random.randn(1000) + 2
})

# 使用散点图查看特征之间的关系
fig = go.Figure(data=go.Scatter(
    x=data['feature1'],
    y=data['feature2'],
    mode='markers',
    marker=dict(
        color=data['feature2'],  # 设置颜色以区分不同数值
        colorscale='Viridis',    # 使用Viridis颜色比例尺
        showscale=True
    )
))

# 添加标题和轴标签
fig.update_layout(
    title='Data Exploration: Scatter plot of feature1 and feature2',
    xaxis_title='Feature 1',
    yaxis_title='Feature 2'
)

# 显示图表
fig.show()

# 使用直方图查看特征的分布
fig = go.Figure([go.Histogram(x=data['feature1']), go.Histogram(x=data['feature2'])])

# 自定义直方图的布局
fig.update_layout(
    barmode='overlay',
    title='Data Exploration: Histogram of features',
    xaxis_title='Value',
    yaxis_title='Count'
)

# 显示图表
fig.show()
