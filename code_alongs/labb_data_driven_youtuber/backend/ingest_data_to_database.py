from database import Database
from constants import CLEANED_DATA_PATH, DATABASE_PATH


def ingest_csv_data_to_duckdb():


    for directory_path in CLEANED_DATA_PATH.glob("*"):
        schema_name = directory_path.name
        for csv_path in directory_path.glob("*"):
            table_name = csv_path.name.split(".")[0]


            with Database(DATABASE_PATH) as db:
                db.query(f"CREATE SCHEMA IF NOT EXISTS {schema_name}")
                db.query(f"""
                    CREATE TABLE IF NOT EXISTS {schema_name}.{table_name} AS
                    SELECT * FROM read_csv_auto('{csv_path}');
                """)
   


if __name__ == "__main__":
    ingest_csv_data_to_duckdb()