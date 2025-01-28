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


# Take in a file from specified from the user
while True:
    path_input = input("File Path: ")

    if not path_input:
        print("No input, exiting program...")
        break

    # Check if the path has quotes
    if (path_input[0] == "'") or (path_input[-1] == "'"):
        print('Please remove quotations around the file path.')
        continue

    # Check if the file exists
    if not os.path.exists(path_input):
        print("File not found, please try again.")
        continue

    # Try to read in CSV file
    try:
        df = pd.read_csv(path_input)
        print("\nFile path is valid! \nAccessing File.")
        break

# Error handling
    except KeyboardInterrupt:
        print("\nProgram interrupted by user. Exiting...")
        break

    except pd.errors.ParserError as e:
        print(f"ParserError: There was an issue parsing the CSV file. {e}")

    except IndexError as e:
        print(f"Index Error: {e}")
    
    except Exception as e:
        print(f"Exception Error: {e}")

    except TypeError as e:
        print(f"Type Error: {e}")

    except PermissionError as e:
        print(f"Permission Error: {e}")

    except KeyboardInterrupt:
        print("Program interrupted by user. Exiting...")
        break

    except NameError as e:
        print(f"Name Error: {e}")
        break


# Get file name and print output correctly
if 'df' in locals():  # Check if df is defined before using it
    file_name = os.path.basename(path_input)
    file_name = file_name.removesuffix(".csv").lower()

    # Print out the prompt for pgAdmin4
    print(f"\nDROP TABLE IF EXISTS public.{file_name};\n")
    print(f"CREATE TABLE IF NOT EXISTS public.{file_name}")
    print("(")
    for col in df.columns:
        print(f'\t{col} {dtypes_converter(df[col].dtypes).lower()} COLLATE pg_catalog."defult"')
    print(");\n")
    print(f"ALTER TABLE IF EXISTS public.{file_name}")
    print("\tOWNER to postgres;")
else:
    print("DataFrame 'df' not created. Exiting.")