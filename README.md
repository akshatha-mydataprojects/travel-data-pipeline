# Travel Data Pipeline

**Project Overview:**  
Production-grade travel data pipeline: CSV → ETL → Neon PostgreSQL → Analytics

**Architecture:**  
- Source CSV files  
- Python ETL scripts  
- PostgreSQL warehouse (Neon)  
- Logging & validation

**Tools & Stack:**  
- Python, Pandas  
- Neon PostgreSQL  
- YAML for configuration  
- GitHub for version control

**Folder Structure:**  
- data/: raw + processed data  
- src/: ETL scripts  
- sql/: table creation & queries  
- logs/: ETL logs  
- config/: database configuration

**Next Steps / Improvements:**  
- Add automated scheduling (Airflow / Lambda)  
- Integrate S3 for raw storage  
- Migrate to Redshift for enterprise readiness
