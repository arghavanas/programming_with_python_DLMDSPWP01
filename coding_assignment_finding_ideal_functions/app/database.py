from sqlalchemy import create_engine
import pandas as pd


class DataSet:
    """Base class for managing datasets with SQLite and Pandas."""

    def __init__(self, name: str, engine, table_name: str):
        self.name = name
        self.engine = engine
        self.table_name = table_name
        self.df = pd.DataFrame()

    def load_csv_into_db(self, csv_path: str):
        temp_df = pd.read_csv(csv_path)
        temp_df.sort_values(by=temp_df.columns[0], inplace=True)
        temp_df.reset_index(drop=True, inplace=True)
        temp_df.to_sql(self.table_name, self.engine, if_exists="replace", index=False)
        print(f"[INFO] Loaded CSV '{csv_path}' into table '{self.table_name}'.")

    def read_db_into_df(self):
        self.df = pd.read_sql(f"SELECT * FROM {self.table_name}", self.engine)
        print(f"[INFO] Loaded table '{self.table_name}' from DB (rows={len(self.df)})")
