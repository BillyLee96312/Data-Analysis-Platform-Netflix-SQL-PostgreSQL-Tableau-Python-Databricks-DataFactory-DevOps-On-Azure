# Sample Data (Module 01)

This directory is for the small sample dataset students will use for Sprint 1. Because most Netflix datasets have licensing restrictions, we recommend one of the following options:

1. Instructor-provided sample CSV
   - Place the sample CSV at `Module 01/sample_data/netflix_sample.csv`.

2. Use a public Netflix dataset (Kaggle / open data) ? manual download
   - Download the dataset and copy the CSV to `Module 01/sample_data/`.

3. Use a trimmed subset of a larger dataset
   - Instructors may provide a small, synthetic subset (a few rows) suitable for labs.

How to upload the sample data to ADLS Gen2 using AzCopy:

- Example:

```powershell
azcopy copy "C:\path\to\Module 01\sample_data\netflix_sample.csv" "https://stnetflix{studentid}.blob.core.windows.net/raw/netflix_sample.csv?sas-token"
```

If no sample dataset is provided, use a small CSV (even 10 rows) with columns compatible with the schema in `Module 01/sql/postgresql_schema.sql`.
