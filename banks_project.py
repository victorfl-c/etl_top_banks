from bs4 import BeautifulSoup
from datetime import datetime
import pandas as pd
import numpy as np
import sqlite3
import requests

# Variáveis globais
log_file = "code_log.txt"
url = 'https://web.archive.org/web/20230908091635/https://en.wikipedia.org/wiki/List_of_largest_banks'
table_attribs = ["Name", "MC_USD_Billion"]
db_name = 'Banks.db'
table_name = 'Largest_banks'
csv_path = './Largest_banks_data.csv'
csv_exchange_rate = './exchange_rate.csv'

# Funções

def extract(url, table_attribs):
    page = requests.get(url).text
    data = BeautifulSoup(page, 'html.parser')
    rows = data.find('table', {'class': 'wikitable'}).find_all('tr')

    extracted_data = []
    for row in rows[1:]:  # Ignorar o cabeçalho
        cols = row.find_all('td')
        if cols:
            name = cols[1].text.strip()
            market_cap = cols[2].text.strip().replace('\n', '').replace(',', '')
            extracted_data.append([name, float(market_cap)])
    
    return pd.DataFrame(extracted_data, columns=table_attribs)


def transform(df, exchange_rate_path):
    exchange_rates = pd.read_csv(exchange_rate_path, index_col=0, header=None)
    exchange_rates_dict = exchange_rates.iloc[:, 0].to_dict()  

    exchanges = {
        'GBP': [np.round(x * float(exchange_rates_dict['GBP']), 2) for x in df['MC_USD_Billion']],
        'EUR': [np.round(x * float(exchange_rates_dict['EUR']), 2) for x in df['MC_USD_Billion']],
        'INR': [np.round(x * float(exchange_rates_dict['INR']), 2) for x in df['MC_USD_Billion']]
    }

    df['MC_GBP_Billion'] = exchanges['GBP']
    df['MC_EUR_Billion'] = exchanges['EUR']
    df['MC_INR_Billion'] = exchanges['INR']

    return df

def load_to_csv(df, csv_path):
    df.to_csv(csv_path, index=False)

def load_to_db(df, sql_connection, table_name):
    df.to_sql(table_name, sql_connection, if_exists='replace', index=False)

def run_query(query_statement, sql_connection):
    print(query_statement)
    query_output = pd.read_sql(query_statement, sql_connection)
    print(query_output)

def log_progress(message):
    timestamp_format = '%Y-%m-%d %H:%M:%S'
    now = datetime.now()
    timestamp = now.strftime(timestamp_format)
    with open(log_file, "a") as f:
        f.write(f"{timestamp} : {message}\n")

# Processo ETL
log_progress('Preliminaries complete. Initiating ETL process.')

# Extração
df = extract(url, table_attribs)
log_progress('Data extraction complete. Initiating Transformation process.')

# Transformação
df = transform(df, csv_exchange_rate)
print(df.head())
log_progress('Data transformation complete. Initiating loading process.')

# Carregar CSV
load_to_csv(df, csv_path)
log_progress('Data saved to CSV file.')

# Conexão SQL
sql_connection = sqlite3.connect(db_name)
log_progress('SQL Connection initiated.')

# Carregar no banco de dados
load_to_db(df, sql_connection, table_name)
log_progress('Data loaded to Database as table. Running queries.')

# Consultas

query_statement = f"SELECT * FROM {table_name}"
run_query(query_statement, sql_connection)

query_statement = f"SELECT AVG(MC_GBP_Billion) FROM {table_name}"
run_query(query_statement, sql_connection)

query_statement = f"SELECT name FROM {table_name} LIMIT 5"
run_query(query_statement, sql_connection)

log_progress('Process Complete.')
sql_connection.close()
