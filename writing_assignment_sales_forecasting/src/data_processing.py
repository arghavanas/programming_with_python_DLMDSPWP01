import sqlite3
import pandas as pd
import os

class DataProcessor:
    """
    Handles data retrieval and preprocessing tasks.
    """

    def __init__(self, db_path, csv_path=None):
        """
        :param db_path: Path to the SQLite database file.
        :param csv_path: CSV file path to create DB if needed.
        """
        self.db_path = db_path
        self.csv_path = csv_path

    def _connect_db(self):
        """Establishes a connection to the SQLite database."""
        return sqlite3.connect(self.db_path)

    def create_database_from_csv(self):
        """
        Creates the SQLite DB from CSV data.
        """
        if self.csv_path is None:
            raise ValueError("CSV path must be provided to create the database.")
        # Load CSV file into a DataFrame
        df = pd.read_csv(self.csv_path, parse_dates=['InvoiceDate'])
        # Ensure the folder for the database exists
        os.makedirs(os.path.dirname(self.db_path), exist_ok=True)
        # Create (or overwrite) the SQLite database and table 'online_retail_ii'
        conn = sqlite3.connect(self.db_path)
        df.to_sql('online_retail_ii', conn, if_exists='replace', index=False)
        conn.close()
        print("Database created from CSV.")

    def load_data(self):
        """
        Loads data from the SQLite table.
        Filters on InvoiceDate between 2009-12-01 and 2011-11-30.
        (Ensure full months for proper seasonal aggregation.)
        """
        # If the database file doesn't exist, create it from CSV
        if not os.path.exists(self.db_path):
            if self.csv_path is not None:
                print("Database file not found. Creating from CSV...")
                self.create_database_from_csv()
            else:
                raise FileNotFoundError("Database file not found and CSV path not provided.")

        conn = self._connect_db()
        query = """
        SELECT 
            InvoiceDate,
            Quantity,
            Price
        FROM online_retail_ii
        WHERE InvoiceDate >= '2009-12-01'
          AND InvoiceDate <= '2011-11-30';
        """
        df = pd.read_sql(query, conn, parse_dates=['InvoiceDate'])
        conn.close()
        return df

    def transform_data(self, df):
        """
        Transforms raw data into a time-series friendly format.
         - Removes rows with negative Quantity (cancellations/returns)
         - Combines Quantity * Price to create 'Sales'
         - Aggregates sales by month.
        """
        # Remove cancellations/returns (negative Quantity)
        df = df[df['Quantity'] > 0]

        # Calculate Sales using Price (not UnitPrice)
        df['Sales'] = df['Quantity'] * df['Price']

        # Set InvoiceDate as index
        df.set_index('InvoiceDate', inplace=True)

        # Resample by month and sum sales
        monthly_sales = df['Sales'].resample('M').sum()

        return monthly_sales
