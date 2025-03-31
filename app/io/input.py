import pandas as pd


def read_input():
    """
    Reads user's input from the console.

    Returns:
        str: User's input.
    """
    return input("Enter text: ")


def read_file(file_path):
    """
    Reads file's content and returns it as string.

    Args:
        file_path (str): The path to the file that needs to be read.

    Returns:
        str: Content of the file. Empty string if file is empty.

    Raises:
        FileNotFoundError: File or directory does not exist.
    """
    try:
        with open(file_path, "r") as file:
            content = file.read()
        return content
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {file_path}")


def read_file_pd(file_path):
    """
    Reads csv file's content and returns it as string.

    Args:
        file_path (str): The path to the file that needs to be read.

    Returns:
        str: Content of the file. Empty string if file is empty.

    Raises:
        FileNotFound: File or directory does not exist.
    """
    try:
        df = pd.read_csv(file_path)
        if df.empty:
            return ""
        return df.to_string(index=False)
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {file_path}")
