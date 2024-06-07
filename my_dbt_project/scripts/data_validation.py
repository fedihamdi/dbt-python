import pandas as pd
import sqlalchemy
from sqlalchemy import create_engine

# Configure database connection
DATABASE_URI = 'your_database_connection_string'
engine = create_engine(DATABASE_URI)

# Load data into a DataFrame
query = "SELECT * FROM your_table"
df = pd.read_sql(query, engine)

# Perform data validation
def validate_data(df):
    if df.isnull().values.any():
        print("Data contains null values")
    else:
        print("Data is clean")

validate_data(df)

# Optionally, write the validated data back to the database
df.to_sql('validated_table', engine, if_exists='replace', index=False)
