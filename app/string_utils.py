"""
Utility to perform advanced string comparisons.
"""

from difflib import SequenceMatcher
import textdistance


def calculate_match_degree(txt1:str,txt2:str) -> float:
    """
    Given two strings, finds the longest common substring.
    Returns the degree of the match based on that longest
    substring.
    """
    match = SequenceMatcher(None, txt1, txt2).find_longest_match()
    return match.size/max(len(txt1),len(txt2))

def calcualte_text_distance(txt1:str,txt2:str) -> float:
    """
    Uses a text distance metric to calculate the similarity
    between two texts. This is not a sub-string match but a
    comparison of similar terms occurring in both texts.
    """
    algs = textdistance.algorithms
    return algs.levenshtein.normalized_similarity(txt1, txt2)


def testing_tim():
    print('Hello github')