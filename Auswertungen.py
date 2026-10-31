import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from PIL import Image
import plotly.express as px
import gdown




st.title("Vom Eis in die dritte Dimension")
st.header("Zusammenfassung der Resultate und Analysen")


image1=Image.open("Titel Bild final.webp")
st.image(image1, width=400)

url = "https://drive.google.com/file/d/1aOjvR1bF0PNR5lL5oG_PZaA6VmSV4rnt/view?usp=drive_link"

video=gdown.download(url, "A Axel normalspeed.mp4", quiet=False)
st.video(video, width=400)

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
    st.button("ℹ️",help="Der Axel ist der einzige der sechs Sprungtypen, bei dem der Absprung vorwärts erfolgt. Dadurch muss bei einem Axel eine halbe Drehung mehr ausgeführt werden als bei den anderen Sprüngen. Das macht ihn besonders anspruchsvoll. Er gehört ausserdem zu den Kantensprüngen.")

daten1=st.selectbox(label="1",options=einfacher_axel,label_visibility="collapsed")
if daten1=="Beispieldaten 1, Videomodus: Normalgeschwindigkeit":
    if st.checkbox("3D-Koordinatensystem"):
        dreidim_plotten("Video 4 Koordinaten.csv")
    #if st.checkbox("Sprungparameter"):

    #if st.checkbox("
    
#elif daten1=="Beispieldaten 2, Videomodus: Slowmotion":
    #dreidim_plotten("Video 5 Koordinaten.csv")
#elif daten1=="Beispieldaten 3, Videomodus: Slowmotion":
    #dreidim_plotten("Video 6 Koordinaten.csv")

col1, col2 = st.columns([10, 1])
with col1:
    st.subheader("Doppelter Salchow")
with col2:
    st.button("ℹ️",help="Beim Salchow erfolgt der Absprung rückwärts von der Innenkante des Schlittschuhs. Das freie Bein schwingt dabei nach vorne und unterstützt den Absprung. Der Salchow gehört zu den Kantensprüngen.")

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
    st.button("ℹ️",help="Der Toeloop wird rückwärts von der Aussenkante eines Schlittschuhs abgesprungen. Dabei wird die Zacke des anderen Schlittschuhs ins Eis gesetzt, um den Absprung zu unterstützen. Er gehört zu den Zackensprüngen.")


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
    st.button("ℹ️",help="Der Rittberger wird rückwärts von der Aussenkante eines Schlittschuhs abgesprungen. Anders als beim Toeloop wird dabei keine Zacke eingesetzt. Das freie Bein bleibt während des Absprungs vor dem Körper gekreuzt. Er gehört zu den Kantensprüngen.")



daten4=st.selectbox(label="4",options=doppelter_loop,label_visibility="collapsed")

#if daten4=="Beispieldaten 1, Videomodus: Normalgeschwindigkeit":
    #dreidim_plotten("Video 7 Koordinaten.csv")
#elif daten4=="Beispieldaten 2, Videomodus: Slowmotion":
    #dreidim_plotten("Video 8 Koordinaten.csv")


col1, col2 = st.columns([10, 1])
with col1:
    st.subheader("Doppelter Lutz")
with col2:
    st.button("ℹ️",help="Der Lutz wird rückwärts von der Aussenkante des Schlittschuhs abgesprungen. Zur Unterstützung des Absprungs wird die Zacke des anderen Schlittschuhs ins Eis gesetzt. Im Gegensatz zum Toeloop erfolgt der Absprung vom anderen Bein. Er gehört zu den Zackensprüngen.")
daten5=st.selectbox(label="5",options=doppelter_lutz,label_visibility="collapsed")

#if daten5=="Beispieldaten 1, Videomodus: Normalgeschwindigkeit":
    #dreidim_plotten("Video 7 Koordinaten.csv")
#elif daten5=="Beispieldaten 2, Videomodus: Slowmotion":
    #dreidim_plotten("Video 8 Koordinaten.csv")
#elif daten5=="Beispieldaten 3, Videomodus: Slowmotion":
    #dreidim_plotten("Video 9 Koordinaten.csv")

col1, col2 = st.columns([10, 1])
with col1:
    st.subheader("Doppelter Flip")
with col2:
    st.button("ℹ️",help="Der Flip wird rückwärts von der Innenkante des Schlittschuhs abgesprungen. Wie beim Lutz wird die Zacke des anderen Schlittschuhs zur Unterstützung des Absprungs ins Eis gesetzt. Der entscheidende Unterschied zwischen Flip und Lutz liegt somit in der verwendeten Absprungkante.")
    
st.write("Nicht in dieser Arbeit analysiert")



