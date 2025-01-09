# STRONA Z WYBOREM CECH


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
        margin-bottom: 10px;  
    }}
    </style>
    """,
    unsafe_allow_html = True
)


st.markdown(
    """
    <p class="custom-text" style="font-weight: bold; color: black;">Wybierz cechy, które opisują Twoje zwierzę:</p>
    """,
    unsafe_allow_html = True
)


# Inicjalizacja cech w session_state
if "cechy" not in st.session_state:
    st.session_state["cechy"] = {
        "aktywny": False,
        "przyjazny": False,
        "chory": False,
        "agresywny": False,
        "bojący się": False,
        "niezidentyfikowany": False
    }


# Wyświetlenie toggle dla cech
col1, col2 = st.columns([1, 6])

with col1:
    st.write("aktywny")
with col2:
    aktywny = st.toggle("", key = "aktywny", value = st.session_state["cechy"]["aktywny"])
    st.session_state["cechy"]["aktywny"] = aktywny


col1, col2 = st.columns([1, 6])

with col1:
    st.write("przyjazny")
with col2:
    przyjazny = st.toggle("", key = "przyjazny", value = st.session_state["cechy"]["przyjazny"])
    st.session_state["cechy"]["przyjazny"] = przyjazny


col1, col2 = st.columns([1, 6])

with col1:
    st.write("chory")
with col2:
    chory = st.toggle("", key = "chory", value = st.session_state["cechy"]["chory"])
    st.session_state["cechy"]["chory"] = chory


col1, col2 = st.columns([1, 6])

with col1:
    st.write("agresywny")
with col2:
    agresywny = st.toggle("", key = "agresywny", value = st.session_state["cechy"]["agresywny"])
    st.session_state["cechy"]["agresywny"] = agresywny


col1, col2 = st.columns([1, 6])

with col1:
    st.write("bojący się")
with col2:
    bojacy_sie = st.toggle("", key = "bojący się", value = st.session_state["cechy"]["bojący się"])
    st.session_state["cechy"]["bojący się"] = bojacy_sie


# Przycisk "Nie wiem"
if st.button("Nie wiem"):
    st.session_state["cechy"] = {
        "aktywny": False,
        "przyjazny": False,
        "chory": False,
        "agresywny": False,
        "bojący się": False,
        "niezidentyfikowany": True
    }


# Tworzenie listy wybranych cech
st.session_state["wybrane_cechy"] = ", ".join([k for k, v in st.session_state["cechy"].items() if v])
st.write(st.session_state["cechy"])

col1, col2 = st.columns([1, 6])

with col1:
    st.write(' ')


col1, col2, col3 = st.columns((1.5,10,1.3))

with col1:
    st.markdown('<div style="text-align: center;">', unsafe_allow_html = True)
    if st.button("Cofnij"):
        st.switch_page("pages/5_page.py")
    st.markdown('</div>', unsafe_allow_html = True)
with col2:
    st.write(" ")
with col3:
    st.markdown('<div style="text-align: center;">', unsafe_allow_html = True)
    if st.button("Dalej"):
        st.switch_page("pages/7_page.py")
    st.markdown('</div>', unsafe_allow_html = True)
