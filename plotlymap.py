import plotly.graph_objects as go

# ------ Data ------
data = []

scattermapbox = go.Scattermapbox()
data.append(scattermapbox)

# ------ Layout ------
mapbox_kargs = dict(
    zoom=10,
    center=dict(
        lat=30.272934,
        lon=120.147376,
    ),
    style="stamen-terrain",
    accesstoken='!!! replace with your mapbox ak !!!'
)

layout_kargs = dict(
    autosize=False,
    width=1400,
    height=800,
    margin=dict(
        r=0, t=38, l=0, b=0, pad=0
    ),
)

layout = go.Layout(
    mapbox=mapbox_kargs,
    **layout_kargs
)

# ------ Figure ------
fig = go.Figure(
    data=data,
    layout=layout
)

fig.show()