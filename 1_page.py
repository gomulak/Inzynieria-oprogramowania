# STRONA Z WYBOREM GATUNKU


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
    <p class="custom-text" style="font-weight: bold; color: black;">Wybierz gatunek:</p>
    """,
    unsafe_allow_html = True
)


# Funkcja do zapisywania wyboru użytkownika
def zapisz_wybor(wybor):
    st.session_state["gatunek"] = wybor  # Zapisujemy wybór do zmiennej 'gatunek'


# Dwie kolumny do wyświetlenia zdjęć
col1, col2 = st.columns(2)

# Przycisk dla "Kota"
with col1:
    st.markdown(
        """
        <style>
            .img-kot {
                width: 200px;  # Dostosowanie szerokości obrazu
            }
        </style>
        """, unsafe_allow_html=True
    )

    st.markdown(
        """
        <style>
            .stImage {
                margin-left: 50px;
            }

        </style>
        """, unsafe_allow_html = True)
    st.image("kot_gatunek.png", caption = None, use_container_width = False,
             width = 200)
    if st.button("Kot 🐱", key = "kot", help = "Wybierz kota", use_container_width = True):
        zapisz_wybor("kot")
with col2:
    st.markdown(
        """
        <style>
            .image-container {
                display: block;
                margin-left: auto;
                margin-right: auto;
                margin-top: 30px;

            }
        </style>
        """, unsafe_allow_html = True
    )

    st.markdown('<div class="image-container">', unsafe_allow_html = True)
    st.image("pies_gatunek.png", caption = None, use_container_width = False, width = 200, output_format = "PNG")
    st.markdown('</div>', unsafe_allow_html = True)
    if st.button("Pies 🐶", key = "pies", help = "Wybierz psa", use_container_width = True):
        zapisz_wybor("pies")


if "gatunek" in st.session_state:
    gatunek = st.session_state["gatunek"]  # Przypisanie wyboru do zmiennej


col1, col2, col3 = st.columns((1.5, 10, 1.3))

with col1:
    st.write(' ')
with col2:
    st.write(" ")
with col3:
    st.markdown('<div style="text-align: right;">', unsafe_allow_html = True)
    if st.button("Dalej"):
        st.switch_page("pages/2_page.py")
    st.markdown('</div>', unsafe_allow_html = True)
