# app.py

from dash import Dash, Input, Output, dcc, html
import plotly.express as px
import plotly.graph_objs as go
import pandas as pd

# Créer une carte de base centrée sur l'île de la Réunion
mapbox_access_token = "pk.eyJ1IjoianVub3Q5NzQwIiwiYSI6ImNsZ2RlYzIyNjBtemUzZm8wbG5odHRmbTcifQ.xHWPxREddhcMx1APXSY-Uw"

data = (
    pd.read_csv("snackbars.csv")
    .assign(lat=lambda data: pd.to_numeric(data["lat"], errors="coerce"))
    .assign(lon=lambda data: pd.to_numeric(data["lon"], errors="coerce"))
    .sort_values(by=["Ville", "Secteur"])
)

villes = data["Ville"].unique()
secteur_str = data["Secteur"].unique()




external_stylesheets = [
    {
        "href": (
            "https://fonts.googleapis.com/css2?"
            "family=Lato:wght@400;700&display=swap"
        ),
        "rel": "stylesheet",
    },
]

app = Dash(__name__, external_stylesheets=external_stylesheets)
app.title = "Snackbars 974"

# Création de la carte
fig = px.scatter_mapbox(data, lat="lat", lon="lon", hover_name="Name", hover_data=["Ville", "Secteur"],
                        zoom=9, 
                        height=730,
                        center={"lat": -21.115141, "lon": 55.536384},)


fig.update_layout(mapbox_style="mapbox://styles/mapbox/outdoors-v12", mapbox_accesstoken=mapbox_access_token)
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

# Création du pie chart
secteurs = data["Secteur"].value_counts()
labels = secteurs.index.tolist()
values = secteurs.tolist()
pie_chart = go.Pie(labels=labels, values=values)

app.layout = html.Div(
    children=[
        html.Div(
            children=[
                html.P(children="🌭", className="header-emoji"),
                html.H1(
                    children="Répartition des Snackbars à La Réunion", 
                    className="header-title"
                ),
                html.P(
                    children=(
                        "Répartition en fonction de la ville et du secteur "
                        " des meilleurs Snackars de La Réunion. Si certains "
                        "Snack venaient à manquer, envoyez moi un message "
                        "sur twitter @ajrunislnd"
                    ),
                    className="header-description",
                ),
            ],
            className="header",
        ),
        html.Div(
            children=[
                html.Div(
                    children=[
                        html.Div(children="Ville", className="menu-title"),
                        dcc.Dropdown(
                            id="ville-filter",
                            options=[
                                {"label": Ville, "value": Ville}
                                for Ville in villes
                            ],
                            value="St Denis",
                            clearable=False,
                            className="dropdown",
                        ),
                    ]
                ),
                html.Div(
                    children=[
                        html.Div(children="Secteur", className="menu-title"),
                        dcc.Dropdown(
                            id="secteur-filter",
                            options=[
                                {
                                    "label": secteur.title(),
                                    "value": secteur,
                                }
                                for secteur in secteur_str
                            ],
                            value="Nord",
                            clearable=False,
                            searchable=False,
                            className="dropdown",
                        ),
                    ],
                ),
            ],
            className="menu",
        ),
        html.Div(
            children=[
                html.Div(
                    children=dcc.Graph(
                        id="map", figure=fig
                    ),
                    className="card",
                ),
                html.Div(
                    children=dcc.Graph(
                        id="pie-chart",
                        figure={
                            "data": [pie_chart],
                            "layout": go.Layout(title="Répartition des snacks par secteur"),
                        },
                    ),
                    className="card",
                ),
            ],
            className="wrapper",
        ),
        html.Footer([
            html.P([
                "Image by ", 
                html.A("Hot-dog icônes créées par Adib Sulthon - Flaticon", href="https://www.flaticon.com/fr/icones-gratuites/hot-dog" , target="_blank")],
                className="footer",),
            
        ]),
    ]
)

@app.callback(
    Output('map', 'figure'),
    Output('pie-chart', 'figure'),
    Input('ville-filter', 'value'),
    Input('secteur-filter', 'value')
)
def update_map(ville, secteur):
    filtered_df = data.query(
        "Ville == @ville and Secteur == @secteur"
    )
    # création de la trace pour la ville sélectionnée
    trace = go.Scattermapbox(
        lat=filtered_df['lat'],
        lon=filtered_df['lon'],
        mode='markers',
        marker=dict(
            size=8,
            opacity=0.8,
        ),
        text=filtered_df['Name'],
        hoverinfo='text'
    )

    # mise à jour de la carte avec la trace de la ville sélectionnée
    fig = go.Figure(
        go.Scattermapbox(
            lat=filtered_df['lat'],
            lon=filtered_df['lon'],
            mode='markers',
            marker=dict(
                size=8,
                opacity=0.8,
            ),
            text=filtered_df['Name'],
            hoverinfo='text'
        )
    )

    fig.update_layout(
        hovermode='closest',
        mapbox=dict(
            accesstoken=mapbox_access_token,
            bearing=0,
            center=dict(
                lat=filtered_df['lat'].mean(),
                lon=filtered_df['lon'].mean()
            ),
            pitch=0,
            zoom=12
        )
    )

    return fig

if __name__ == "__main__":
    app.run_server(debug=True)
