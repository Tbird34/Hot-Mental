import pandas as pd

def load_csv(filepath):
    """
    Load a CSV file into a Pandas DataFrame.

    Parameters:
    filepath (str): The path to the CSV file.

    Returns:
    DataFrame: The loaded data as a Pandas DataFrame.
    """
    try:
        df = pd.read_csv(filepath)
        print("File loaded successfully.")
        return df
    except FileNotFoundError:
        print("File not found. Please check the file path.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
file_path = '/Users/damonnamin/desktop/MLHealth/data/diabetes-dataset.csv'  # Replace with your file path
dataframe = load_csv(file_path)

# Optional: Display the first few rows of the dataframe
if dataframe is not None:
    print(dataframe.head())
