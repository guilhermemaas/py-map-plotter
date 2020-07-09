import chart_studio.plotly as py
import plotly.graph_objs as go
import plotly
import pandas as pd

# setting user, api key and access token
#py.tools.set_credentials_file(username='guilhermemaas', api_key='')
#mapbox_access_token = ''

data = []
for event in range(0, 10):
    event_data = dict(
            lat = -26.829782,
            lon = -49.2785357,
            name = event,
            marker = dict(size = 8, opacity = 0.5),
            type = 'scattermapbox'
        )
    data.append(event_data)
print(data)
"""
layout = dict(
    height = 800,
    # top, bottom, left and right margins
    margin = dict(t = 0, b = 0, l = 0, r = 0),
    font = dict(color = '#FFFFFF', size = 11),
    paper_bgcolor = '#000000',
    mapbox = dict(
        # here you need the token from Mapbox
        accesstoken = mapbox_access_token,
        bearing = 0,
        # where we want the map to be centered
        center = dict(
            lat = 38,
            lon = -94
        ),
        # we want the map to be "parallel" to our screen, with no angle
        pitch = 0,
        # default level of zoom
        zoom = 3,
        # default map style
        style = 'dark'
    )
)
"""