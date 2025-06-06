import pyodbc
import os

def insert_project_update(data):
    conn_str = os.environ.get("AZURE_SQL_CONNECTION_STRING")
    with pyodbc.connect(conn_str) as conn:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO project_updates (project_id, status) VALUES (?, ?)",
            data["project_id"], data["status"]
        )
        conn.commit()
