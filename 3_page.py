# STRONA Z WYBOREM PŁCI


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
    </style>
    """,
    unsafe_allow_html = True
)


st.markdown(
    """
    <style>
    .custom-text {
        font-size: 300px; 
        font-family: 'Poppins', sans-serif;  
        color: #FFFFFF; 
    }
    </style>
    <p class="custom-text" style="font-weight: bold; color: black;">Wybierz płeć:</p>
    """,
    unsafe_allow_html = True
)


def zapisz_wybor(wybor):
    st.session_state["plec"] = wybor


col1, col2 = st.columns(2)

with col1:
    if st.button("samica :female_sign:", key = "samica", help = "Wybierz samicę", use_container_width = True):
        zapisz_wybor("samica")
with col2:
    if st.button("samiec :male_sign:", key = "samiec", help = "Wybierz samca", use_container_width = True):
        zapisz_wybor("samiec")


if "plec" in st.session_state:
    plec = st.session_state["plec"]


col1, col2, col3 = st.columns((1.5,10,1.3))

with col1:
    st.markdown('<div style="text-align: center;">', unsafe_allow_html = True)
    if st.button("Cofnij"):
        st.switch_page("pages/2_page.py")
    st.markdown('</div>', unsafe_allow_html = True)
with col2:
    st.write(" ")
with col3:
    st.markdown('<div style="text-align: center;">', unsafe_allow_html = True)
    if st.button("Dalej"):
        st.switch_page("pages/4_page.py")
    st.markdown('</div>', unsafe_allow_html = True)
