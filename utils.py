import nltk
import os
from nltk.corpus import wordnet as wn

nltk_data_path = "/tmp/nltk_data"
if not os.path.exists(nltk_data_path):
    os.makedirs(nltk_data_path)
nltk.data.path.append(nltk_data_path)

# Only download if not already present in the tmp folder
try:
    wn.ensure_loaded()
except:
    nltk.download('wordnet', download_dir=nltk_data_path)
    nltk.download('omw-1.4', download_dir=nltk_data_path)

def check_semantic_match(input_a, input_b, recipes):
    syns_a = {input_a.lower()}
    syns_b = {input_b.lower()}
    
    for syn in wn.synsets(input_a):
        for lemma in syn.lemmas():
            syns_a.add(lemma.name().lower().replace('_', ' '))
    for syn in wn.synsets(input_b):
        for lemma in syn.lemmas():
            syns_b.add(lemma.name().lower().replace('_', ' '))

    for recipe_pair in recipes.keys():
        target_a, target_b = recipe_pair
        if (target_a in syns_a and target_b in syns_b) or \
           (target_a in syns_b and target_b in syns_a):
            return recipes[recipe_pair]
    return None
