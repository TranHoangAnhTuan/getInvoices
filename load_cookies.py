import json

def load_cookies_from_json(file_path):
    """Loads cookies from a JSON file.

    Args:
        file_path (str): The path to the JSON file.

    Returns:
        dict: A dictionary containing the loaded cookies, with keys as cookie names and values as cookie values.
    """

    try:
        with open(file_path, 'r') as f:
            cookies_data = json.load(f)
    except FileNotFoundError:
        print(f"Error: JSON file not found at '{file_path}'.")
        return {}
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON format in '{file_path}'.")
        return {}

    return {cookie['name']: cookie['value'] for cookie in cookies_data}


print(load_cookies_from_json('cookies.json'))  # Example usage