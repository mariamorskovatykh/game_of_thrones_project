
import os

def replace_word_in_file(file_path:str, old_word:str, new_word:str)->None:
    """
    Replaces a specific word in a given file with another word and saves the changes.

    Parameters:
    file_path (str): The path to the file.
    old_word (str): The word to be replaced.
    new_word (str): The word to replace the old word with.

    Returns:
    None
    """
    if not os.path.exists(file_path):
        print("File path is invalid.")
        return

    with open(file_path, "r") as file:
        file_data = file.read()

    file_data = file_data.replace(old_word, new_word)

    with open(file_path, "w") as file:
        file.write(file_data)
