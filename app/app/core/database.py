import os
import psycopg2
from psycopg2.extras import RealDictCursor
from dotenv import load_dotenv

load_dotenv()

class Database:
    def __init__(self):
        self.host = os.getenv("DB_HOST")
        self.database = os.getenv("DB_NAME")
        self.user = os.getenv("DB_USER")
        self.password = os.getenv("DB_PASSWORD")
        self.port = os.getenv("DB_PORT")

    def get_connection(self):
        try:
            # Usamos la URL completa (como la de Neón)
            conn_string = (
                f"postgresql://{self.user}:{self.password}"
                f"@{self.host}/{self.database}"
                f"?sslmode=require&channel_binding=require"
            )
            return psycopg2.connect(
                conn_string,
                cursor_factory=RealDictCursor
            )
        except Exception as e:
            print(f"Error de conexión a la BD: {e}")
            return None