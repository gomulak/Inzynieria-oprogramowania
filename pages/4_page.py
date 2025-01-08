# STRONA Z WYBOREM WIEKU


import streamlit as st


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
        margin-bottom: 1px;  
    }}
    </style>
    """,
    unsafe_allow_html = True
)


def zapisz_wybor(wybor):
    st.session_state["wiek"] = wybor


st.markdown(
    """
    <p class="custom-text" style="font-weight: bold; color: black;">Podaj wiek:</p>
    """,
    unsafe_allow_html = True
)


col1, col2 = st.columns(2)

# Pole na wpisanie lat
with col1:
    lata = st.number_input("", min_value = 0, max_value = 100, step = 1, key = "lata", value = None, placeholder = "Podaj lata")
    if lata is None:
        lata = 0
    st.write("lat")
# Pole na wpisanie miesięcy
with col2:
    miesiace = st.number_input("", min_value = 0, max_value = 11, step = 1, key = "miesiace", value = None,  placeholder = "Podaj miesiące")
    if miesiace is None:
        miesiace = 0
    st.write("miesięcy")


wiek = lata * 12 + miesiace
zapisz_wybor(wiek)


col1, col2, col3 = st.columns((1.5,10,1.3))

with col1:
    st.markdown('<div style="text-align: center;">', unsafe_allow_html = True)
    if st.button("Cofnij"):
        st.switch_page("pages/3_page.py")
    st.markdown('</div>', unsafe_allow_html = True)
with col2:
    st.write(" ")
with col3:
    st.markdown('<div style="text-align: center;">', unsafe_allow_html = True)
    if st.button("Dalej"):
        st.switch_page("pages/5_page.py")
    st.markdown('</div>', unsafe_allow_html = True)
