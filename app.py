import streamlit as st

st.set_page_config(page_title="Eiskunstlauf Analyse",page_icon="⛸️",layout="wide")
main_page=st.Page("Infos.py", title="Über das Projekt", default=True)
page_2=st.Page("Auswertungen.py", title="Analyse & Berechnungen", icon="📊")

pg=st.navigation([main_page, page_2])

pg.run()
