
def replace_word_in_string(text, old_word, new_word):
    """
    This function takes a string, an old word and a new word as input and replaces all occurrences of the old word in the string with the new word.

    Parameters:
        text (str): the input string.
        old_word (str): word that needs to be replaced.
        new_word (str): word that will replace the old word.

    Returns:
        str: the modified text with replaced words.
    """
    new_text = text.replace(old_word, new_word)
    return new_text

