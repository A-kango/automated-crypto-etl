
# 🚀 Automated Crypto ETL Pipeline

This project is an **automated ETL (Extract, Transform, Load) pipeline** that pulls real-time cryptocurrency market data from the [CoinGecko API](https://www.coingecko.com/), transforms and cleans the data using **Python and Pandas**, and loads it into a **PostgreSQL** data warehouse for reporting and analysis. The pipeline is automatically scheduled to run daily at **6:00 AM**.

---

## 📌 Features

- 🔁 **Automated ETL**: Scheduled daily run at 6:00 AM using the `schedule` library.
- 🌐 **API Extraction**: Real-time data from CoinGecko.
- 🧹 **Data Transformation**: Cleaning, formatting, and restructuring with Pandas.
- 🗄️ **Data Warehouse**: Loaded into PostgreSQL for querying.
- 📊 **Power BI Ready**: ODBC connection enables BI dashboards.
- ✅ **Production-Ready**: Includes automation, error handling, and logging.


## ⚙️ Technologies Used

- 🐍 Python
- 📦 Pandas
- 🌐 Requests
- 🛢️ PostgreSQL
- 🔌 SQLAlchemy
- 📈 Power BI (via pyODBC)
- ⏰ Schedule (for automation)

## 🚀 How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/A-kango/automated-crypto-etl.git
cd automated-crypto-etl
###2. Install Dependencies
pip install -r requirements.txt
##3. Set Up PostgreSQL
   Make sure you have a PostgreSQL database running locally:

   Host: localhost

   Port: 5432

   User: postgres

   Password: ----

   Database: Crytocurrency_wahehouse

   Create this database if it doesn’t exist.
  
---
##4. Run the ETL Script Manually
  python Webscraping.py

##5. Run the Scheduler Script (Auto Daily Run at 6:00 AM)
python "Auto-Crypto pipeline.py"

### ✅ `requirements.txt`

Create a `requirements.txt` file and paste this:

```txt
requests
pandas
sqlalchemy
pyodbc
psycopg2-binary
schedule

👨‍💻 Author
Engineer Anthony Kangogo
Data Engineering | ETL Pipelines | API Integration | Python + SQL


  
