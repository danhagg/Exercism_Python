def is_pangram(word):
    """Determines if word is pangram"""
is_pangram = lambda word: not set('abcdefghijklmnopqrstuvwxyz') - set(word.lower())

# Spaces, punctuation char from the test string set not in the alphabet set 
# Force sets into the simplest True/False values in Python,
# then containers with content are 'True' and empty containers are 'False'.
# not also changes True -> False, and False -> True.
# Then return that True/False result
