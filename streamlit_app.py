import streamlit as st

st.set_page_config(layout="wide")

# CSS pour styliser les boutons
st.markdown("""
    <style>
    .stButton button {
        background-color: #4CAF50;
        color: white;
        border: none;
        border-radius: 12px;
        padding: 10px 24px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        margin: 4px 2px;
        transition-duration: 0.4s;
        cursor: pointer;
    }
    .stButton button:hover {
        background-color: white;
        color: black;
        border: 2px solid #4CAF50;
    }
    </style>
""", unsafe_allow_html=True)

# --- PAGE SETUP ---
about_page = st.Page(
    page = "views/about_me.py",
    title = "A propos de moi",
    icon = ":material/account_circle:",
    default=True
)

formation_1_page = st.Page(
    page = "views/BI_with_SQL_and_Shiny.py",
    title = "Business Intelligence avec SQL, R et Shiny",
    icon=":material/database:" #icones sur le site de Bootstrap
)

# --- NAVIGATION SETUP [WITHOUT SECTIONS] ---
pg = st.navigation(pages = [about_page, formation_1_page])


# --- RUN NAVIGATION ---
pg.run()