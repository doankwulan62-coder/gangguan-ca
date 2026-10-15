from pathlib import Path
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Ca · SSA-Nyala",
    page_icon="🧪",
    layout="wide",
    initial_sidebar_state="collapsed",
)

HTML_FILE = Path(__file__).parent / "Analisis_Ca_SSA-Nyala-4.html"

if not HTML_FILE.exists():
    st.error("File Analisis_Ca_SSA-Nyala-4.html tidak ditemukan. Pastikan file ini ada di repository yang sama dengan app.py.")
    st.stop()

html = HTML_FILE.read_text(encoding="utf-8")

# Aplikasi HTML asli dijalankan di dalam iframe Streamlit.
# Interaksi JavaScript pada aplikasi tetap berjalan di dalam iframe tersebut.
components.html(html, height=1000, scrolling=True)
