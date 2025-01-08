# STRONA STARTOWA


import streamlit as st
st.set_page_config(initial_sidebar_state = "collapsed")


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
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;700&display=swap" rel="stylesheet">
    <style>
        body {
            font-family: 'Poppins', sans-serif;
            line-height: 1.6;
            margin: 20px;
            color: #333;
        }
        .container {
            max-width: 800px;
            margin: 0 auto;
            text-align: center;
        }
        h1 {
            color: #FF69B4;
            font-size: 36px;
        }
        p {
            font-size: 18px;
        }
        ul {
            text-align: left;
            margin: 20px auto;
            padding: 0;
            list-style: none;
        }
        ul li {
            margin: 10px 0;
        }
    </style>
    """, unsafe_allow_html = True
)


st.markdown(
    """
    <div class="container">
        <h1>Witaj w Kalkulatorze Przewidywania Długości Pobytu Zwierząt Domowych w Schronisku!</h1>
        <p>
            Czy wiesz, że przewidywanie czasu, jaki zwierzę spędzi w schronisku, może pomóc w lepszym zarządzaniu zasobami i poprawie jego opieki? Nasze narzędzie analizuje kluczowe dane, aby oszacować, ile dni może potrwać proces adopcji.
        </p>
        <h4>🐕 Jak to działa?</h4>
        <p>
            Wprowadź dane o zwierzęciu, takie jak wiek, rasa, wielkość czy cechy charakteru, a nasz model obliczy przewidywaną liczbę dni do adopcji.
        </p>
        <h4>🐈 Dlaczego to ważne?</h4>
        <ul>
            <li>💗 Pozwala lepiej planować zasoby schroniska.</li>
            <li>💗 Ułatwia skuteczniejszą opiekę nad zwierzętami.</li>
            <li>💗 Pomaga znaleźć rozwiązania skracające czas oczekiwania na nowy dom.</li>
        </ul>
        <p>
            🦴 <strong>Zrób pierwszy krok ku poprawie życia zwierząt w schroniskach!</strong><br>
            Sprawdź nasz kalkulator już teraz i zobacz, jak możemy wspólnie pomóc naszym czworonożnym przyjaciołom.
        </p>
    </div>
    """, unsafe_allow_html = True
)


col1, col2, col3 = st.columns(3)

with col1:
    st.write(' ')
with col2:
    st.markdown('<div style="text-align: center;">', unsafe_allow_html=True)
    if st.button("Kliknij, aby rozpocząć"):
        st.switch_page("pages/1_page.py")
    st.markdown('</div>', unsafe_allow_html=True)
with col3:
    st.write(' ')
