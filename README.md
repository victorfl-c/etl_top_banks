

# Sistema Automatizado de ETL para os 10 Maiores Bancos por Capitalização de Mercado

## 📋 **Visão Geral**
Este projeto automatiza o processo de extração, transformação e carregamento (ETL) de dados sobre os 10 maiores bancos do mundo por capitalização de mercado. Ele obtém dados da Wikipedia, converte as capitalizações de mercado de USD para GBP, EUR e INR e armazena os resultados em um arquivo CSV e em um banco de dados para análises futuras.

## 🚀 **Funcionalidades**
- **Raspagem Web**: Extrai dados atualizados sobre os maiores bancos utilizando BeautifulSoup.
- **Transformação de Dados**: Converte valores de capitalização de mercado de USD para GBP, EUR e INR com base em taxas de câmbio fornecidas.
- **Armazenamento de Dados**: Salva os dados processados localmente em um arquivo CSV e os carrega em um banco de dados SQLite.
- **Consultas SQL**: Executa consultas SQL personalizadas para análise dos dados.
- **Logs de Progresso**: Registra eventos importantes durante o processo ETL.

## 🛠 **Tecnologias Utilizadas**
- **Python**: Linguagem principal do projeto.
- **Bibliotecas**:
  - `BeautifulSoup`: Para raspagem de dados web.
  - `pandas`: Para manipulação e análise de dados.
  - `numpy`: Para cálculos numéricos.
  - `sqlite3`: Para operações com bancos de dados.
  - `requests`: Para obtenção de dados HTML.

## 📂 **Estrutura do Projeto**
```plaintext
|-- exchange_rate.csv       # Taxas de câmbio para GBP, EUR, INR
|-- Largest_banks_data.csv  # Dados processados em formato CSV
|-- Banks.db                # Banco de dados SQLite com os dados processados
|-- code_log.txt            # Arquivo de log do processo ETL
|-- main.py                 # Script principal em Python
```

## 📖 **Como Usar**

### 1. Pré-requisitos
Certifique-se de ter instalado:
- Python 3.8+
- Bibliotecas necessárias (use `pip install -r requirements.txt` para instalar as dependências)

### 2. Configuração
1. Clone este repositório:
   ```bash
   git clone <link-do-repositorio>
   cd <pasta-do-repositorio>
   ```
2. Insira as taxas de câmbio no arquivo `exchange_rate.csv` no formato:
   ```csv
    Currency,Rate
    EUR,0.93
    GBP,0.8
    INR,82.95
   ```

### 3. Execute o Script
Execute o script Python para rodar o processo ETL:
```bash
python main.py
```

### 4. Resultado
- Os dados processados serão salvos no arquivo `Largest_banks_data.csv`.
- Os dados serão carregados no banco de dados `Banks.db`.
- Logs estarão disponíveis no arquivo `code_log.txt`.

## 🧾 **Consultas SQL**
Exemplos de consultas executadas no processo ETL:
1. Buscar todos os dados:
   ```sql
   SELECT * FROM Largest_banks;
   ```
2. Calcular a capitalização de mercado média em GBP:
   ```sql
   SELECT AVG(MC_GBP_Billion) FROM Largest_banks;
   ```
3. Buscar os nomes dos 5 maiores bancos:
   ```sql
   SELECT name FROM Largest_banks LIMIT 5;
   ```

## 📈 **Melhorias Futuras**
- Adicionar suporte a mais moedas.
- Agendar execuções automáticas do ETL com um agendador de tarefas (ex.: cron).
- Implementar tratamento de erros para a raspagem de dados e operações no banco de dados.

## 🤝 **Contribuindo**
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests.

## 📧 **Contato**
Em caso de dúvidas ou feedback, entre em contato via LinkedIn ou e-mail.

---
🚀 Feliz codificação!
