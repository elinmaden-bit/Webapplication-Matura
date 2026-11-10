import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from PIL import Image
import plotly.express as px
import gdown
from scipy.interpolate import UnivariateSpline
import numpy as np
import ast
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"

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


def dreidim_plotten(dateiname,fig):
    
    daten = pd.read_csv(DATA_DIR/dateiname, sep=";")
	#Auf Ebene 0 bringen
    daten["Z"]=pd.to_numeric(daten["Z"], errors="coerce")
    tiefster_punkt= daten["Z"].min()
    daten["Z"]=daten["Z"]-tiefster_punkt
	
    red = daten[daten["Farbe"] == "Red"].copy()
    green = daten[daten["Farbe"] == "Green"].copy()

    fig.add_trace(go.Scatter3d(x=red["X"],y=red["Y"],z=red["Z"],mode="markers",name="Rote Punkte",marker=dict(size=3, color="red"),text=red["Frame"],hovertemplate="Frame: %{text}<br>X: %{x}<br>Y: %{y}<br>Z: %{z}<extra></extra>"))

    fig.add_trace(go.Scatter3d(x=green["X"],y=green["Y"],z=green["Z"],mode="markers",name="Grüne Punkte",marker=dict(size=3, color="green"),text=green["Frame"],hovertemplate="Frame: %{text}<br>X: %{x}<br>Y: %{y}<br>Z: %{z}<extra></extra>"))

    fig.update_layout(title="Rekonstruierte 3D-Positionen",scene=dict(xaxis_title="X-Koordinate",yaxis_title="Y-Koordinate",zaxis_title="Z-Koordinate",aspectmode="data"),height=700)

    return fig

def interpolation(dateiname, fig, glattung=0.01):

    daten = pd.read_csv(DATA_DIR/dateiname, sep=";")
    #Daten auf höhe 0 bringen
    daten["Z"]=pd.to_numeric(daten["Z"], errors="coerce")
    tiefster_punkt= daten["Z"].min()
    daten["Z"]=daten["Z"]-tiefster_punkt

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
    
    return (fig, t_neu_green, geschwindigkeit_green, beschleunigung_green, t_neu_red, geschwindigkeit_red, beschleunigung_red)

def sprungrichtung(dateiname, fig):
    daten = pd.read_csv(DATA_DIR/dateiname, sep=";")
    absprung = np.array(ast.literal_eval(daten["Take-off Position"].iloc[0]))
    landung = np.array(ast.literal_eval(daten["Landungs Position"].iloc[0]))
    absprung_xy=absprung[:2]
    landung_xy = landung[:2]
    
    sprungrichtung=landung-absprung_xy

    laenge = np.linalg.norm(sprungrichtung)
    laenge=np.sqrt(sprungrichtung[0]**2+sprungrichtung[1]**2)

    fig.add_trace(go.Scatter3d(x=[absprung_xy[0],landung_xy[0]],y=[absprung_xy[1], landung_xy[1]],z=[0,0],mode="lines+markers",line=dict(color="pink", width=15),marker=dict(size=[0,5],symbol="circle"),name="Sprungrichtung (von Absprung bis Landung)"))
    return fig

def analyse(dateiname1, dateiname2):
    fig = go.Figure()

    fig = dreidim_plotten(dateiname1, fig)
    (fig, t_neu_green, geschwindigkeit_green, beschleunigung_green, t_neu_red, geschwindigkeit_red, beschleunigung_red) = interpolation(dateiname1, fig)
    fig = sprungrichtung(dateiname2, fig)

    st.plotly_chart(fig, use_container_width=True)

		
    return (t_neu_green, geschwindigkeit_green, beschleunigung_green, t_neu_red, geschwindigkeit_red, beschleunigung_red)
    
def tabelle(dateiname):
    daten=pd.read_csv(DATA_DIR/dateiname, sep=";")
    st.subheader("Berechnete Werte des Sprungs")
    st.table(daten)

def graphik_höhe(dateiname1, dateiname2):
    fig_hoehe=go.Figure()
    daten=pd.read_csv(DATA_DIR/dateiname1, sep=";")
	
    daten2=pd.read_csv(DATA_DIR/dateiname2, sep=";")
    take_off_frame=pd.to_numeric(daten2["Take-off Frame"], errors="coerce").iloc[0]

    daten["Z"]=pd.to_numeric(daten["Z"], errors="coerce")
    tiefster_punkt= daten["Z"].min()
    daten["Z"]=daten["Z"]-tiefster_punkt
    hoehen_daten= daten[["Farbe", "Frame", "Z"]].copy()
    red = hoehen_daten[hoehen_daten["Farbe"] == "Red"]
    green = hoehen_daten[hoehen_daten["Farbe"] == "Green"]
    red["Frame"] = pd.to_numeric(red["Frame"],errors="coerce")
    green["Frame"] = pd.to_numeric(green["Frame"],errors="coerce")	
    fig_hoehe.add_trace(go.Scatter(x=(red["Frame"]-take_off_frame)/30,y=red["Z"],mode="lines+markers",name="Roter Punkt",line=dict(color="red")))

    fig_hoehe.add_trace(go.Scatter(x=(green["Frame"]-take_off_frame)/30,y=green["Z"],mode="lines+markers",name="Grüner Punkt",line=dict(color="green")))

    fig_hoehe.update_layout(title="Höhenverlauf während des Sprungs",xaxis_title="Zeit[s]",yaxis_title="Höhe [m]",legend_title="Punktfarbe")

    st.plotly_chart(fig_hoehe, use_container_width=True)

def geschleunigung_xy(dateiname1):
    fig1=go.Figure()
    (fig, t_neu_green, geschwindigkeit_green, beschleunigung_green,t_neu_red, geschwindigkeit_red, beschleunigung_red) = interpolation(dateiname1, fig1)
    fig_v=go.Figure()
    fig_a=go.Figure()

    fig_v.add_trace(go.Scatter(x=t_neu_red,y=geschwindigkeit_red,mode="lines",name="Roter Punkt",line=dict(color="red")))
    fig_v.add_trace(go.Scatter(x=t_neu_green,y=geschwindigkeit_green,mode="lines",name="Grüner Punkt",line=dict(color="green")))
    fig_v.update_layout(title="Geschwindigkeitsverlauf während des Sprungs in xy-Richtung",xaxis_title="Zeit[s]",yaxis_title="v [m/s]",legend_title="Punktfarbe")

    fig_a.add_trace(go.Scatter(x=t_neu_red,y=beschleunigung_red,mode="lines",name="Roter Punkt",line=dict(color="red")))
    fig_a.add_trace(go.Scatter(x=t_neu_green,y=beschleunigung_green,mode="lines",name="Grüner Punkt",line=dict(color="green")))
    fig_a.update_layout(title="Beschleunigungsverlauf während des Sprungs",xaxis_title="Zeit[s]",yaxis_title="a [m/s^2]",legend_title="Punktfarbe")

    st.plotly_chart(fig_v, use_container_width=True)
    st.plotly_chart(fig_a, use_container_width=True)


def rotation(dateiname1, dateiname2):
    daten=pd.read_csv(DATA_DIR/dateiname1, sep=";")
    daten2=pd.read_csv(DATA_DIR/dateiname2, sep=";")
    fig_xy=go.Figure()

    take_off_frame=pd.to_numeric(daten2["Take-off Frame"], errors="coerce").iloc[0]
    landing_frame=pd.to_numeric(daten2["Landungs Frame"], errors="coerce").iloc[0]
	
    take_off_position=ast.literal_eval(daten2["Take-off Position"].iloc[0])
    landing_position=ast.literal_eval(daten2["Landungs Position"].iloc[0])
    take_off_position_x=take_off_position[0]
    landing_position_x=landing_position[0]
    take_off_position_y=take_off_position[1]
    landing_position_y=landing_position[1]
	
    xy_daten=daten[["Farbe", "Frame", "X", "Y"]].copy()
    xy_daten["Frame"] = pd.to_numeric(xy_daten["Frame"], errors="coerce")
    red_original=xy_daten[xy_daten["Farbe"]=="Red"]
    green_original=xy_daten[xy_daten["Farbe"]=="Green"]
	
    red_daten=xy_daten[(xy_daten["Farbe"]=="Red")&(xy_daten["Frame"]>take_off_frame)&(xy_daten["Frame"]<landing_frame)].copy()
    green_daten=xy_daten[(xy_daten["Farbe"]=="Green")&(xy_daten["Frame"]>take_off_frame)&(xy_daten["Frame"]<landing_frame)].copy()

    verwendete_red = set()
    verwendete_green = set()
    verbindungen = []

    for frame, gruppe in xy_daten.groupby("Frame"):

        red = gruppe[gruppe["Farbe"] == "Red"]
        green = gruppe[gruppe["Farbe"] == "Green"]
	
        if not red.empty and not green.empty:
            verbindungen.append((red.iloc[0], green.iloc[0]))
			
            verwendete_red.add(red.index[0])
            verwendete_green.add(green.index[0])

    if len(verbindungen) < 3:
        st.write("Framepaare auf Differenz 5 erweitert")
        red_daten = xy_daten[(xy_daten["Farbe"] == "Red")&(xy_daten["Frame"]>take_off_frame)&(xy_daten["Frame"]<landing_frame)&(~xy_daten.index.isin(verwendete_red))]
        green_daten = xy_daten[(xy_daten["Farbe"] == "Green")&(xy_daten["Frame"]>take_off_frame)&(xy_daten["Frame"]<landing_frame)&(~xy_daten.index.isin(verwendete_green))]

        for red_index, red in red_daten.iterrows():

            if len(verbindungen) >= 3:
                break

            kandidaten = green_daten[abs(green_daten["Frame"] - red["Frame"]) <= 5].copy()

            if not kandidaten.empty:

                kandidaten["Differenz"] = abs(kandidaten["Frame"] - red["Frame"])

                green = kandidaten.sort_values("Differenz").iloc[0]

                verbindungen.append((red, green))

                verwendete_red.add(red_index)
                verwendete_green.add(green.name)

                green_daten = green_daten.drop(green.name)

    for red, green in verbindungen:
        fig_xy.add_trace(go.Scatter(x=[red["X"], green["X"]],y=[red["Y"], green["Y"]],mode="lines",name="Verbindung Rot-Grün bei gleicher Zeit",line=dict(color="grey", width=1),showlegend=False,hoverinfo="skip"))

    fig_xy.add_trace(go.Scatter(x=red_original["X"],y=red_original["Y"],mode="lines+markers",name="Roter Punkt",line=dict(color="red")))
    fig_xy.add_trace(go.Scatter(x=green_original["X"],y=green_original["Y"],mode="lines+markers",name="Grüner Punkt",line=dict(color="green")))
    fig_xy.add_trace(go.Scatter(x=[take_off_position_x,landing_position_x],y=[take_off_position_y,landing_position_y], mode="lines", name="Sprungrichtung von Absprung bis Landung", line=dict(color="violet")))
    fig_xy.update_layout(title="XY-Positionsverlauf während des Sprungs",xaxis_title="X-Position[m]",yaxis_title="Y-Position [m]",legend_title="Punktfarbe")
    st.plotly_chart(fig_xy, use_container_width=True)

col1, col2 = st.columns([5, 1])
with col1:
    st.subheader("Einfacher Axel")
with col2:
    st.button("ℹ️",help="Der Axel ist der einzige der sechs Sprungtypen, bei dem der Absprung vorwärts erfolgt. Dadurch muss bei einem Axel eine halbe Drehung mehr ausgeführt werden als bei den anderen Sprüngen. Das macht ihn besonders anspruchsvoll. Er gehört ausserdem zu den Kantensprüngen.")

daten1=st.selectbox(label="1",options=einfacher_axel,label_visibility="collapsed")
if daten1=="Beispieldaten 1, Videomodus: Normalgeschwindigkeit":
    if st.checkbox("3D-Koordinatensystem", key="checkboxvideo4"):
        analyse("Video 4 Koordinaten.csv","Video 4 Ergebnisse.csv")
    if st.checkbox("Sprungparameter", key="checkbox4"):
        tabelle("Video 4 Ergebnisse.csv")
    if st.checkbox("Funktion Höhe-Zeit", key="2checkbox4"):
        graphik_höhe("Video 4 Koordinaten.csv","Video 4 Ergebnisse.csv")
    if st.checkbox("Funktion Geschwindigkeit und Beschleunigung (xy-Richtung)", key="3checkbox4"):
        geschleunigung_xy("Video 4 Koordinaten.csv")
    if st.checkbox("Funktion X Position-Y Position", key="4checkbox4"):
        rotation("Video 4 Koordinaten.csv","Video 4 Ergebnisse.csv")
    
elif daten1=="Beispieldaten 2, Videomodus: Slowmotion":
    if st.checkbox("3D-Koordinatensystem", key="checkboxvideo5"):
        analyse("Video 5 Koordinaten.csv","Video 5 Ergebnisse.csv")
    if st.checkbox("Sprungparameter", key="checkbox5"):
        tabelle("Video 5 Ergebnisse.csv")
    if st.checkbox("Funktion Höhe-Zeit", key="2checkbox5"):
        graphik_höhe("Video 5 Koordinaten.csv","Video 5 Ergebnisse.csv")
    if st.checkbox("Funktion Geschwindigkeit und Beschleunigung (xy-Richtung)", key="3checkbox5"):
        geschleunigung_xy("Video 5 Koordinaten.csv")
    if st.checkbox("Funktion X Position-Y Position", key="4checkbox5"):
        rotation("Video 5 Koordinaten.csv","Video 5 Ergebnisse.csv")
        
elif daten1=="Beispieldaten 3, Videomodus: Slowmotion":
    if st.checkbox("3D-Koordinatensystem", key="checkboxvideo6"):
        analyse("Video 6 Koordinaten.csv","Video 6 Ergebnisse.csv")
    if st.checkbox("Sprungparameter", key="checkbox6"):
        tabelle("Video 6 Ergebnisse.csv")
    if st.checkbox("Funktion Höhe-Zeit", key="2checkbox6"):
        graphik_höhe("Video 6 Koordinaten.csv","Video 6 Ergebnisse.csv")
    if st.checkbox("Funktion Geschwindigkeit und Beschleunigung (xy-Richtung)", key="3checkbox6"):
        geschleunigung_xy("Video 6 Koordinaten.csv")
    if st.checkbox("Funktion X Position-Y Position", key="4checkbox6"):
        rotation("Video 6 Koordinaten.csv","Video 6 Ergebnisse.csv")

col1, col2 = st.columns([10, 1])
with col1:
    st.subheader("Doppelter Salchow")
with col2:
    st.button("ℹ️",help="Beim Salchow erfolgt der Absprung rückwärts von der Innenkante des Schlittschuhs. Das freie Bein schwingt dabei nach vorne und unterstützt den Absprung. Der Salchow gehört zu den Kantensprüngen.")

daten2=st.selectbox(label="2",options=doppelter_salchow,label_visibility="collapsed")

if daten2=="Beispieldaten 1, Videomodus: Normalgeschwindigkeit":
    if st.checkbox("3D-Koordinatensystem", key="checkboxvideo7"):
        analyse("Video 7 Koordinaten.csv","Video 7 Ergebnisse.csv")
    if st.checkbox("Sprungparameter", key="checkbox7"):
        tabelle("Video 7 Ergebnisse.csv")
    if st.checkbox("Funktion Höhe-Zeit", key="2checkbox7"):
        graphik_höhe("Video 7 Koordinaten.csv","Video 7 Ergebnisse.csv")
    if st.checkbox("Funktion Geschwindigkeit und Beschleunigung (xy-Richtung)", key="3checkbox7"):
        geschleunigung_xy("Video 7 Koordinaten.csv")
    if st.checkbox("Funktion X Position-Y Position", key="4checkbox7"):
        rotation("Video 7 Koordinaten.csv","Video 7 Ergebnisse.csv")

elif daten2=="Beispieldaten 2, Videomodus: Slowmotion":
    if st.checkbox("3D-Koordinatensystem", key="checkboxvideo9"):
        analyse("Video 9 Koordinaten.csv","Video 9 Ergebnisse.csv")
    if st.checkbox("Sprungparameter", key="checkbox9"):
        tabelle("Video 9 Ergebnisse.csv")
    if st.checkbox("Funktion Höhe-Zeit", key="2checkbox9"):
        graphik_höhe("Video 9 Koordinaten.csv","Video 9 Ergebnisse.csv")
    if st.checkbox("Funktion Geschwindigkeit und Beschleunigung (xy-Richtung)", key="3checkbox9"):
        geschleunigung_xy("Video 9 Koordinaten.csv")
    if st.checkbox("Funktion X Position-Y Position", key="4checkbox9"):
        rotation("Video 9 Koordinaten.csv","Video 9 Ergebnisse.csv")


col1, col2 = st.columns([10, 1])
with col1:
    st.subheader("Doppelter Toeloop")
with col2:
    st.button("ℹ️",help="Der Toeloop wird rückwärts von der Aussenkante eines Schlittschuhs abgesprungen. Dabei wird die Zacke des anderen Schlittschuhs ins Eis gesetzt, um den Absprung zu unterstützen. Er gehört zu den Zackensprüngen.")


daten3=st.selectbox(label="3",options=doppelter_toeloop,label_visibility="collapsed")

if daten3=="Beispieldaten 1, Videomodus: Normalgeschwindigkeit":
    if st.checkbox("3D-Koordinatensystem", key="checkboxvideo10"):
        analyse("Video 10 Koordinaten.csv","Video 10 Ergebnisse.csv")
    if st.checkbox("Sprungparameter", key="checkbox10"):
        tabelle("Video 10 Ergebnisse.csv")
    if st.checkbox("Funktion Höhe-Zeit", key="2checkbox10"):
        graphik_höhe("Video 10 Koordinaten.csv","Video 10 Ergebnisse.csv")
    if st.checkbox("Funktion Geschwindigkeit und Beschleunigung (xy-Richtung)", key="3checkbox10"):
        geschleunigung_xy("Video 10 Koordinaten.csv")
    if st.checkbox("Funktion X Position-Y Position", key="4checkbox10"):
        rotation("Video 10 Koordinaten.csv","Video 10 Ergebnisse.csv")
        
elif daten3=="Beispieldaten 2, Videomodus: Slowmotion":
    if st.checkbox("3D-Koordinatensystem", key="checkboxvideo11"):
        analyse("Video 11 Koordinaten.csv","Video 11 Ergebnisse.csv")
    if st.checkbox("Sprungparameter", key="checkbox11"):
        tabelle("Video 11 Ergebnisse.csv")
    if st.checkbox("Funktion Höhe-Zeit", key="2checkbox11"):
        graphik_höhe("Video 11 Koordinaten.csv","Video 11 Ergebnisse.csv")
    if st.checkbox("Funktion Geschwindigkeit und Beschleunigung (xy-Richtung)", key="3checkbox11"):
        geschleunigung_xy("Video 11 Koordinaten.csv")
    if st.checkbox("Funktion X Position-Y Position", key="4checkbox11"):
        rotation("Video 11 Koordinaten.csv","Video 11 Ergebnisse.csv")
        
elif daten3=="Beispieldaten 3, Videomodus: Slowmotion":
    if st.checkbox("3D-Koordinatensystem", key="checkboxvideo12"):
        analyse("Video 12 Koordinaten.csv","Video 12 Ergebnisse.csv")
    if st.checkbox("Sprungparameter", key="checkbox12"):
        tabelle("Video 12 Ergebnisse.csv")
    if st.checkbox("Funktion Höhe-Zeit", key="2checkbox12"):
        graphik_höhe("Video 12 Koordinaten.csv","Video 12 Ergebnisse.csv")
    if st.checkbox("Funktion Geschwindigkeit und Beschleunigung (xy-Richtung)", key="3checkbox12"):
        geschleunigung_xy("Video 12 Koordinaten.csv")
    if st.checkbox("Funktion X Position-Y Position", key="4checkbox12"):
        rotation("Video 12 Koordinaten.csv","Video 12 Ergebnisse.csv")

col1, col2 = st.columns([10, 1])
with col1:
    st.subheader("Doppelter Rittberger")
with col2:
    st.button("ℹ️",help="Der Rittberger wird rückwärts von der Aussenkante eines Schlittschuhs abgesprungen. Anders als beim Toeloop wird dabei keine Zacke eingesetzt. Das freie Bein bleibt während des Absprungs vor dem Körper gekreuzt. Er gehört zu den Kantensprüngen.")



daten4=st.selectbox(label="4",options=doppelter_loop,label_visibility="collapsed")

if daten4=="Beispieldaten 1, Videomodus: Normalgeschwindigkeit":
    if st.checkbox("3D-Koordinatensystem", key="checkboxvideo13"):
        analyse("Video 13 Koordinaten.csv","Video 13 Ergebnisse.csv")
    if st.checkbox("Sprungparameter", key="checkbox13"):
        tabelle("Video 13 Ergebnisse.csv")
    if st.checkbox("Funktion Höhe-Zeit", key="2checkbox13"):
        graphik_höhe("Video 13 Koordinaten.csv","Video 13 Ergebnisse.csv")
    if st.checkbox("Funktion Geschwindigkeit und Beschleunigung (xy-Richtung)", key="3checkbox13"):
        geschleunigung_xy("Video 13 Koordinaten.csv")
    if st.checkbox("Funktion X Position-Y Position", key="4checkbox13"):
        rotation("Video 13 Koordinaten.csv","Video 13 Ergebnisse.csv")


elif daten4=="Beispieldaten 2, Videomodus: Slowmotion":
    if st.checkbox("3D-Koordinatensystem", key="checkboxvideo14"):
        analyse("Video 14 Koordinaten.csv","Video 14 Ergebnisse.csv")
    if st.checkbox("Sprungparameter", key="checkbox14"):
        tabelle("Video 14 Ergebnisse.csv")
    if st.checkbox("Funktion Höhe-Zeit", key="2checkbox14"):
        graphik_höhe("Video 14 Koordinaten.csv","Video 14 Ergebnisse.csv")
    if st.checkbox("Funktion Geschwindigkeit und Beschleunigung (xy-Richtung)", key="3checkbox14"):
        geschleunigung_xy("Video 14 Koordinaten.csv")
    if st.checkbox("Funktion X Position-Y Position", key="4checkbox14"):
        rotation("Video 14 Koordinaten.csv","Video 14 Ergebnisse.csv")


col1, col2 = st.columns([10, 1])
with col1:
    st.subheader("Doppelter Lutz")
with col2:
    st.button("ℹ️",help="Der Lutz wird rückwärts von der Aussenkante des Schlittschuhs abgesprungen. Zur Unterstützung des Absprungs wird die Zacke des anderen Schlittschuhs ins Eis gesetzt. Im Gegensatz zum Toeloop erfolgt der Absprung vom anderen Bein. Er gehört zu den Zackensprüngen.")
daten5=st.selectbox(label="5",options=doppelter_lutz,label_visibility="collapsed")

if daten5=="Beispieldaten 1, Videomodus: Normalgeschwindigkeit":
    if st.checkbox("3D-Koordinatensystem", key="checkboxvideo15"):
        analyse("Video 15 Koordinaten.csv","Video 15 Ergebnisse.csv")
    if st.checkbox("Sprungparameter", key="checkbox15"):
        tabelle("Video 15 Ergebnisse.csv")
    if st.checkbox("Funktion Höhe-Zeit", key="2checkbox15"):
        graphik_höhe("Video 15 Koordinaten.csv","Video 15 Ergebnisse.csv")
    if st.checkbox("Funktion Geschwindigkeit und Beschleunigung (xy-Richtung)", key="3checkbox15"):
        geschleunigung_xy("Video 15 Koordinaten.csv")
    if st.checkbox("Funktion X Position-Y Position", key="4checkbox15"):
        rotation("Video 15 Koordinaten.csv","Video 15 Ergebnisse.csv")
        
elif daten5=="Beispieldaten 2, Videomodus: Slowmotion":
    if st.checkbox("3D-Koordinatensystem", key="checkboxvideo16"):
        analyse("Video 16 Koordinaten.csv","Video 16 Ergebnisse.csv")
    if st.checkbox("Sprungparameter", key="checkbox16"):
        tabelle("Video 16 Ergebnisse.csv")
    if st.checkbox("Funktion Höhe-Zeit", key="2checkbox16"):
        graphik_höhe("Video 16 Koordinaten.csv","Video 16 Ergebnisse.csv")
    if st.checkbox("Funktion Geschwindigkeit und Beschleunigung (xy-Richtung)", key="3checkbox16"):
        geschleunigung_xy("Video 16 Koordinaten.csv")
    if st.checkbox("Funktion X Position-Y Position", key="4checkbox16"):
        rotation("Video 16 Koordinaten.csv","Video 16 Ergebnisse.csv")
        
elif daten5=="Beispieldaten 3, Videomodus: Slowmotion":
    if st.checkbox("3D-Koordinatensystem", key="checkboxvideo17"):
        analyse("Video 17 Koordinaten.csv","Video 17 Ergebnisse.csv")
    if st.checkbox("Sprungparameter", key="checkbox17"):
        tabelle("Video 17 Ergebnisse.csv")
    if st.checkbox("Funktion Höhe-Zeit", key="2checkbox17"):
        graphik_höhe("Video 17 Koordinaten.csv","Video 17 Ergebnisse.csv")
    if st.checkbox("Funktion Geschwindigkeit und Beschleunigung (xy-Richtung)", key="3checkbox17"):
        geschleunigung_xy("Video 17 Koordinaten.csv")
    if st.checkbox("Funktion X Position-Y Position", key="4checkbox17"):
        rotation("Video 17 Koordinaten.csv","Video 17 Ergebnisse.csv")

col1, col2 = st.columns([10, 1])
with col1:
    st.subheader("Doppelter Flip")
with col2:
    st.button("ℹ️",help="Der Flip wird rückwärts von der Innenkante des Schlittschuhs abgesprungen. Wie beim Lutz wird die Zacke des anderen Schlittschuhs zur Unterstützung des Absprungs ins Eis gesetzt. Der entscheidende Unterschied zwischen Flip und Lutz liegt somit in der verwendeten Absprungkante.")
    
st.write("Nicht in dieser Arbeit analysiert")



