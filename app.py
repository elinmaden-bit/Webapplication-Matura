import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from PIL import Image
import plotly.express as px
st.title("Vom Eis in die dritte Dimension")
st.header("Rekonstruktion und Auswertung von Sprungbewegungen anhand zweier Kameraperspektiven mittels Farbsegmentation")
image1=Image.open("Titel Bild final.webp")
st.image(image1, width=400)
einfacher_axel=["Beispieldaten 1, Videomodus: Normalgeschwindigkeit","Beispieldaten 2, Videomodus: Slowmotion","Beispieldaten 3, Videomodus: Slowmotion"]
doppelter_salchow=["Beispieldaten 1, Videomodus: Normalgeschwindigkeit","Beispieldaten 2, Videomodus: Slowmotion","Beispieldaten 3, Videomodus: Slowmotion"]
doppelter_toeloop=["Beispieldaten 1, Videomodus: Normalgeschwindigkeit","Beispieldaten 2, Videomodus: Slowmotion","Beispieldaten 3, Videomodus: Slowmotion"]
doppelter_loop=["Beispieldaten 1, Videomodus: Normalgeschwindigkeit","Beispieldaten 2, Videomodus: Slowmotion"]
doppelter_lutz=["Beispieldaten 1, Videomodus: Normalgeschwindigkeit","Beispieldaten 2, Videomodus: Slowmotion","Beispieldaten 3, Videomodus: Slowmotion"]
st.subheader("Einfacher Axel")
st.selectbox(" ",einfacher_axel)
daten = pd.read_csv("Video 4 Koordinaten.csv", sep=";")
fig = go.Figure()


red = daten[daten["Farbe"] == "Red"]

fig.add_trace(go.Scatter3d(x=red["X"],y=red["Y"],z=red["Z"],mode="markers",name="Rote Punkte",marker=dict(size=3, color="red"),text=red["Frame"], hovertemplate="Frame: %{text}<br>X: %{x}<br>Y: %{y}<br>Z:%{z}<extra></extra>"))

green = daten[daten["Farbe"] == "Green"]

fig.add_trace(go.Scatter3d(x=green["X"],y=green["Y"],z=green["Z"],mode="markers",name="Grüne Punkte",marker=dict(size=3, color="green"),text=green["Frame"],hovertemplate="Frame: %{text}<br>X: %{x}<br>Y: %{y}<br>Z: %{z}<extra></extra>"))

fig.update_layout(title="Rekonstruierte 3D-Positionen",scene=dict(xaxis_title="X-Koordinate",yaxis_title="Y-Koordinate",zaxis_title="Z-Koordinate",aspectmode="data"),height=700)

# In Streamlit anzeigen
st.plotly_chart(fig, use_container_width=True)


st.subheader("Doppelter Salchow")
st.selectbox("Daten auswählen",doppelter_salchow)
st.subheader("Doppelter Toeloop")
st.selectbox("Daten auswählen",doppelter_toeloop)

st.subheader("Doppelter Rittberger")
st.selectbox("Daten auswählen",doppelter_loop)

st.subheader("Doppelter Lutz")
st.selectbox("Daten auswählen",doppelter_lutz)

