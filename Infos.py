import streamlit as st


st.header("Über das Projekt")

st.subheader("Zweck & Ziel")
st.write("Das Ziel dieses Projekts ist es, einen Eiskunstlaufsprung mithilfe von zwei Videoaufnahmen aus unterschiedlichen Perspektiven dreidimensional zu analysieren.\nDazu wurde ein Python-Programm entwickelt, das ausgewählte farbige Markierungen in den Videos mithilfe von Bildverarbeitung erkennt und ihre Positionen über mehrere Einzelbilder hinweg verfolgt. Durch die Kombination der beiden Kameraperspektiven werden anschliessend die räumlichen Koordinaten der Markierungen rekonstruiert.\nAuf Grundlage dieser 3D-Daten können verschiedene Eigenschaften des Sprungs untersucht werden. Dazu gehören beispielsweise die Absprung- und Landeposition, die Sprunghöhe, die Flugzeit, die Sprungweite und die Rotation.\nDie Ergebnisse werden in dieser Webanwendung dargestellt, sodass die Bewegungsanalyse übersichtlich und nachvollziehbar betrachtet werden kann.\nDas übergeordnete Ziel ist es, herauszufinden, inwiefern sich die Bewegung eines Eiskunstlaufsprungs mithilfe von Videoaufnahmen und computergestützter Analyse quantitativ erfassen und auswerten lässt.")

st.subheader("Videosegmentierung")
st.write("Der Abschnitt der Videosegmentierung beginnt mit der Basis, dass zwei Videos vorhanden sind, die aus unterschiedlichen Winkeln denselben Sprung aufnehmen. Zur zeitlichen Synchronisierung der Sprünge wird zu Beginn ein blaues T-shirt gezeigt, wessen Farbe segmentiert wird und das aktuelle Frame dabei gespeichert wird.\nDer Absprung und das Landeframe muss bekannt sein, da das Programm diese leider nicht selbst erkennen kann. Für die Rot/Grün Segmentierung wird das Frame auf ein Frame kurz vor dem Absprung gesetzt und danach wird die Rote und Grüne Markierung erkannt. Durch das Bekanntgeben verschiedener Parameter der Aufnahmekameras wird die 3D-Position der Markierungen zum Zeitpunkt der einzelnen Frames ermittelt.")

st.subheader("Analyse & Berechnungen")
st.write("Im Bereich Analyse & Berechnungen werden die 3D-Daten danach analysiert und die Daten veranschaulicht. Ausserdem werden unteranderem Luftzeit, Sprunghöhe, Sprungweite und Rotation berechnet.")

st.subheader("Allgemeine Anwendung")
st.write("Hier kommen die Bedingungen für die allgemeine Anwendung hin")
