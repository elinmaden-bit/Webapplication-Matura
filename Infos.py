import streamlit as st



st.header("Über das Projekt")

st.image("Titelbild Über das Projekt.jpg", width=500)

st.subheader("Zweck & Ziel")
st.write("""
In diesem Projekt wird untersucht, wie sich ein Eiskunstlaufsprung mithilfe von Computer Vision und Videoaufnahmen dreidimensional analysieren lässt. Ziel ist es, die Bewegung während eines Sprungs nicht nur visuell zu betrachten, sondern verschiedene Eigenschaften auch quantitativ zu erfassen.

Dafür wurde ein Python-Programm entwickelt, das farbige Markierungen auf den Schlittschuhen in Videoaufnahmen erkennt und ihre Positionen über mehrere Einzelbilder hinweg bestimmt. Mithilfe von zwei Kameraperspektiven werden aus diesen Bildinformationen räumliche Koordinaten berechnet. Dadurch lässt sich die Bewegung der Markierungen im dreidimensionalen Raum nachvollziehen.
""")

st.subheader("Vorgehen & Funktionsweise")
st.write("""
Die Analyse basiert auf zwei Videoaufnahmen desselben Eiskunstlaufsprungs, die aus unterschiedlichen Perspektiven aufgenommen wurden. Mithilfe der Bildverarbeitungsbibliothek OpenCV werden die roten und grünen Markierungen in den einzelnen Videobildern erkannt. Anschliessend werden die ermittelten Bildkoordinaten unter Berücksichtigung der Kamerapositionen und der geometrischen Zusammenhänge in dreidimensionale Koordinaten umgerechnet.

Da die beiden Videoaufnahmen aus unterschiedlichen Blickwinkeln stammen, können die Informationen beider Kameras kombiniert werden. So lässt sich die räumliche Position der Markierungen für verschiedene Zeitpunkte des Sprungs rekonstruieren.
""")

st.subheader("Analyse & Berechnungen")
st.write("""
Auf Grundlage der rekonstruierten 3D-Daten werden verschiedene Eigenschaften des Sprungs untersucht. Dazu gehören insbesondere:

Flugzeit: die Zeitspanne zwischen Absprung und Landung.

Sprunghöhe: die maximale vertikale Bewegung der erkannten Markierungen über der Eisebene.

Sprungweite: die horizontale Distanz zwischen Absprung- und Landeposition.

Rotation: die während des Sprungs ausgeführte Drehbewegung.

Geschwindigkeit und Beschleunigung: die zeitliche Veränderung der Bewegung in der horizontalen Ebene.

Die berechneten Werte werden in der Webanwendung mithilfe von Diagrammen und weiteren Darstellungen veranschaulicht. Dadurch können die Bewegungsabläufe und die Ergebnisse der Analyse übersichtlich betrachtet werden.
""")

st.subheader("Umfang der Webanwendung")
st.write("""
Die Webanwendung dient dazu, das entwickelte Analyseverfahren und dessen Ergebnisse zu präsentieren. Sie basiert auf den bereits aufgenommenen und ausgewerteten Videos des Projekts. Eine eigene Videoupload- oder Videosegmentierungsfunktion ist nicht Bestandteil der Anwendung. Die dargestellten Berechnungen und Diagramme beziehen sich deshalb auf die im Rahmen der Maturaarbeit untersuchten Sprünge.

Das übergeordnete Ziel des Projekts ist es, die Möglichkeiten und Grenzen von Computer Vision bei der dreidimensionalen Bewegungsanalyse im Eiskunstlauf aufzuzeigen.
""")
