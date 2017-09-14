def is_isogram(word):
    """Function determine if a word or phrase is an isogram"""
    word = [ch.lower() for ch in word if ch.isalpha()]
    return len(word) == len(set(word))
