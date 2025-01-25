import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np
from datetime import datetime, timedelta


# 生成模拟交通流量数据
traffic_dates = pd.date_range(start='2024 - 01 - 01', end='2024 - 01 - 31', freq='h')
traffic_stations = ['Station A', 'Station B', 'Station C', 'Station D']
traffic_data = {
    'date': np.repeat(traffic_dates, len(traffic_stations)),
  'station': np.tile(traffic_stations, len(traffic_dates)),
    'traffic_flow': np.random.randint(100, 1000, len(traffic_dates) * len(traffic_stations))
}
traffic_df = pd.DataFrame(traffic_data)


# 生成模拟污染指数数据
pollution_dates = pd.date_range(start='2024 - 01 - 01', end='2024 - 01 - 31', freq='4h')
pollution_stations = ['Pollution Station X', 'Pollution Station Y']
pollution_data = {
    'date': np.repeat(pollution_dates, len(pollution_stations)),
  'station': np.tile(pollution_stations, len(pollution_dates)),
    'pollution_index': np.random.uniform(0, 100, len(pollution_dates) * len(pollution_stations))
}
pollution_df = pd.DataFrame(pollution_data)


# 创建初始图表布局
fig = go.Figure()

# 添加交通流量折线图
for station in traffic_stations:
    station_data = traffic_df[traffic_df['station'] == station]
    fig.add_trace(go.Scatter(
        x = station_data['date'],
        y = station_data['traffic_flow'],
        mode = 'lines+markers',
        name = f'Traffic Flow - {station}',
        visible = False
    ))

# 添加污染指数柱状图
for station in pollution_stations:
    station_data = pollution_df[pollution_df['station'] == station]
    fig.add_trace(go.Bar(
        x = station_data['date'],
        y = station_data['pollution_index'],
        name = f'Pollution Index - {station}',
        visible = False
    ))


# 创建时间范围滑块
sliders = [
    {
        'active': 0,
        'yanchor': 'top',
        'xanchor': 'left',
        'currentvalue': {
            'font': {'size': 20},
            'prefix': 'Time:',
            'visible': True,
            'xanchor': 'right'
        },
        'transition': {'duration': 300, 'easing': 'cubic - in - out'},
        'pad': {'b': 10, 't': 50},
        'len': 0.9,
        'x': 0.1,
        'y': 0,
      'steps': []
    }
]

# 创建按钮用于切换图表类型
buttons = [
    {
        'label': 'Traffic Flow',
      'method': 'update',
        'args': [
            {'visible': [True if 'Traffic Flow' in trace.name else False for trace in fig.data]},
            {'title': 'Traffic Flow Over Time'}
        ]
    },
    {
        'label': 'Pollution Index',
      'method': 'update',
        'args': [
            {'visible': [True if 'Pollution Index' in trace.name else False for trace in fig.data]},
            {'title': 'Pollution Index Over Time'}
        ]
    }
]


# 创建动态更新的帧
frames = []
for i in range(len(traffic_dates)):
    frame_traffic = []
    for station in traffic_stations:
        station_data = traffic_df[(traffic_df['station'] == station) & (traffic_df['date'] <= traffic_dates[i])]
        frame_traffic.append(go.Scatter(
            x = station_data['date'],
            y = station_data['traffic_flow'],
            mode = 'lines+markers',
            name = f'Traffic Flow - {station}'
        ))

    frame_pollution = []
    for station in pollution_stations:
        station_data = pollution_df[(pollution_df['station'] == station) & (pollution_df['date'] <= traffic_dates[i])]
        frame_pollution.append(go.Bar(
            x = station_data['date'],
            y = station_data['pollution_index'],
            name = f'Pollution Index - {station}'
        ))

    frame = go.Frame(data = frame_traffic + frame_pollution, name = traffic_dates[i].strftime('%Y - %m - %d %H:%M:%S'))
    frames.append(frame)

    step = {
      'method': 'animate',
        'args': [
            [traffic_dates[i].strftime('%Y - %m - %d %H:%M:%S')],
            {'frame': {'duration': 300, 'easing': 'linear'},'mode': 'immediate'}
        ],
        'label': traffic_dates[i].strftime('%Y - %m - %d %H:%M:%S')
    }
    sliders[0]['steps'].append(step)


# 更新图表布局
fig.update_layout(
    sliders = sliders,
    updatemenus = [
        {
            'buttons': buttons,
            'direction': 'left',
            'pad': {'r': 10, 't': 10},
            'type': 'buttons',
            'x': 0.1,
            'xanchor': 'left',
            'y': 1.1,
            'yanchor': 'top'
        }
    ],
    title = 'City Traffic and Pollution Analysis',
    xaxis_title = 'Time',
    yaxis_title = 'Value',
    hovermode = 'x unified'
)


# 添加动画控制按钮
fig.update_layout(
    updatemenus = [
        {
            'type': 'buttons',
            'buttons': [
                {
                    'label': 'Play',
                  'method': 'animate',
                    'args': [None, {'frame': {'duration': 300,'redraw': True}, 'fromcurrent': True}]
                },
                {
                    'label': 'Pause',
                  'method': 'animate',
                    'args': [[None], {'frame': {'duration': 0,'redraw': False},'mode': 'immediate'}]
                }
            ]
        }
    ]
)


fig.frames = frames

# 显示图表
fig.show()
