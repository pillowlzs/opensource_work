import plotly.graph_objects as go
import numpy as np

def generate_sphere(radius=1, num_points=50):
    u = np.linspace(0, 2 * np.pi, num_points)
    v = np.linspace(0, np.pi, num_points)
    x = radius * np.outer(np.cos(u), np.sin(v))
    y = radius * np.outer(np.sin(u), np.sin(v))
    z = radius * np.outer(np.ones(np.size(u)), np.cos(v))
    return x, y, z

x, y, z = generate_sphere(radius=2, num_points=50)

# 创建 3D 表面图对象
fig = go.Figure(data=[go.Surface(
    x=x,
    y=y,
    z=z
)])

fig.update_layout(
    title='3D 球体示例',
    scene=dict(
        xaxis_title='X 轴',
        yaxis_title='Y 轴',
        zaxis_title='Z 轴'
    )
)
fig.show()