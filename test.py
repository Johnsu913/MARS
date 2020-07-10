import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
df = pd.read_csv('Base.csv')

Time = df[' TimeSinceLoad(s)']
XShimmer = df['X (Shimmer)']
YShimmer = df['Y (Shimmer)']
ZShimmer = df['Z (Shimmer)']
SkinConductance = df['Skin Conductance']
SkinResistance = df['Skin Resistance']
PPG = df['PPG']
HRV = df['HRV']
HeartRate = df['Heart Rate']
fig = go.Figure()
fig.add_trace(go.Scatter(x=Time, y=XShimmer, name='X (Shimmer)',
                        line=dict(color='firebrick', width=4)))
fig.add_trace(go.Scatter(x=Time, y=YShimmer, name = 'Y (Shimmer)',
                        line=dict(color='royalblue', width=4)))
fig.add_trace(go.Scatter(x=Time, y=ZShimmer, name='Z (Shimmer)',
                        line=dict(color='green', width=4,
                            dash='dash')))
fig.update_layout(title='XYZ Shimmers vs TimeSinceLoad',
                   xaxis_title='Time(s)',
                   yaxis_title='Shimmer')
                   
fig.show()

fig2 = go.Figure()

fig2.add_trace(go.Scatter(x=Time, y=PPG, name='PPG',
                        line=dict(color='firebrick', width=4)))
fig2.add_trace(go.Scatter(x=Time, y=HRV, name = 'HRV',
                        line=dict(color='royalblue', width=4)))
fig2.add_trace(go.Scatter(x=Time, y=HeartRate, name='Heart Rate',
                        line=dict(color='green', width=4,
                            dash='dash')))
fig2.update_layout(title='values vs TimeSinceLoad',
                   xaxis_title='Time(s)',
                   yaxis_title='values')

fig2.show()
