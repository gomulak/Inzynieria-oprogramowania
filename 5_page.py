# STRONA Z WYBOREM WAGI


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


st.markdown(
    """
    <p class="custom-text" style="font-weight: bold; color: black;">Podaj wagę w kilogramach:</p>
    """,
    unsafe_allow_html = True
)


left_image_url = "maly.png"  # URL lub lokalna ścieżka
right_image_url = "duzy.png"


# Wyświetl obrazy nad sliderem
col1, col2, col3 = st.columns([1, 6, 1])


st.markdown(
    """
    <style>
        .stImage {
            margin-bottom: -50px;
        }
        .stSlider {
            margin-top: -20px;
        }
    </style>
    """, unsafe_allow_html = True)
with col1:
    st.image(left_image_url, use_container_width = True)
with col3:
    st.image(right_image_url, use_container_width = True)


def zapisz_wybor(wybor):
    st.session_state["waga"] = wybor


# Slider między obrazkami
waga = st.slider("", min_value = 0, max_value = 90, value = 50)
zapisz_wybor(waga)


col1, col2, col3 = st.columns((1.5,10,1.3))

with col1:
    st.markdown('<div style="text-align: center;">', unsafe_allow_html = True)
    if st.button("Cofnij"):
        st.switch_page("pages/4_page.py")
    st.markdown('</div>', unsafe_allow_html = True)
with col2:
    st.write(" ")
with col3:
    st.markdown('<div style="text-align: center;">', unsafe_allow_html = True)
    if st.button("Dalej"):
        st.switch_page("pages/6_page.py")
    st.markdown('</div>', unsafe_allow_html = True)
