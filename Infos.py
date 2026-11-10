import streamlit as st


st.header("Über das Projekt")

st.subheader("Zweck & Ziel")
st.write(st.write("""
Das Ziel dieses Projekts ist es, einen Eiskunstlaufsprung mithilfe von zwei Videoaufnahmen aus unterschiedlichen Perspektiven dreidimensional zu analysieren.

Dazu wurde ein Python-Programm entwickelt, das farbige Markierungen an den Schlittschuhen mithilfe von Bildverarbeitung erkennt und ihre Positionen in den einzelnen Videoframes verfolgt. Durch die Kombination der Aufnahmen beider Kameras können anschliessend die räumlichen Koordinaten der Markierungen rekonstruiert werden.

Auf Grundlage dieser 3D-Daten lassen sich verschiedene Bewegungsparameter untersuchen. Dazu gehören beispielsweise die Absprung- und Landeposition, die Sprunghöhe, die Flugzeit, die horizontale Sprungweite und die Rotation.

Die Webapplikation ermöglicht es, diese Daten auszuwerten und die Bewegung des Sprungs anhand verschiedener Diagramme und berechneter Werte zu veranschaulichen.
"""))

st.subheader("Videosegmentierung")
st.write("""
Für die Analyse werden zwei Videoaufnahmen benötigt, die denselben Sprung aus unterschiedlichen Perspektiven zeigen. Die Videos werden zunächst zeitlich aufeinander abgestimmt. Dazu wird ein blaues T-Shirt zu Beginn der Aufnahme verwendet, dessen Farbe automatisch erkannt wird.

Anschliessend werden die roten und grünen Markierungen an den Schlittschuhen in den einzelnen Frames segmentiert. Der Zeitpunkt des Absprungs und der Landung muss dabei manuell angegeben werden, da das Programm diese Ereignisse nicht zuverlässig selbst erkennen kann.

Mithilfe der Kameraparameter und der erkannten Bildkoordinaten werden die dreidimensionalen Positionen der Markierungen berechnet. Diese bilden die Grundlage für die anschliessende Bewegungsanalyse.
""")

st.subheader("Analyse & Berechnungen")
st.write("""
Die rekonstruierten 3D-Daten werden anschliessend ausgewertet und grafisch dargestellt. Dabei können unter anderem die Flugzeit, die Sprunghöhe, die horizontale Sprungweite und die Rotation berechnet werden.

Zusätzlich lassen sich die Positionen der Markierungen sowie deren Geschwindigkeit und Beschleunigung während des Sprungs untersuchen. Die Ergebnisse werden in Form von Kennzahlen und Diagrammen dargestellt.
"""))

st.subheader("Voraussetzungen für eigene Videos")
st.write("""
Damit eigene Videoaufnahmen mit dem Programm analysiert werden können, müssen einige Voraussetzungen erfüllt sein.

**Aufnahme mit zwei Kameras**
- Beide Videos müssen denselben Sprung aus unterschiedlichen Perspektiven zeigen.
- Die Kameras müssen während der gesamten Aufnahme an einer festen Position bleiben.
- Der Winkel zwischen den Kameras und ihr Abstand zueinander müssen bekannt sein.
- Die Videos müssen dieselbe Bildrate (Frames pro Sekunde, fps) aufweisen.
- Die Aufnahmen müssen zeitlich synchronisiert werden können.

**Kameraparameter**
Für die räumliche Rekonstruktion müssen die geometrischen Eigenschaften der Kameras bekannt sein. Dazu gehören insbesondere:
- Der Abstand und die Ausrichtung der Kameras zueinander.
- Die Auflösung der Videoaufnahmen in Pixeln.
- Die verwendeten Smartphone-Modelle sowie die benötigten Abmessungen in Zentimetern.
- Die für das jeweilige Kameramodell bestimmten Kalibrierungsparameter.

**Markierungen und Aufnahmebedingungen**
- An den Schlittschuhen müssen rote und grüne Markierungen angebracht sein.
- Die Markierungen müssen während der Bewegung möglichst gut sichtbar bleiben.
- Die Farben müssen sich ausreichend deutlich vom Hintergrund unterscheiden.
- Die Lichtverhältnisse sollten während der Aufnahme möglichst konstant sein.
- Beide Markierungen sollten möglichst häufig gleichzeitig in beiden Kameraperspektiven erkennbar sein.

**Weitere Angaben**
Zusätzlich müssen der Absprung- und der Landepunkt beziehungsweise die entsprechenden Frames manuell bestimmt werden. Die erforderlichen Kameraparameter müssen vor der Analyse korrekt eingegeben werden.

Die Genauigkeit der Ergebnisse hängt stark davon ab, wie gut diese Voraussetzungen eingehalten werden. Abweichungen bei der Kameraposition, der Synchronisation oder der Erkennung der Markierungen können zu Ungenauigkeiten bei der 3D-Rekonstruktion und den anschliessenden Berechnungen führen.
""")
