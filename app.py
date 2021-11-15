import streamlit as st
from utils import *

st.title("Sitemap Analyser")

with st.form(key="sitemap_form"):
    sitemaps = st.text_area(label = "Paste the urls of your sitemaps", height = 300)
    submit = st.form_submit_button("Analyse")

if submit:
    sitemaps = sitemaps.split()
    df = get_sitemap_df(sitemaps)
    st.download_button(data=df.to_csv(index=False), label="Download CSV", file_name = "Sitemap Analyser.csv")
    st.write(df)
