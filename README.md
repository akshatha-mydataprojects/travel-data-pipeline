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

Raw CSV → Data Validation → Transformation → Processed CSV → PostgreSQL (Neon Cloud)

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
```

---

##  Tech Stack

- Python  
- Pandas  
- PostgreSQL (Neon Cloud)  
- psycopg2  
- YAML configuration management  
- Git & GitHub  
- Python logging module  

---

##  Key Features

✔ Modular project structure (ingest / transform / load / utils)  
✔ Data validation checks and cleaning  
✔ Duplicate removal  
✔ Standardized formatting  
✔ Idempotent inserts using PostgreSQL `ON CONFLICT`  
✔ Timestamped logging for monitoring  
✔ Separation of credentials using config.yaml  

---

##  Project Structure

```
travel-data-pipeline/
│
├── data/
│   ├── raw/
│   └── processed/
├── logs/
├── src/
│   ├── ingest/
│   ├── transform/
│   ├── load/
│   └── utils/
├── config/
├── requirements.txt
└── README.md
```

---

##  How to Run

Activate virtual environment:

```
venv\Scripts\activate
```

Run the pipeline:

```
python -m src.ingest.ingest_csv_to_postgres
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
- Data pipeline architecture design
- SQL schema creation
- Data transformation using Pandas
- Logging & monitoring practices
- Production-style project structuring

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
