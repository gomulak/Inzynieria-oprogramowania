# STRONA Z WYBOREM RASY


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
        margin-bottom: 1px;  /* Zmniejszamy przerwę między tekstem a selectbox */
    }}
    </style>
    """,
    unsafe_allow_html = True
)


def zapisz_wybor(wybor):
    st.session_state["rasa"] = wybor


if "rasa" not in st.session_state:
    st.session_state["rasa"] = None


st.markdown(
    """
    <p class="custom-text" style="font-weight: bold; color: black;">Wybierz rasę:</p>
    """,
    unsafe_allow_html = True
)


rasy_psy = ['Akita Inu', 'Amstaff', 'Amstaff/Pitbull', 'Beagle', 'Bernardyn', 'Bokser', 'Border Collie',
        'Buldog Francuski', 'Cairn Terrier', 'Cane Corso', 'Cavalier King Charles Spaniel', 'Chart', 'Chihuahua',
        'Cocker Spaniel', 'Cocker Spaniel Amerykański', 'Cocker Spaniel Angielski', 'Dalmatyńczyk', 'Dog Argentyński',
        'Dog Niemiecki', 'Doberman Pincher', 'Foksterier', 'Golden Retriever', 'Gończy Polski',
        'Gryfonik Brukselski', 'Husky', 'Jack Russell Terrier', 'Jamnik', 'Labrador', 'Lhasa Apso', 'Malamut',
        'Maltańczyk', 'Mix Boston', 'Mix Cairn', 'Mix Doberm', 'Mops', 'Nova Scotia Duck Tolling Retriever',
        'Owczarek Belgijski', 'Owczarek Kaukaski', 'Owczarek Niemiecki', 'Owczarek Podhalański',
        'Owczarek Środkowoazjatycki', 'Pekińczyk', 'Pitbul', 'Pinczer', 'Pinczer Miniaturowy', 'Pinczer Średni',
        'Posokowiec', 'Pudel', 'Rhodesian', 'Rottweiler', 'Samojed', 'Seter Irlandzki', 'Shiba Inu', 'Shih Tzu',
        'Sznaucer', 'Sznaucer Miniaturowy', 'Sznaucer Olbrzymi', 'Szpic', 'Szpic Niemiecki Miniaturowy', 'Szpic Wild',
        'Thai Ridge', 'Terier', 'Terier Walijski', 'Toller', 'West Highland White Terrier', 'Wilczak', 'Wyżeł',
        'Wyżeł Francuski', 'Wyżeł Weimarski', 'Yorkshire Terier', 'Kundelek']

rasy_koty = ['Abisyński', 'Bengalski', 'Brytyjski', 'Chausie', 'Devon Rex', 'Europejska', 'Maine Coon', 'Norweski Leśny',
             'Perski', 'Ragdoll', 'Rosyjski Niebieski', 'Selkirk Rex', 'Sfinks', 'Syberyjski', 'Syjamski', 'Syryjski',
             'Święty Kot Birmański', 'Dachowiec']


# Wybór ras w zależności od wybranego gatunku zwierzęcia
if "gatunek" in st.session_state:
    gatunek = st.session_state["gatunek"]

    if gatunek == "kot":
        rasy = rasy_koty
    elif gatunek == "pies":
        rasy = rasy_psy
    else:
        rasy = []

    if st.session_state["rasa"] not in rasy:
        st.session_state["rasa"] = None

    rasa_wybor = st.selectbox(
        "",
        options = rasy,
        index = rasy.index(st.session_state["rasa"]) if st.session_state["rasa"] else 0
    )
    zapisz_wybor(rasa_wybor)

        # Dodatkowy przycisk dla psów
    if gatunek == "pies" and st.button("Kundelek/nie mam pewności"):
        st.session_state["rasa"] = "kundelek"
        zapisz_wybor(rasa_wybor)

        # Dodatkowy przycisk dla kotów
    if gatunek == "kot" and st.button("Dachowiec/nie mam pewności"):
        st.session_state["rasa"] = "dachowiec"
        zapisz_wybor(rasa_wybor)
        
st.write(f"Wybrana rasa: {st.session_state['rasa']}")

col1, col2, col3 = st.columns((1.5,10,1.3))

with col1:
    st.markdown('<div style="text-align: center;">', unsafe_allow_html = True)
    if st.button("Cofnij"):
        st.switch_page("pages/1_page.py")
    st.markdown('</div>', unsafe_allow_html = True)
with col2:
    st.write(" ")
with col3:
    st.markdown('<div style="text-align: right;">', unsafe_allow_html = True)
    if st.button("Dalej"):
        st.switch_page("pages/3_page.py")
    st.markdown('</div>', unsafe_allow_html = True)
