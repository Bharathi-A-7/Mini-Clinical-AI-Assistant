import os
import json
import yaml

def load_yaml_file(file_path):
    """
    Load a YAML file and return its contents as a dictionary.

    Args:
        file_path (str): Full path to the YAML file.

    Returns:
        dict: Parsed contents of the YAML file.
    """
    with open(file_path, 'r', encoding='utf-8') as f:
            return yaml.safe_load(f)
    

def write_json_to_file(data, file_path):
    """
    Write a dictionary to a JSON file.

    Args:
        data (dict): The dict to write.
        file_path (str): The  file path.
    """
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False)



def load_prompts_from_dir(directory_path):
    """
    Load all JSON files from the given directory.
    
    Args:
        directory_path (str): Path to the folder containing JSON prompt files.
        
    Returns:
        dict: Dictionary mapping filename to its JSON content.
    """
    prompt_dict = {}
    
    for filename in os.listdir(directory_path):
        if filename.endswith(".json"):
            filepath = os.path.join(directory_path, filename)
            with open(filepath, 'r', encoding='utf-8') as file:
                data = json.load(file)
                key = os.path.splitext(filename)[0]  # remove .json extension
                prompt_dict[key] = data
    
    return prompt_dict


def read_text_file(file_path):
    """
    Read and return the contents of a text file.

    Args:
        file_path (str): Path to the text file.

    Returns:
        str: File contents as a string.
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()
    

def write_text_to_file(text, file_path):
    """
    Write a string to a text file.

    Args:
        text (str): The text to write.
        file_path (str): The file path.
    """
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(text)



