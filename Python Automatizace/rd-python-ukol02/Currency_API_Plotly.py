# UKOL 2: Ziskejte data pomoci verejne API a zobrazte je pomoci Plotly nebo seaborn a ulozte data do souboru csv.
# Martin Filipek, filipek.martin@gmail.com

import datetime
import requests
import pandas as pd
import plotly.graph_objects as go

url = 'https://www.cnb.cz/cs/financni_trhy/devizovy_trh/kurzy_devizoveho_trhu/denni_kurz.txt?date=DD.MM.RRRR'

def replace_date(date, url:str):

    # Format the date to DD.MM.YYYY1
    formatted_date = date.strftime('%d.%m.%Y')
    formatted_url = url.replace('DD.MM.RRRR', formatted_date)
    return(formatted_url)

def get_data(url: str):
   
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            data = response.text
            return data
        else:
            print(f"Error: HTTP {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return None


def main():
    date = input('Zadejte datum devizoveho kurzu ve formatu DD.MM.RRRR: ')           # Vstupni datum od uzivatele
    date = datetime.datetime.strptime(date, '%d.%m.%Y')             # Prevod vstupu na datetime objekt
    formatted_url=replace_date(date, url)                           # Nahrazeni data v URL
    print(f"Formatted API URL: {formatted_url}")
    data = get_data(url=formatted_url)                  # Ziskani dat z API
    print("Ziskana data:")
    print(data)

    data_lines = data.splitlines()                      # Rozdeleni dat na radky                                             
    data_cleaned = "\n".join(data_lines[1:])            # Smazani prvniho radku
    data_cleaned = data_cleaned.replace(',', '.')       # Nahrazeni desetinne carky za tecku   
    data_cleaned = data_cleaned.replace('|', ',')       # Nahrazeni oddelovace z | na ,   
    # Ulozeni ocistenych dat do CSV souboru
    filename = f"Currency_{date.year}{date.month:02d}{date.day:02d}.csv"
    with open(filename, "w", encoding='utf-8') as f:  # "w" = write mode
        f.write(data_cleaned)  
    print(f"Data byla ulozena do souboru: {filename}")                                                                     
    
    # Ukaz sloupcovy graf pomoci Plotly
    df = pd.read_csv(filename, sep=',')                         # Nacteni dat do DataFrame
    fig = go.Figure(data=[go.Bar(x=df['země'], y=df['kurz'], text = df['množství'])])  # Vytvoreni sloupcoveho grafu
    fig.update_layout(title=f'Devizový kurz k datu {date.strftime("%d.%m.%Y")}',
                      xaxis_title='Země',
                      yaxis_title='Kurz')                           
    fig.show()                                                  # Zobrazeni grafu
                                              
if __name__ == "__main__":
    main()