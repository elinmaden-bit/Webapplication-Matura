import streamlit as st

st.set_page_config(page_title="Eiskunstlauf Analyse",page_icon="⛸️",layout="wide")
main_page=st.Page("Auswertungen.py", title="Analyse & Berechnungen", icon="📊", default=True)
page_2=st.Page("Videoanalyse.py", title="Videosegmentierung", icon="🎥")

pg=st.navigation([main_page, page_2])

pg.run()
