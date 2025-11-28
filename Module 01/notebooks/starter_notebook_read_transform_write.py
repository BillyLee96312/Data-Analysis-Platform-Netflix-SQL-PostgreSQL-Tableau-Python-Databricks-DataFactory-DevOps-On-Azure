# Starter Databricks PySpark Notebook (Python file)
# Reads Netflix CSV files from ADLS Gen2 'raw' container, performs simple transformations,
# writes processed data to 'processed' container (Parquet), and writes the same data to PostgreSQL via JDBC.

# Parameters:
# - raw_path: path to CSV files, e.g. 'abfss://raw@stnetflix{studentid}.dfs.core.windows.net/netflix_data.csv'
# - processed_path: path to write processed parquet files
# - jdbc_url: JDBC URL for PostgreSQL
# - jdbc_user/jdbc_password: credentials (should be kept in secret scope / Key Vault)

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, to_date
import os

# Replace defaults with DB and storage config (or pass as widget values in Databricks)
raw_path = os.environ.get('NETFLIX_RAW_PATH', '/dbfs/mnt/raw/netflix_sample.csv')
processed_path = os.environ.get('NETFLIX_PROCESSED_PATH', '/dbfs/mnt/processed/netflix_sample.parquet')
JDBC_URL = os.environ.get('NETFLIX_JDBC_URL','jdbc:postgresql://pgnetflix.example:5432/analytics')
JDBC_USER = os.environ.get('NETFLIX_JDBC_USER','<user>')
JDBC_PASSWORD = os.environ.get('NETFLIX_JDBC_PASSWORD','<password>')

# Use Spark session provided by Databricks
spark = SparkSession.builder.getOrCreate()

# Read CSV
df = spark.read.option('header', 'true').csv(raw_path)
print('Input records:', df.count())

# Simple transformation: select columns and parse dates
transformed = (
    df.select('show_id', 'type', 'title', 'director', 'cast', 'country', 'date_added', 'release_year')
      .withColumn('date_added', to_date(col('date_added'), 'MMMM d, yyyy'))
)

transformed.show(5)

# Write to ADLS processed container in parquet
transformed.write.mode('overwrite').parquet(processed_path)
print('Wrote processed data to', processed_path)

# Write to PostgreSQL using JDBC (ensure security: use secrets/key vaults, not hard-coded values)
properties = {
    'user': JDBC_USER,
    'password': JDBC_PASSWORD,
    'driver': 'org.postgresql.Driver'
}

jdbc_table = 'netflix.netflix_shows'
transformed.write.jdbc(url=JDBC_URL, table=jdbc_table, mode='append', properties=properties)
print('Inserted records into PostgreSQL table', jdbc_table)

# End of the starter notebook script
print('Done.')
