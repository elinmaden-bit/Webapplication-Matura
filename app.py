import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from PIL import Image
import plotly.express as px
st.title("Vom Eis in die dritte Dimension")
st.header("Rekonstruktion und Auswertung von Sprungbewegungen anhand zweier Kameraperspektiven mittels Farbsegmentation")
image1=Image.open("Bild titel.png")
st.image(image1, width=400)

st.subheader("Video 4")
st.write("Sprungart: einfacher Axel, Videomodus: Normalgeschwindigkeit")
daten = pd.read_csv("Video 4 Koordinaten.csv", sep=";")
fig = go.Figure()


red = daten[daten["Farbe"] == "Red"]

fig.add_trace(go.Scatter3d(x=red["X"],y=red["Y"],z=red["Z"],mode="markers",name="Rote Punkte",marker=dict(size=3, color="red"),text=red["Frame"], hovertemplate="Frame: %{text}<br>X: %{x}<br>Y: %{y}<br>Z:%{z}<extra></extra>"))

green = daten[daten["Farbe"] == "Green"]

fig.add_trace(go.Scatter3d(x=green["X"],y=green["Y"],z=green["Z"],mode="markers",name="Grüne Punkte",marker=dict(size=3, color="green"),text=green["Frame"],hovertemplate="Frame: %{text}<br>X: %{x}<br>Y: %{y}<br>Z: %{z}<extra></extra>"))

fig.update_layout(title="Rekonstruierte 3D-Positionen",scene=dict(xaxis_title="X-Koordinate",yaxis_title="Y-Koordinate",zaxis_title="Z-Koordinate",aspectmode="data"),height=700)

# In Streamlit anzeigen
st.plotly_chart(fig, use_container_width=True)

st.subheader("Video 5")
st.write("Sprungart: einfacher Axel, Videomodus: Slowmotion")
st.subheader("Video 6")
st.write("Sprungart: einfacher Axel, Videomodus: Slowmotion")
st.subheader("Video 7")
st.write("Sprungart: doppelter Salchow, Videomodus: Normalgeschwindigkeit")
st.subheader("Video 8")
st.write("Sprungart: doppelter Salchow, Videomodus: Slowmotion")
st.subheader("Video 9")
st.write("Sprungart: doppelter Salchow, Videomodus: Slowmotion")
st.subheader("Video 10")
st.write("Sprungart: doppelter Toeloop, Videomodus: Normalgeschwindigkeit")
st.subheader("Video 11")
st.write("Sprungart: doppelter Toeloop, Videomodus: Slowmotion")
st.subheader("Video 12")
st.write("Sprungart: doppelter Toeloop, Videomodus: Slowmotion")
st.subheader("Video 13")
st.write("Sprungart: doppelter Rittberger, Videomodus: Normalgeschwindigkeit")
st.subheader("Video 14")
st.write("Sprungart: doppelter Rittberger, Videomodus: Slowmotion")
st.subheader("Video 15")
st.write("Sprungart: doppelter Lutz, Videomodus: Normalgeschwindigkeit")
st.subheader("Video 16")
st.write("Sprungart: doppelter Lutz, Videomodus: Slowmotion")
st.subheader("Video 17")
st.write("Sprungart: doppelter Lutz, Videomodus: slowmotion")
