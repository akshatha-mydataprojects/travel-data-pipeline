#  End-to-End ETL Pipeline for Travel Booking Data (Python + PostgreSQL)

##  Professional Context

This project was built as part of my transition back into Data Engineering, leveraging my prior experience in SQL database administration and Azure SQL cloud support.  

It simulates a real-world use case for a global online travel booking company and demonstrates production-style ETL design using Python and a cloud-hosted PostgreSQL data warehouse (Neon).

---

##  Business Scenario

The company receives daily booking data exports from multiple regions, in different currencies (USD, EUR, GBP), and lacks centralized reporting. Finance struggles to calculate total revenue in USD, and leadership cannot track destination performance or monthly booking trends reliably.

###  Objective

The objective is to:

- Centralize raw booking data into a cloud data warehouse  
- Standardize all prices into USD  
- Validate and clean incoming datasets  
- Enable automated analytical reporting  
- Provide business-ready insights such as revenue by destination and monthly booking trends  

##  How the Pipeline Solves It

The pipeline addresses the business challenges as follows:

- **Centralized Data**: Ingests raw CSVs from multiple regions into a single Neon PostgreSQL warehouse  
- **Data Validation & Cleaning**: Removes duplicates, ensures correct date formats, and checks for missing critical values  
- **Currency Standardization**: Converts EUR and GBP to USD for consistent revenue calculations  
- **Automated Reporting**: Generates analytical summaries such as revenue per destination, monthly bookings, top destinations, and booking status distribution  
- **Logging & Monitoring**: Tracks ETL execution to ensure reliability and reproducibility  

This allows business stakeholders to make **data-driven decisions**, monitor **destination performance**, and accurately **track revenue trends** in USD.

---
##  Project Overview

This project implements an end-to-end ETL (Extract, Transform, Load) pipeline that:

- Ingests raw travel booking data from CSV files  
- Validates and cleans the data  
- Saves processed data for auditability  
- Loads structured data into Neon PostgreSQL  
- Implements logging and idempotent database inserts
- Generates Analytical reports  

---
##  Architecture

Raw CSV → Data Validation → Cleaning and Transformation → Processed CSV → PostgreSQL (Neon Cloud) → Generate Analytical Reports

```
data/raw/
    ↓
src/transform/
    ↓
data/processed/
    ↓
src/load/
    ↓
Neon PostgreSQL
    ↓  
Generate Analytical Reports
```

---

##  Tech Stack

- Python  
- Pandas
- SQL 
- PostgreSQL (Neon Cloud)   
- YAML configuration management    
- Python logging module
- Git & GitHub 

---

##  Pipeline Features

- Modular project structure (ingest / transform / load / utils) 
- CSV ingestion (supports large datasets)
- Data validation checks  
- Duplicate removal  
- Standardized formatting- Currency Standardization (EUR, GBP → USD) 
- Idempotent inserts using PostgreSQL `ON CONFLICT`  
- Timestamped logging for monitoring  
- Automated analytical report generation
- Separation of credentials using config.yaml 

---

##  Project Structure

```
travel-data-pipeline/
│
├── data/
│   ├── raw/                # Raw input datasets
│   ├── processed/          # Cleaned data files
│
├── logs/                   # ETL execution logs
│
├── portfolio_outputs/      # Analytical output summaries
│
├── sql/
│   ├── schema/             # Table creation scripts
│   ├── models/             # Analytical SQL queries
│
├── src/
│   ├── ingest/             # ETL ingestion logic
│   ├── transform/          # Data cleaning & normalization
│   ├── load/               # Reporting & aggregation scripts
│   ├── utils/              # Database connection utilities
│
├── generate_csv.py         # Script to generate large sample dataset
├── requirements.txt
└── README.md
```

---
##  Database Schema

```sql
CREATE TABLE IF NOT EXISTS travel_bookings (
    booking_id INT PRIMARY KEY,
    user_id INT,
    destination VARCHAR(100),
    booking_date DATE,
    travel_date DATE,
    price NUMERIC,
    currency VARCHAR(10),
    booking_status VARCHAR(20)
);
```

---

##  Example Analytical Reports Generated

- Total Revenue  
- Revenue by Destination  
- Bookings per Month  
- Top Destinations by Booking Volume  
- Booking Status Distribution  

Reports are saved in:

portfolio_outputs/

---
##  How to Run

pip install -r requirements.txt

Activate virtual environment:

```
venv\Scripts\activate
```
To Configure database connection:

Create a file:

src/utils/config.py

Add your Neon credentials:

```python
DB_HOST = "your_neon_host"
DB_NAME = "your_database"
DB_USER = "your_username"
DB_PASSWORD = "your_password"
```

To run the ETL pipeline:

```
python -m src.ingest.ingest_csv_to_postgres
```
To Generate Analytical reports:

```
python -m src.load.load_summary
```
---

##  Example Queries

```sql
SELECT COUNT(*) FROM travel_bookings;

SELECT destination, COUNT(*) AS booking_count
FROM travel_bookings
GROUP BY destination
ORDER BY booking_count DESC
LIMIT 5;

```

---


##  Future Enhancements

- Airflow orchestration
- AWS S3 integration
- Data quality framework
- CI/CD automation

---

## 👩‍💻 Author

**Akshatha B**  
SQL | Cloud | Data Engineering  

Open to Data Engineering opportunities.
