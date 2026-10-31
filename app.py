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

def dreidim_plotten(dateiname):

    daten = pd.read_csv(dateiname, sep=";")
    fig = go.Figure()
    
    red = daten[daten["Farbe"] == "Red"]
    fig.add_trace(go.Scatter3d(x=red["X"],y=red["Y"],z=red["Z"],mode="markers",name="Rote Punkte",marker=dict(size=3, color="red"),text=red["Frame"],hovertemplate="Frame: %{text}<br>X: %{x}<br>Y: %{y}<br>Z: %{z}<extra></extra>"))

    green = daten[daten["Farbe"] == "Green"]
    fig.add_trace(go.Scatter3d(x=green["X"],y=green["Y"],z=green["Z"],mode="markers",name="Grüne Punkte",marker=dict(size=3, color="green"),text=green["Frame"],hovertemplate="Frame: %{text}<br>X: %{x}<br>Y: %{y}<br>Z: %{z}<extra></extra>"))

    fig.update_layout(title="Rekonstruierte 3D-Positionen",scene=dict(xaxis_title="X-Koordinate",yaxis_title="Y-Koordinate",zaxis_title="Z-Koordinate",aspectmode="data"),height=700)

    st.plotly_chart(fig, use_container_width=True)


col1, col2 = st.columns([10, 1])
with col1:
    st.subheader("Einfacher Axel")
with col2:
    st.button("ℹ️",help="Der Axel ist einer der sechs Sprungtypen, die es im Eiskunstlauf gibt. Er ist der einzige Sprung, der vorwärts abgesprungen wird. Dadurch erhält er eine halbe Rotation mehr als die anderen Sprünge, was ihn auch zum schwersten Sprung macht.")

daten1=st.selectbox(label="1",options=einfacher_axel,label_visibility="collapsed")
if daten1=="Beispieldaten 1, Videomodus: Normalgeschwindigkeit":
    dreidim_plotten("Video 4 Koordinaten.csv")    
#elif daten1=="Beispieldaten 2, Videomodus: Slowmotion":
    #dreidim_plotten("Video 5 Koordinaten.csv")
#elif daten1=="Beispieldaten 3, Videomodus: Slowmotion":
    #dreidim_plotten("Video 6 Koordinaten.csv")

col1, col2 = st.columns([10, 1])
with col1:
    st.subheader("Doppelter Salchow")
with col2:
    st.button("ℹ️",help="Der Salchow kann mit dem Axel und dem Toeloop verglichen werden, da er ein ähnlichen Absprung hat. Beim Salchow beginnt der Sprung auf einer rückwärts-einwärts Kante und wird durch eine Drehung nach vorne abgesprungen.")

daten2=st.selectbox(label="2",options=doppelter_salchow,label_visibility="collapsed")

#if daten2=="Beispieldaten 1, Videomodus: Normalgeschwindigkeit":
    #dreidim_plotten("Video 7 Koordinaten.csv")
#elif daten2=="Beispieldaten 2, Videomodus: Slowmotion":
    #dreidim_plotten("Video 8 Koordinaten.csv")
#elif daten2=="Beispieldaten 3, Videomodus: Slowmotion":
    #dreidim_plotten("Video 9 Koordinaten.csv")

col1, col2 = st.columns([10, 1])
with col1:
    st.subheader("Doppelter Toeloop")
with col2:
    st.button("ℹ️",help="Der Toeloop wird rückwärts von einer Auswärtskante abgesprungen, wobei der Absprung durch das Einstecken der Zacke mit dem Spielbein erfolgt.")


daten3=st.selectbox(label="3",options=doppelter_toeloop,label_visibility="collapsed")

#if daten3=="Beispieldaten 1, Videomodus: Normalgeschwindigkeit":
    #dreidim_plotten("Video 7 Koordinaten.csv")
#elif daten3=="Beispieldaten 2, Videomodus: Slowmotion":
    #dreidim_plotten("Video 8 Koordinaten.csv")
#elif daten3=="Beispieldaten 3, Videomodus: Slowmotion":
    #dreidim_plotten("Video 9 Koordinaten.csv")

col1, col2 = st.columns([10, 1])
with col1:
    st.subheader("Doppelter Rittberger")
with col2:
    st.button("ℹ️",help="Der Rittberger hat einen individuellen Absprung, der mit keinen der anderen Sprüngen zu vergleichen ist. Er wird rückwärts von der Auswärtskante abgesprungen, wobei das Spielbein während des Absprungs vorne über dem anderen Bein gekreuzt bleibt.")



daten4=st.selectbox(label="4",options=doppelter_loop,label_visibility="collapsed")

#if daten4=="Beispieldaten 1, Videomodus: Normalgeschwindigkeit":
    #dreidim_plotten("Video 7 Koordinaten.csv")
#elif daten4=="Beispieldaten 2, Videomodus: Slowmotion":
    #dreidim_plotten("Video 8 Koordinaten.csv")

col1, col2 = st.columns([10, 1])
with col1:
    st.subheader("Doppelter Lutz")
with col2:
    st.button("ℹ️",help="Der Lutz wird von der rückwärts Auswärtskante abgesprungen. Dabei wird der Absprung durch das Einstecken der Zacke des Spielbeins ausgelöst. Der Unterschied zum Toeloop ist, dass das Spielbein beim Lutz das rechte Bein ist, und beim Toeloop ist es das Linke.")
daten5=st.selectbox(label="5",options=doppelter_lutz,label_visibility="collapsed")

#if daten5=="Beispieldaten 1, Videomodus: Normalgeschwindigkeit":
    #dreidim_plotten("Video 7 Koordinaten.csv")
#elif daten5=="Beispieldaten 2, Videomodus: Slowmotion":
    #dreidim_plotten("Video 8 Koordinaten.csv")
#elif daten5=="Beispieldaten 3, Videomodus: Slowmotion":
    #dreidim_plotten("Video 9 Koordinaten.csv")

