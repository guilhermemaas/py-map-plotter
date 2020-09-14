import plotly.graph_objects as go
#<
#https://plotly.com/python/
#https://dash.plotly.com/basic-callbacks
#https://dash-gallery.plotly.host/Portal/

mapbox_access_token = open("mapbox_token.txt").read()

fig = go.Figure(go.Scattermapbox(
    lat=[
        '-26.819624',
        '-26.820047',
        '-26.820334',
        '-26.821081',
        '-26.819817',
        '-26.819702',
        '-26.821770',
        '-26.819874'
        ],
    lon=[
        '-49.272977'
        '-49.275375',
        '-49.273293',
        '-49.275160',
        '-49.276126',
        '-49.275611',
        '-49.276405',
        '-49.276898',
        ],
    mode='markers',
    marker=go.scattermapbox.Marker(
        size=9,
        color='#34D822'
    ),
    text=["The coffee bar","Bistro Bohem","Black Cat",
             "Snap","Columbia Heights Coffee","Azi's Cafe",
             "Blind Dog Cafe","Le Caprice","Filter"],
))

fig.update_layout(
    autosize=True,
    hovermode='closest',
    mapbox=dict(
        accesstoken=mapbox_access_token,
        bearing=0,
        center=go.layout.mapbox.Center(
            lat=-26.819788,
            lon=-49.272934
            #lat=45,
            #lon=-73
            #-26.819788, -49.272934
        ),
        style='dark',
        pitch=0,
        zoom=10
    )
)

fig.show()