# STRONA Z PODSUMOWANIEM DANYCH WPROWADZONYCH PRZEZ UŻYTKOWNIKA


import streamlit as st
import pandas as pd


bg_color = "#FFB6C1"
text_color = "#000000"


st.markdown(
    f"""
    <style>
    .stApp {{
        background-color: {bg_color};
        color: {text_color};
    }}
    .custom-text {{
        font-size: 300px; 
        font-family: 'Poppins', sans-serif;  
        color: #FFFFFF; 
        margin-bottom: 10px;  
    }}
    </style>
    """,
    unsafe_allow_html = True
)


st.markdown(
    """
    <p class="custom-text" style="font-weight: bold; color: black;">Podsumowanie danych:</p>
    """,
    unsafe_allow_html = True
)


total_months = st.session_state.get("wiek", 0)
years = total_months // 12
months = total_months % 12
wiek_tekst = f"{years} lat i {months} miesięcy"


# Tworzenie słownika z danymi
dane = {
    "Gatunek": [st.session_state.get("gatunek", "Nie wybrano")],
    "Rasa": [st.session_state.get("rasa", "Nie podano")],
    "Płeć": [st.session_state.get("plec", "Nie wybrano")],
    "Wiek": [wiek_tekst],
    "Waga (kg)": [st.session_state.get("waga", 0)],
    "Cechy": [st.session_state.get("wybrane_cechy", "Niezidentyfikowany")],
}


# Tworzenie DataFrame
df = pd.DataFrame(dane)


# Wyświetlenie tabeli
st.dataframe(df, hide_index = True, use_container_width = True)

st.session_state["dane_do_modelu"] = {
    "gatunek": st.session_state.get("gatunek", "Nie wybrano"),
    "rasa": st.session_state.get("rasa", "Nie podano"),
    "płeć": st.session_state.get("plec", "Nie wybrano"),
    "wiek_miesiące": st.session_state.get("wiek", 0),
    "waga_kg": st.session_state.get("waga", 0),
    "cechy": st.session_state.get("wybrane_cechy", "Niezidentyfikowany"),
}

col1, col2, col3 = st.columns(3)

with col1:
    st.write(" ")
with col2:
    st.markdown('<div style="text-align: center;">', unsafe_allow_html = True)
    if st.button("Przelicz liczbę dni"):
        st.switch_page("pages/8_page.py")
    st.markdown("</div>", unsafe_allow_html = True)
with col3:
    st.write(" ")
