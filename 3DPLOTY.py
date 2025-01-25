import plotly.graph_objects as go
import numpy as np

# 生成数据
x = np.linspace(-5, 5, 50)
y = np.linspace(-5, 5, 50)
x, y = np.meshgrid(x, y)
z = np.sin(np.sqrt(x**2 + y**2))

# 创建 3D 曲面图
surface = go.Surface(z=z, x=x, y=y, colorscale='Viridis', opacity=0.7)

# 创建 3D 散点数据
scatter_x = np.random.uniform(-5, 5, 100)
scatter_y = np.random.uniform(-5, 5, 100)
scatter_z = np.sin(np.sqrt(scatter_x**2 + scatter_y**2))

scatter = go.Scatter3d(x=scatter_x, y=scatter_y, z=scatter_z, mode='markers',
                       marker=dict(size=5, color='red', opacity=0.8))

# 设置布局
layout = go.Layout(
    title='复杂的 3D 图像绘制',
    scene=dict(
        xaxis_title='X',
        yaxis_title='Y',
        zaxis_title='Z',
        aspectmode='cube'
    ),
    showlegend=False
)

# 将图形元素组合在一起
fig = go.Figure(data=[surface, scatter], layout=layout)

# 显示图像
fig.show()
