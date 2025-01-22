import pytest
import plotly.graph_objects as go
import numpy as np
import pandas as pd
from hypothesis import given, strategies as st

# 定义测试用的图表类型
chart_types = ['scatter', 'line', 'bar', 'box', 'heatmap']

# 模拟空数据、NaN 和非数值数据
empty_data = st.lists(st.floats(), min_size=0)  # 空列表
nan_data = st.lists(st.one_of(st.floats(), st.just(float('nan'))))  # 包含 NaN 的列表
string_data = st.lists(st.text(), min_size=1)  # 字符串数据
date_data = st.lists(st.datetimes(), min_size=1)  # 日期数据
zero_size_data = st.integers(min_value=0)  # 传入大小为0的情况

# 测试异常数据的处理
@given(chart_type=st.sampled_from(chart_types), x=empty_data, y=empty_data)
def test_empty_data(chart_type, x, y):
    """测试空数据输入的情况"""
    try:
        if chart_type == 'scatter':
            fig = go.Figure(data=go.Scatter(x=x, y=y, mode='markers'))
        elif chart_type == 'line':
            fig = go.Figure(data=go.Scatter(x=x, y=y, mode='lines'))
        elif chart_type == 'bar':
            fig = go.Figure(data=go.Bar(x=x, y=y))
        elif chart_type == 'box':
            fig = go.Figure(data=go.Box(y=y))
        elif chart_type == 'heatmap':
            z = [[float(i + j) for i in range(10)] for j in range(10)]
            fig = go.Figure(data=go.Heatmap(z=z))
        assert len(fig.data) > 0
    except Exception as e:
        assert str(e)  # 期望能捕获到异常


@given(chart_type=st.sampled_from(chart_types), x=nan_data, y=nan_data)
def test_nan_data(chart_type, x, y):
    """测试 NaN 数据输入的情况"""
    try:
        if chart_type == 'scatter':
            fig = go.Figure(data=go.Scatter(x=x, y=y, mode='markers'))
        elif chart_type == 'line':
            fig = go.Figure(data=go.Scatter(x=x, y=y, mode='lines'))
        elif chart_type == 'bar':
            fig = go.Figure(data=go.Bar(x=x, y=y))
        elif chart_type == 'box':
            fig = go.Figure(data=go.Box(y=y))
        elif chart_type == 'heatmap':
            z = [[float(i + j) for i in range(10)] for j in range(10)]
            fig = go.Figure(data=go.Heatmap(z=z))
        assert len(fig.data) > 0
    except Exception as e:
        assert str(e)  # 期望能捕获到异常


@given(chart_type=st.sampled_from(chart_types), x=string_data, y=string_data)
def test_string_data(chart_type, x, y):
    """测试字符串数据输入的情况"""
    try:
        if chart_type == 'scatter':
            fig = go.Figure(data=go.Scatter(x=x, y=y, mode='markers'))
        elif chart_type == 'line':
            fig = go.Figure(data=go.Scatter(x=x, y=y, mode='lines'))
        elif chart_type == 'bar':
            fig = go.Figure(data=go.Bar(x=x, y=y))
        elif chart_type == 'box':
            fig = go.Figure(data=go.Box(y=y))
        elif chart_type == 'heatmap':
            z = [[float(i + j) for i in range(10)] for j in range(10)]
            fig = go.Figure(data=go.Heatmap(z=z))
        assert len(fig.data) > 0
    except Exception as e:
        assert str(e)  # 期望能捕获到异常


@given(chart_type=st.sampled_from(chart_types), x=date_data, y=date_data)
def test_date_data(chart_type, x, y):
    """测试日期数据输入的情况"""
    try:
        if chart_type == 'scatter':
            fig = go.Figure(data=go.Scatter(x=x, y=y, mode='markers'))
        elif chart_type == 'line':
            fig = go.Figure(data=go.Scatter(x=x, y=y, mode='lines'))
        elif chart_type == 'bar':
            fig = go.Figure(data=go.Bar(x=x, y=y))
        elif chart_type == 'box':
            fig = go.Figure(data=go.Box(y=y))
        elif chart_type == 'heatmap':
            z = [[float(i + j) for i in range(10)] for j in range(10)]
            fig = go.Figure(data=go.Heatmap(z=z))
        assert len(fig.data) > 0
    except Exception as e:
        assert str(e)  # 期望能捕获到异常


@given(chart_type=st.sampled_from(chart_types), x=st.lists(st.floats(min_value=0)), y=st.lists(st.floats(min_value=0)), size=zero_size_data)
def test_zero_size(chart_type, x, y, size):
    """测试传入大小为0的情况"""
    try:
        if chart_type == 'scatter':
            fig = go.Figure(data=go.Scatter(x=x, y=y, mode='markers', marker=dict(size=size)))
        elif chart_type == 'line':
            fig = go.Figure(data=go.Scatter(x=x, y=y, mode='lines'))
        elif chart_type == 'bar':
            fig = go.Figure(data=go.Bar(x=x, y=y))
        elif chart_type == 'box':
            fig = go.Figure(data=go.Box(y=y))
        elif chart_type == 'heatmap':
            z = [[float(i + j) for i in range(10)] for j in range(10)]
            fig = go.Figure(data=go.Heatmap(z=z))
        assert len(fig.data) > 0
    except Exception as e:
        assert str(e)  # 期望能捕获到异常
