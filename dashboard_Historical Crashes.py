import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Wczytanie danych
@st.cache_data
def load_data():
    data = pd.read_csv("Cleaned_Historical_Crashes.csv")
    data['Date'] = pd.to_datetime(data['Date'], errors='coerce')
    return data

dataset = load_data()

# Nagłówek dashboardu
st.title("Dashboard: Analiza Katastrof Lotniczych")
st.markdown("Prezentacja danych dotyczących katastrof lotniczych w formie wykresów, tabel i statystyk.")

# Ogólne statystyki
st.header("Ogólne Statystyki")
st.dataframe(dataset.describe())

# Słowniczek
st.subheader("Opis kolumn:")
column_descriptions = {
    "Date": "Data katastrofy",
    "Time": "Czas katastrofy",
    "Aircraft": "Typ samolotu",
    "Operator": "Linia lotnicza",
    "Country": "Kraj katastrofy",
    "Pax on board": "Liczba pasażerów na pokładzie",
    "Crew on board": "Liczba załogi na pokładzie",
    "Total fatalities": "Łączna liczba ofiar katastrofy",
    "Crash cause": "Przyczyna katastrofy",
    "Flight phase": "Faza lotu, w której doszło do katastrofy",
    "YOM": "Rok produkcji samolotu (Year of Manufacture)"
}
for col, desc in column_descriptions.items():
    st.markdown(f"- **{col}**: {desc}")

st.subheader("Opis faz lotu:")
flight_phase_descriptions = {
    "Taxiing": "Ruch samolotu na ziemi, np. kołowanie po pasie startowym.",
    "Takeoff (climb)": "Start samolotu i początkowa faza wznoszenia.",
    "Flight": "Faza lotu na stałej wysokości, często nazywana przelotem.",
    "Landing (descent or approach)": "Zniżanie samolotu i podejście do lądowania.",
    "Parking": "Samolot jest na ziemi, np. po zakończeniu kołowania."
}
for phase, desc in flight_phase_descriptions.items():
    st.markdown(f"- **{phase}**: {desc}")

# Liczba katastrof w czasie
st.header("Liczba katastrof w czasie")
yearly_crashes = dataset['Date'].dt.year.value_counts().sort_index()
plt.figure(figsize=(10, 6))
plt.plot(yearly_crashes.index, yearly_crashes.values, label='Liczba katastrof')
plt.title("Liczba katastrof na przestrzeni lat")
plt.xlabel("Rok")
plt.ylabel("Liczba katastrof")
plt.grid()
st.pyplot(plt)

# Przyczyny katastrof w różnych fazach lotu
st.header("Przyczyny katastrof w poszczególnych fazach lotu")
phase_causes = dataset.groupby(['Flight phase', 'Crash cause']).size().reset_index(name='Count')
plt.figure(figsize=(12, 8))
sns.barplot(data=phase_causes, x='Flight phase', y='Count', hue='Crash cause')
plt.title("Przyczyny katastrof w poszczególnych fazach lotu")
plt.xlabel("Faza lotu")
plt.ylabel("Liczba katastrof")
st.pyplot(plt)

# Filtr - wybór kraju
st.header("Filtruj dane dla danego kraju")
country = st.selectbox("Wybierz kraj:", options=sorted(dataset['Country'].dropna().unique()))
filtered_data = dataset[dataset['Country'] == country]
st.write(f"Katastrofy w kraju: {country}")
st.dataframe(filtered_data)