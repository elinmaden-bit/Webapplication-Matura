import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from PIL import Image
import plotly.express as px
import gdown
from scipy.interpolate import UnivariateSpline
import numpy as np
import ast



st.title("Vom Eis in die dritte Dimension")
st.header("Zusammenfassung der Resultate und Analysen")


image1=Image.open("Titel Bild final.webp")
st.image(image1, width=400)



einfacher_axel=["Beispieldaten 1, Videomodus: Normalgeschwindigkeit","Beispieldaten 2, Videomodus: Slowmotion","Beispieldaten 3, Videomodus: Slowmotion"]
doppelter_salchow=["Beispieldaten 1, Videomodus: Normalgeschwindigkeit","Beispieldaten 2, Videomodus: Slowmotion"]
doppelter_toeloop=["Beispieldaten 1, Videomodus: Normalgeschwindigkeit","Beispieldaten 2, Videomodus: Slowmotion","Beispieldaten 3, Videomodus: Slowmotion"]
doppelter_loop=["Beispieldaten 1, Videomodus: Normalgeschwindigkeit","Beispieldaten 2, Videomodus: Slowmotion"]
doppelter_lutz=["Beispieldaten 1, Videomodus: Normalgeschwindigkeit","Beispieldaten 2, Videomodus: Slowmotion","Beispieldaten 3, Videomodus: Slowmotion"]


fps=30
#für plotten und interpolation
fig = go.Figure()

def dreidim_plotten(dateiname):
    
    daten = pd.read_csv(dateiname, sep=";")
    red = daten[daten["Farbe"] == "Red"].copy()
    green = daten[daten["Farbe"] == "Green"].copy()

    fig.add_trace(go.Scatter3d(x=red["X"],y=red["Y"],z=red["Z"],mode="markers",name="Rote Punkte",marker=dict(size=3, color="red"),text=red["Frame"],hovertemplate="Frame: %{text}<br>X: %{x}<br>Y: %{y}<br>Z: %{z}<extra></extra>"))

    fig.add_trace(go.Scatter3d(x=green["X"],y=green["Y"],z=green["Z"],mode="markers",name="Grüne Punkte",marker=dict(size=3, color="green"),text=green["Frame"],hovertemplate="Frame: %{text}<br>X: %{x}<br>Y: %{y}<br>Z: %{z}<extra></extra>"))

    fig.update_layout(title="Rekonstruierte 3D-Positionen",scene=dict(xaxis_title="X-Koordinate",yaxis_title="Y-Koordinate",zaxis_title="Z-Koordinate",aspectmode="data"),height=700)

    return fig

def interpolation(dateiname, glattung=0.01):

    daten = pd.read_csv(dateiname, sep=";")
    red = daten[daten["Farbe"] == "Red"].copy()
    green = daten[daten["Farbe"] == "Green"].copy()

    red["Frame"] = pd.to_numeric(red["Frame"], errors="coerce")
    green["Frame"] = pd.to_numeric(green["Frame"], errors="coerce")
    
    t_red=red["Frame"].to_numpy()/fps

    x_red=red["X"].to_numpy()
    y_red = red["Y"].to_numpy()
    z_red = red["Z"].to_numpy()
    
    sortierung_red = np.argsort(t_red)
    t_red, x_red, y_red, z_red = t_red[sortierung_red], x_red[sortierung_red], y_red[sortierung_red], z_red[sortierung_red]
    
    spline_x_red = UnivariateSpline(t_red, x_red, s=glattung)
    spline_y_red = UnivariateSpline(t_red, y_red, s=glattung)
    spline_z_red = UnivariateSpline(t_red, z_red, s=glattung)

    t_neu_red = np.linspace(t_red[0], t_red[-1], 500)
    x_neu_red = spline_x_red(t_neu_red)
    y_neu_red = spline_y_red(t_neu_red)
    z_neu_red = spline_z_red(t_neu_red)

    vx_red = spline_x_red.derivative(1)(t_neu_red)
    vy_red = spline_y_red.derivative(1)(t_neu_red)
    geschwindigkeit_red = np.sqrt(vx_red**2 + vy_red**2)

    ax_red = spline_x_red.derivative(2)(t_neu_red)
    ay_red = spline_y_red.derivative(2)(t_neu_red)

    beschleunigung_red = np.sqrt(ax_red**2 + ay_red**2)

    t_green=green["Frame"].to_numpy()/fps

    x_green=green["X"].to_numpy()
    y_green = green["Y"].to_numpy()
    z_green = green["Z"].to_numpy()
    
    sortierung_green = np.argsort(t_green)
    t_green, x_green, y_green, z_green = t_green[sortierung_green], x_green[sortierung_green], y_green[sortierung_green], z_green[sortierung_green]
    
    spline_x_green = UnivariateSpline(t_green, x_green, s=glattung)
    spline_y_green = UnivariateSpline(t_green, y_green, s=glattung)
    spline_z_green = UnivariateSpline(t_green, z_green, s=glattung)

    t_neu_green = np.linspace(t_green[0], t_green[-1], 500)
    x_neu_green = spline_x_green(t_neu_green)
    y_neu_green = spline_y_green(t_neu_green)
    z_neu_green = spline_z_green(t_neu_green)

    vx_green = spline_x_green.derivative(1)(t_neu_green)
    vy_green = spline_y_green.derivative(1)(t_neu_green)
    geschwindigkeit_green = np.sqrt(vx_green**2 + vy_green**2)

    ax_green = spline_x_green.derivative(2)(t_neu_green)
    ay_green = spline_y_green.derivative(2)(t_neu_green)

    beschleunigung_green = np.sqrt(ax_green**2 + ay_green**2)

    fig.add_trace(go.Scatter3d(x=x_neu_red,y=y_neu_red,z=z_neu_red,mode="lines",name="Rote Gerade",line=dict(color="black", width=5)))

    fig.add_trace(go.Scatter3d(x=x_neu_green,y=y_neu_green,z=z_neu_green,mode="lines", name="Grüne Gerade", line=dict(color="black", width=5)))
    
    return fig, geschwindigkeit_green, beschleunigung_green, geschwindigkeit_red, beschleunigung_red

def sprungrichtung(dateiname):
    daten = pd.read_csv(dateiname, sep=";")
    absprung = np.array(ast.literal_eval(daten["Take-off Position"].iloc[0]))
    landung = np.array(ast.literal_eval(daten["Landungs Position"].iloc[0]))
    absprung_xy=absprung[:2]
    
    sprungrichtung=landung-absprung_xy

    laenge = np.linalg.norm(sprungrichtung)
    laenge=np.sqrt(sprungrichtung[0]**2+sprungrichtung[1]**2)

    fig.add_trace(go.Scatter3d(x=[absprung_xy[0],landung[0]],y=[absprung_xy[1], landung[1]],z=[absprung[2],absprung[2]],mode="lines+markers",line=dict(color="pink", width=15),marker=dict(size=[0,5],symbol="circle"),name="Sprungrichtung (von Absprung bis Landung)"))
    

col1, col2 = st.columns([10, 1])
with col1:
    st.subheader("Einfacher Axel")
with col2:
    st.button("ℹ️",help="Der Axel ist der einzige der sechs Sprungtypen, bei dem der Absprung vorwärts erfolgt. Dadurch muss bei einem Axel eine halbe Drehung mehr ausgeführt werden als bei den anderen Sprüngen. Das macht ihn besonders anspruchsvoll. Er gehört ausserdem zu den Kantensprüngen.")

daten1=st.selectbox(label="1",options=einfacher_axel,label_visibility="collapsed")
if daten1=="Beispieldaten 1, Videomodus: Normalgeschwindigkeit":
    if st.checkbox("3D-Koordinatensystem", key="checkboxvideo4"):
        dreidim_plotten("data/Video 4 Koordinaten.csv")
        print(daten[["X", "Y", "Z"]].shape)
        print(daten[["X", "Y", "Z"]].head())
        print(daten[["X", "Y", "Z"]].isna().sum())
        interpolation("data/Video 4 Koordinaten.csv")
        sprungrichtung("data/Video 4 Ergebnisse.csv")
        st.plotly_chart(fig, use_container_width=True)
    #if st.checkbox("Sprungparameter"):

    #if st.checkbox("
    
elif daten1=="Beispieldaten 2, Videomodus: Slowmotion":
    if st.checkbox("3D-Koordinatensystem", key="checkboxvideo5"):
        dreidim_plotten("Video 5 Koordinaten.csv")
        interpolation("data/Video 5 Koordinaten.csv")
        sprungrichtung("data/Video 5 Ergebnisse.csv")
        st.plotly_chart(fig, use_container_width=True)
elif daten1=="Beispieldaten 3, Videomodus: Slowmotion":
    if st.checkbox("3D-Koordinatensystem", key="checkboxvideo6"):
        dreidim_plotten("Video 6 Koordinaten.csv")
        interpolation("data/Video 6 Koordinaten.csv")
        sprungrichtung("data/Video 6 Ergebnisse.csv")
        st.plotly_chart(fig, use_container_width=True)

col1, col2 = st.columns([10, 1])
with col1:
    st.subheader("Doppelter Salchow")
with col2:
    st.button("ℹ️",help="Beim Salchow erfolgt der Absprung rückwärts von der Innenkante des Schlittschuhs. Das freie Bein schwingt dabei nach vorne und unterstützt den Absprung. Der Salchow gehört zu den Kantensprüngen.")

daten2=st.selectbox(label="2",options=doppelter_salchow,label_visibility="collapsed")

if daten2=="Beispieldaten 1, Videomodus: Normalgeschwindigkeit":
    if st.checkbox("3D-Koordinatensystem", key="checkboxvideo7"):
        dreidim_plotten("Video 7 Koordinaten.csv")
        interpolation("data/Video 7 Koordinaten.csv")
        sprungrichtung("data/Video 7 Ergebnisse.csv")
        st.plotly_chart(fig, use_container_width=True) 

elif daten2=="Beispieldaten 2, Videomodus: Slowmotion":
    if st.checkbox("3D-Koordinatensystem", key="checkboxvideo9"):
        dreidim_plotten("Video 9 Koordinaten.csv")
        interpolation("data/Video 9 Koordinaten.csv")
        sprungrichtung("data/Video 9 Ergebnisse.csv")
        st.plotly_chart(fig, use_container_width=True)


col1, col2 = st.columns([10, 1])
with col1:
    st.subheader("Doppelter Toeloop")
with col2:
    st.button("ℹ️",help="Der Toeloop wird rückwärts von der Aussenkante eines Schlittschuhs abgesprungen. Dabei wird die Zacke des anderen Schlittschuhs ins Eis gesetzt, um den Absprung zu unterstützen. Er gehört zu den Zackensprüngen.")


daten3=st.selectbox(label="3",options=doppelter_toeloop,label_visibility="collapsed")

if daten3=="Beispieldaten 1, Videomodus: Normalgeschwindigkeit":
    if st.checkbox("3D-Koordinatensystem", key="checkboxvideo10"):
        dreidim_plotten("Video 10 Koordinaten.csv")
        interpolation("data/Video 10 Koordinaten.csv")
        sprungrichtung("data/Video 10 Ergebnisse.csv")
        st.plotly_chart(fig, use_container_width=True)
        
elif daten3=="Beispieldaten 2, Videomodus: Slowmotion":
    if st.checkbox("3D-Koordinatensystem", key="checkboxvideo11"):
        dreidim_plotten("Video 11 Koordinaten.csv")
        interpolation("data/Video 11 Koordinaten.csv")
        sprungrichtung("data/Video 11 Ergebnisse.csv")
        st.plotly_chart(fig, use_container_width=True)
        
elif daten3=="Beispieldaten 3, Videomodus: Slowmotion":
    if st.checkbox("3D-Koordinatensystem", key="checkboxvideo12"):
        dreidim_plotten("Video 12 Koordinaten.csv")
        interpolation("data/Video 12 Koordinaten.csv")
        sprungrichtung("data/Video 12 Ergebnisse.csv")
        st.plotly_chart(fig, use_container_width=True)


col1, col2 = st.columns([10, 1])
with col1:
    st.subheader("Doppelter Rittberger")
with col2:
    st.button("ℹ️",help="Der Rittberger wird rückwärts von der Aussenkante eines Schlittschuhs abgesprungen. Anders als beim Toeloop wird dabei keine Zacke eingesetzt. Das freie Bein bleibt während des Absprungs vor dem Körper gekreuzt. Er gehört zu den Kantensprüngen.")



daten4=st.selectbox(label="4",options=doppelter_loop,label_visibility="collapsed")

if daten4=="Beispieldaten 1, Videomodus: Normalgeschwindigkeit":
    if st.checkbox("3D-Koordinatensystem", key="checkboxvideo13"):
        dreidim_plotten("Video 13 Koordinaten.csv")
        interpolation("data/Video 13 Koordinaten.csv")
        sprungrichtung("data/Video 13 Ergebnisse.csv")
        st.plotly_chart(fig, use_container_width=True)
elif daten4=="Beispieldaten 2, Videomodus: Slowmotion":
    if st.checkbox("3D-Koordinatensystem", key="checkboxvideo14"):
        dreidim_plotten("Video 14 Koordinaten.csv")
        interpolation("data/Video 14 Koordinaten.csv")
        sprungrichtung("data/Video 14 Ergebnisse.csv")
        st.plotly_chart(fig, use_container_width=True)


col1, col2 = st.columns([10, 1])
with col1:
    st.subheader("Doppelter Lutz")
with col2:
    st.button("ℹ️",help="Der Lutz wird rückwärts von der Aussenkante des Schlittschuhs abgesprungen. Zur Unterstützung des Absprungs wird die Zacke des anderen Schlittschuhs ins Eis gesetzt. Im Gegensatz zum Toeloop erfolgt der Absprung vom anderen Bein. Er gehört zu den Zackensprüngen.")
daten5=st.selectbox(label="5",options=doppelter_lutz,label_visibility="collapsed")

if daten5=="Beispieldaten 1, Videomodus: Normalgeschwindigkeit":
    if st.checkbox("3D-Koordinatensystem", key="checkboxvideo15"):
        dreidim_plotten("Video 15 Koordinaten.csv")
        interpolation("data/Video 15 Koordinaten.csv")
        sprungrichtung("data/Video 15 Ergebnisse.csv")
        st.plotly_chart(fig, use_container_width=True)
        
elif daten5=="Beispieldaten 2, Videomodus: Slowmotion":
    if st.checkbox("3D-Koordinatensystem", key="checkboxvideo16"):
        dreidim_plotten("Video 16 Koordinaten.csv")
        interpolation("data/Video 16 Koordinaten.csv")
        sprungrichtung("data/Video 16 Ergebnisse.csv")
        st.plotly_chart(fig, use_container_width=True)
        
elif daten5=="Beispieldaten 3, Videomodus: Slowmotion":
    if st.checkbox("3D-Koordinatensystem", key="checkboxvideo17"):
        dreidim_plotten("Video 17 Koordinaten.csv")
        interpolation("data/Video 17 Koordinaten.csv")
        sprungrichtung("data/Video 17 Ergebnisse.csv")
        st.plotly_chart(fig, use_container_width=True)

col1, col2 = st.columns([10, 1])
with col1:
    st.subheader("Doppelter Flip")
with col2:
    st.button("ℹ️",help="Der Flip wird rückwärts von der Innenkante des Schlittschuhs abgesprungen. Wie beim Lutz wird die Zacke des anderen Schlittschuhs zur Unterstützung des Absprungs ins Eis gesetzt. Der entscheidende Unterschied zwischen Flip und Lutz liegt somit in der verwendeten Absprungkante.")
    
st.write("Nicht in dieser Arbeit analysiert")



