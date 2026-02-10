import psycopg2
import yaml

def get_connection():
    with open("config/config.yaml", "r") as f:
        config = yaml.safe_load(f)

    db = config["database"]
    conn = psycopg2.connect(
        host=db["host"],
        port=db["port"],
        dbname=db["name"],
        user=db["user"],
        password=db["password"]
    )
    return conn

if __name__ == "__main__":
    try:
        conn = get_connection()
        print("✅ Database connection successful")
        conn.close()
    except Exception as e:
        print("❌ Database connection failed:", e)
