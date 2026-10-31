import streamlit as st

main_page=st.Page("Auswertung.py", title="Analyse & Berechnungen", icon="📊")
page_2=st.Page("Videoanalyse.py", title="Videosegmentierung", icon="🎥")

pg=st.navigation([main_page, page_2])

pg.run()
