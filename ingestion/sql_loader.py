from sqlalchemy import create_engine
import pandas as pd

def load_sql(connection_string, query):
    engine = create_engine(connection_string)
    df = pd.read_sql(query, engine)
    return df