import pandas as pd
import os


def load_dataset(file_path: str) -> pd.DataFrame:
    """
    Load the dataset from a CSV file.

    Args:
        file_path (str): The path to the CSV file.

    Returns:
        pd.DataFrame: A pandas DataFrame containing the dataset.
    """
    try:
        dataset = pd.read_csv(file_path)
        return dataset
    except FileNotFoundError:
        raise FileNotFoundError(f"The file at {file_path} was not found.")
    except Exception as e:
        raise RuntimeError(f"An error occurred while loading the dataset: {e}")


def validate_dataset(df: pd.DataFrame) -> pd.DataFrame:
    """
    Validate that the dataset contains the required columns, including 'das_score'.

    Args:
        df (pd.DataFrame): The input DataFrame containing depression, anxiety, stress, and das scores.

    Returns:
        pd.DataFrame: The validated DataFrame.
    """
    required_columns = [
        "depression_score",
        "anxiety_score",
        "stress_score",
        "das_score",
    ]
    missing_columns = [col for col in required_columns if col not in df.columns]

    if missing_columns:
        raise ValueError(
            f"The DataFrame is missing the following required columns: {', '.join(missing_columns)}"
        )

    return df


def show_datasets() -> list:
    """
    Scan the 'data' folder in the parent directory and return a list of files present in it.

    Returns:
        list: A list of datasets that can be used.
    """
    current_dir = os.path.dirname(
        os.path.abspath(__file__)
    )  # Get directory of current file
    parent_dir = os.path.dirname(current_dir)  # Get parent directory
    data_folder = os.path.join(parent_dir, "data")
    if not os.path.exists(data_folder):
        raise FileNotFoundError(
            "The 'data' folder does not exist in the parent directory."
        )

    return [
        file
        for file in os.listdir(data_folder)
        if os.path.isfile(os.path.join(data_folder, file))
    ]
    
    