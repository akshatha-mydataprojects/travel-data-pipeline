#  Cloud Travel Data ETL Pipeline (Python + PostgreSQL)

##  Professional Context

This project was built as part of my transition back into Data Engineering, leveraging my prior experience in SQL database administration and Azure SQL cloud support.  

It demonstrates production-style ETL design principles using Python and a cloud-hosted PostgreSQL data warehouse (Neon).

---

##  Project Overview

This project implements an end-to-end ETL (Extract, Transform, Load) pipeline that:

- Ingests raw travel booking data from CSV files  
- Validates and cleans the data  
- Saves processed data for auditability  
- Loads structured data into Neon PostgreSQL  
- Implements logging and idempotent database inserts  

The goal is to simulate a real-world data engineering workflow using modular architecture and cloud infrastructure.

---

##  Architecture

Raw CSV → Data Validation and cleaning → Transformation- Currency Standardization (EUR, GBP → USD) → Processed CSV → PostgreSQL (Neon Cloud)

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
- Git & GitHub  
- Python logging module  

---

##  Pipeline Features

✔ Modular project structure (ingest / transform / load / utils) 
✔ CSV ingestion (supports large datasets – 200+ records tested)
✔ Data validation checks  
✔ Duplicate removal  
✔ Standardized formatting- Currency standardization to USD 
✔ Idempotent inserts using PostgreSQL `ON CONFLICT`  
✔ Timestamped logging for monitoring  
✔ Automated analytical report generation
✔ Separation of credentials using config.yaml 


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
To Configure database connection

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

SELECT * 
FROM travel_bookings 
WHERE booking_status = 'confirmed';
```

---

##  What This Demonstrates

- Cloud database integration
- End-to-end Data pipeline design
- SQL schema creation
- Data transformation using Pandas
- Logging & monitoring
- Production-style project structuring
- Analytical reporting automation  
- Version control using Git

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
