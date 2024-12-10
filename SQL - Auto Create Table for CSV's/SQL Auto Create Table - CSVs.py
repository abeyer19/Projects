import pandas as pd
import os

# python dtypes to PostgreSQL data type function by way of dictionary
def dtypes_converter(dtype):
    dtypes_dict = {'int64': 'INTEGER',
            'int32': 'INTEGER',
            'int16': 'SMALLINT',
            'int8': 'SMALLINT',
            'float64': 'DOUBLE PRECISION',
            'float32': 'REAL',
            'bool': 'BOOLEAN',
            'object': 'TEXT',
            'datetime64[ns]': 'TIMESTAMP',
            'timedelta64[ns]': 'INTERVAL'}
    return dtypes_dict.get(str(dtype))


# take in a file from specified from the user
path_input = input("File Path: ")


# convert to a pandas dataframe
df = pd.read_csv(path_input)


# get file name
file_name = os.path.basename(path_input)
file_name = file_name.removesuffix(".csv").lower()


# print out the prompt for pgAdmin4
print(f"DROP TABLE IF EXISTS public.{file_name};\n")
print(f"CREATE TABLE IF NOT EXISTS public.{file_name}")
print("(")
for col in df.columns:
    print(f'\t{col} {dtypes_converter(df[col].dtypes).lower()} COLLATE pg_catalog."defult"')
print(");\n")
print(f"ALTER TABLE IF EXISTS public.{file_name}")
print("\tOWNER to postgres;")
