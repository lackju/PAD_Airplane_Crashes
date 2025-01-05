# Analiza Katastrof Lotniczych

Ten projekt koncentruje się na analizie historycznych katastrof lotniczych przy użyciu technik przetwarzania i wizualizacji danych. Projekt dostarcza informacji na temat przyczyn wypadków lotniczych, trendów w czasie oraz faz lotu, w których dochodziło do katastrof.

## Pliki w repozytorium

### 1. `plane crashes.csv`
Oryginalny zbiór danych pobrany z Kaggle. Zawiera dane historyczne dotyczące katastrof lotniczych, w tym datę, czas, operatora, typ samolotu oraz przyczyny katastrof.

### 2. `Historical Crashes.ipynb`
Plik Jupyter Notebook zawierający:
- **Czyszczenie danych**: Przygotowanie surowych danych, usuwanie brakujących wartości oraz eliminacja anomalii.
- **Analiza danych**: Eksploracja statystyczna i graficzna danych dotyczących katastrof, w tym analiza trendów, korelacji oraz przyczyn wypadków.

### 3. `cleaned_historical_crashes.csv`
Oczyszczona wersja zbioru danych, przygotowana po usunięciu anomalii i braków w danych w notebooku Jupyter. Jest to główny zbiór danych używany do dalszej analizy oraz tworzenia dashboardu.

### 4. `dashboard_Historical_Crashes.py`
Plik zawierający kod dashboardu stworzonego w Streamlit. Dashboard umożliwia:
- Wyświetlanie ogólnych statystyk dotyczących katastrof lotniczych.
- Analizę przyczyn katastrof w różnych fazach lotu.
- Filtrowanie danych według kraju.
- Wizualizację trendów w czasie.

Aby uruchomić dashboard, należy wykonać w terminalu następujące polecenie:
```bash
streamlit run dashboard_Historical_Crashes.py
```
