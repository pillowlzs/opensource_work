import plotly.graph_objects as go
import pandas as pd
import numpy as np
import plotly.express as px
from dash import Dash, dcc, html, Input, Output

# 生成模拟数据
np.random.seed(42)
data = {
    'date': pd.date_range('2023-01-01', periods=100),
    'product': np.random.choice(['Product A', 'Product B', 'Product C', 'Product D'], 100),
  'region': np.random.choice(['East', 'West', 'North', 'South'], 100),
  'sales': np.random.randint(100, 1000, 100)
}
df = pd.DataFrame(data)

# 初始化Dash应用
app = Dash(__name__)

# 布局设置
app.layout = html.Div([
    html.H1("Sales Data Analysis Dashboard"),
    dcc.Dropdown(
        id='product-dropdown',
        options=[{'label': i, 'value': i} for i in df['product'].unique()],
        value=df['product'].unique()[0]
    ),
    dcc.Dropdown(
        id='region-dropdown',
        options=[{'label': i, 'value': i} for i in df['region'].unique()],
        value=df['region'].unique()[0]
    ),
    html.Button('Update Charts', id='update-button'),
    dcc.Graph(id='scatter-plot'),
    dcc.Graph(id='bar-plot'),
    dcc.Graph(id='line-plot')
])


# 回调函数，更新散点图
@app.callback(
    Output('scatter-plot', 'figure'),
    Input('update-button', 'n_clicks'),
    Input('product-dropdown', 'value'),
    Input('region-dropdown', 'value')
)
def update_scatter_plot(n_clicks, selected_product, selected_region):
    filtered_df = df[(df['product'] == selected_product) & (df['region'] == selected_region)]
    fig = px.scatter(filtered_df, x='date', y='sales', title=f'Sales Scatter Plot for {selected_product} in {selected_region}')
    return fig


# 回调函数，更新柱状图
@app.callback(
    Output('bar-plot', 'figure'),
    Input('update-button', 'n_clicks'),
    Input('product-dropdown', 'value'),
    Input('region-dropdown', 'value')
)
def update_bar_plot(n_clicks, selected_product, selected_region):
    filtered_df = df[(df['product'] == selected_product) & (df['region'] == selected_region)]
    monthly_sales = filtered_df.groupby(pd.Grouper(key='date', freq='M'))['sales'].sum()
    fig = go.Figure(data=[go.Bar(x=monthly_sales.index, y=monthly_sales.values)])
    fig.update_layout(title=f'Monthly Sales Bar Plot for {selected_product} in {selected_region}')
    return fig


# 回调函数，更新折线图
@app.callback(
    Output('line-plot', 'figure'),
    Input('update-button', 'n_clicks'),
    Input('product-dropdown', 'value'),
    Input('region-dropdown', 'value')
)
def update_line_plot(n_clicks, selected_product, selected_region):
    filtered_df = df[(df['product'] == selected_product) & (df['region'] == selected_region)]
    daily_sales = filtered_df.groupby('date')['sales'].sum()
    fig = go.Figure(data=[go.Line(x=daily_sales.index, y=daily_sales.values)])
    fig.update_layout(title=f'Daily Sales Line Plot for {selected_product} in {selected_region}')
    return fig


if __name__ == '__main__':
    app.run_server(debug=True)