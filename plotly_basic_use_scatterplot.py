import plotly.express as px
import pandas as pd

#创建演示数据
df = pd.DataFrame({
    'date': ['2025-01-01', '2025-01-02', '2025-01-03', '2023-05-04'],
    'product':['A','A','B','C'],
    'amount': [20, 40, 30, 26],
    'cost': [3, 6, 2, 10]
})
df['roi'] = df['amount'] / df['cost']

# 创建散点图
fig = px.scatter(df, x='cost', y='amount',color='product', size='roi',title='Scatter Plot')
fig.show()

