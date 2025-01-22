import plotly.graph_objects as go
from hypothesis import given, strategies as st

# 定义策略
chart_types = st.sampled_from(['scatter', 'bar', 'line', 'box', 'heatmap'])
x_strategy = st.lists(st.floats(), min_size=1, max_size=10)
y_strategy = st.lists(st.floats(), min_size=1, max_size=10)
size_strategy = st.integers(min_value=1, max_value=10)

@given(chart_type=chart_types, x=x_strategy, y=y_strategy, size=size_strategy)
def test_plotly_chart(chart_type, x, y, size):
    """
    模糊测试不同类型的 Plotly 图表
    """
    # 强制确保 x 和 y 的长度一致
    if len(x) != len(y):
        min_len = min(len(x), len(y))
        x = x[:min_len]  # 截取 x 的前 min_len 个元素
        y = y[:min_len]  # 截取 y 的前 min_len 个元素

    # 创建图表
    if chart_type == 'scatter':
        fig = go.Figure(data=go.Scatter(x=x, y=y, mode='markers', marker=dict(size=size)))
    elif chart_type == 'bar':
        fig = go.Figure(data=go.Bar(x=x, y=y))
    elif chart_type == 'line':
        fig = go.Figure(data=go.Scatter(x=x, y=y, mode='lines'))
    elif chart_type == 'box':
        fig = go.Figure(data=go.Box(y=y))
    elif chart_type == 'heatmap':
        z = [[float(i + j) for i in range(10)] for j in range(10)]  # 创建简单的热力图数据
        fig = go.Figure(data=go.Heatmap(z=z))

    # 检查图表数据是否正确生成
    assert len(fig.data) > 0  # 确保图表有数据
    if chart_type in ['scatter', 'line']:
        # 对于 scatter 和 line 类型，确保 x 和 y 的长度相同
        assert len(fig.data[0].x) == len(fig.data[0].y)
    elif chart_type == 'box':
        # 对于 box 图，检查 y 数据长度
        assert len(fig.data[0].y) > 0
    elif chart_type == 'heatmap':
        # 对于 heatmap，检查 z 数据维度
        assert len(fig.data[0].z) > 0

    # 确保图表类型正确
    if chart_type == 'line':
        # 对于 'line' 类型图表，检查 mode 是否是 'lines'
        assert fig.data[0].mode == 'lines'
    else:
        # 对于其他类型的图表，检查 type 是否正确
        assert fig.data[0].type == chart_type
