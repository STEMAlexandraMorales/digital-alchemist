import nltk
from nltk.corpus import wordnet as wn
try:
    wn.synsets('metal')
except LookupError:
    nltk.download('wordnet')

def get_semantic_synonyms(word):
    """
    Uses WordNet to find a set of synonyms for a given word.
    This allows the game to be more flexible (e.g., accepting 'petrol' for 'petroleum').
    """
    synonyms = {word.lower()}
    for syn in wn.synsets(word):
        for lemma in syn.lemmas():
            synonyms.add(lemma.name().lower().replace('_', ' '))
    return synonyms

def check_semantic_match(input_a, input_b, recipes):
    """
    Checks if the user's input matches any recipe keys, 
    even if they use a synonym found in WordNet.
    """
    syns_a = get_semantic_synonyms(input_a)
    syns_b = get_semantic_synonyms(input_b)
    
    for recipe_pair in recipes.keys():
        # recipe_pair is a sorted tuple of lowercase strings
        target_a, target_b = recipe_pair
        
        # Check if user syns for A match target A and user syns for B match target B
        # Or vice versa
        if (target_a in syns_a and target_b in syns_b) or            (target_a in syns_b and target_b in syns_a):
            return recipes[recipe_pair]
            
    return None

def format_score_bar(innovation, degradation, length=20):
    """
    Returns a visual string representation of the stability balance.
    """
    total = innovation + degradation
    if total == 0:
        return "[" + "-" * length + "]"
    
    inn_part = int((innovation / total) * length)
    deg_part = length - inn_part
    return "[" + "=" * inn_part + "!" * deg_part + "]"
