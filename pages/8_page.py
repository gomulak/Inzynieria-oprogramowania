# STRONA Z MODELEM I WYNIKIEM


import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import time
import base64


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
    unsafe_allow_html=True
)


# Do modelu
dane = pd.read_csv("dane.csv", header=0)
dane = pd.DataFrame(dane)
(train_set, test_set) = train_test_split(dane, train_size = 0.7, random_state = 13)
liczba_kolumn = len(dane.columns)


train_inputs = train_set.iloc[:, 0:(liczba_kolumn - 1)]
train_days = train_set.iloc[:, (liczba_kolumn - 1)]
test_inputs = test_set.iloc[:, 0:(liczba_kolumn - 1)]
test_days = test_set.iloc[:, (liczba_kolumn - 1)]


model = RandomForestRegressor(max_depth = 5, random_state = 13, n_estimators = 50)
model.fit(train_inputs, train_days)


dane_uzytkownika = st.session_state.get("dane_do_modelu", {})
df = pd.DataFrame([dane_uzytkownika])


# Zmiana na małe litery
df = df.applymap(lambda x: x.lower() if isinstance(x, str) else x)

df["rasa"] = df["rasa"].str.lower().str.strip()
df["gatunek"] = df["gatunek"].str.lower().str.strip()
df["płeć"] = df["płeć"].str.lower().str.strip()


# Zamiana nazw rasy, żeby działały w modelu
df.loc[df['rasa'] == 'toller', 'rasa'] = 'nova scotia duck tolling retriev'
df.loc[df['rasa'] == 'nova scotia duck tolling retriever', 'rasa'] = 'nova scotia duck tolling retriev'
df.loc[df['rasa'] == 'wyżeł francuski', 'rasa'] = 'wyżeł fran'
df.loc[df['rasa'] == 'dachowiec', 'rasa'] = 'europejska'
df.loc[df['rasa'] == 'kundelek', 'rasa'] = 'mieszaniec'
df.loc[df['rasa'] == 'selkirk rex', 'rasa'] = 'selkirk re'


kategorie = ["przyjazny", "agresywny", "chory", "bojący się", "aktywny"]
for kategoria in kategorie:
    df[kategoria] = df["cechy"].apply(lambda x: 1 if kategoria in x else 0)


kolumny_docelowe = dane.columns


df_dopasowany = pd.get_dummies(df, columns = ["rasa", "gatunek", "płeć"])
df_dopasowany = df.reindex(columns = kolumny_docelowe, fill_value = 0)
df_dopasowany = df_dopasowany.drop(columns = ["czas_pobytu_dni"], errors = 'ignore')
df_dopasowany["wiek_miesiące"] = df["wiek_miesiące"]
df_dopasowany["waga_kg"] = df["waga_kg"]


st.write("Dane pierwotne:", df)

# Mapowanie wartości z kolumny "gatunek" do odpowiedniej kolumny dummy
if "gatunek" in df.columns:
    for gatunek_value in df["gatunek"].unique():
        column_name = f"gatunek_{gatunek_value}"
        if column_name in df_dopasowany.columns:
            df_dopasowany[column_name] = (df["gatunek"] == gatunek_value).astype(int)

# Mapowanie wartości z kolumny "płeć" do odpowiedniej kolumny dummy
if "płeć" in df.columns:
    for plec_value in df["płeć"].unique():
        column_name = f"płeć_{plec_value}"
        if column_name in df_dopasowany.columns:
            df_dopasowany[column_name] = (df["płeć"] == plec_value).astype(int)

# Mapowanie wartości z kolumny "rasa" do odpowiedniej kolumny dummy
if "rasa" in df.columns:
    for rasa_value in df["rasa"].unique():
        column_name = f"rasa_{rasa_value}"
        if column_name in df_dopasowany.columns:
            df_dopasowany[column_name] = (df["rasa"] == rasa_value).astype(int)

st.write("Po zastosowaniu get_dummies/Dane wejściowe do modelu:", df_dopasowany)

liczba_dni = model.predict(df_dopasowany)[0]


# Konwersja pliku GIF na base64
gif_path = "gif.gif"
with open(gif_path, "rb") as f:
    gif_data = f.read()
    gif_base64 = base64.b64encode(gif_data).decode("utf-8")


gif_html = f'''
<div style="display: flex; justify-content: center;">
    <img src="data:image/gif;base64,{gif_base64}" alt="GIF" width="300" height="300"/>
</div>
'''


placeholder = st.empty()
placeholder.markdown(gif_html, unsafe_allow_html = True)
time.sleep(2)
placeholder.empty()  # Ukrycie GIF-a
if liczba_dni <= 30:
    st.markdown(
        f"""
        <style>
            .stSuccess div {{
                display: flex;
                justify-content: center;
                align-items: center;
                text-align: center;
            }}
        </style>
        """, unsafe_allow_html = True)
    st.success(f"Szacowany czas pobytu wprowadzonego zwierzęcia w schronisku wynosi {int(liczba_dni)} dni.")

elif 30 < liczba_dni <= 60:
    st.markdown(
        f"""
        <style>
            .stWarning div {{
                display: flex;
                justify-content: center;
                align-items: center;
                text-align: center;
            }}
        </style>
        """, unsafe_allow_html = True)
    st.warning(f"Szacowany czas pobytu wprowadzonego zwierzęcia w schronisku wynosi {int(liczba_dni)} dni.")

else:
    st.markdown(
        f"""
        <style>
            .stError div {{
                display: flex;
                justify-content: center;
                align-items: center;
                text-align: center;
            }}
        </style>
        """, unsafe_allow_html = True)
    st.error(f"Szacowany czas pobytu wprowadzonego zwierzęcia w schronisku wynosi {int(liczba_dni)} dni.")
st.markdown('<p style="font-size: 12px;">Możliwy błąd szacowań wynosi 65 dni.</p>', unsafe_allow_html = True)


col1, col2, col3 = st.columns(3)

with col1:
    st.write(' ')
with col2:
    st.markdown('<div style="text-align: center;">', unsafe_allow_html = True)
    if st.button("Oblicz ponownie"):
        st.switch_page("main.py")
    st.markdown('</div>', unsafe_allow_html = True)
with col3:
    st.write(' ')
