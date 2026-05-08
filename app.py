from flask import Flask, request, jsonify
from library import RECIPES, STARTING_ELEMENTS
from utils import check_semantic_match

app = Flask(__name__)

# Basic inventory state
state = {
    "inventory": STARTING_ELEMENTS,
    "innovation": 0,
    "degradation": 0
}

@app.route('/')
def index():
    return jsonify({
        "message": "Digital Alchemist API Online",
        "inventory": state["inventory"],
        "stats": {"innovation": state["innovation"], "degradation": state["degradation"]}
    })

@app.route('/combine', methods=['POST'])
def combine():
    data = request.json
    el1 = data.get('el1', '').lower()
    el2 = data.get('el2', '').lower()

    if el1 not in state["inventory"] or el2 not in state["inventory"]:
        return jsonify({"error": "Elements not in inventory"}), 400

    result = check_semantic_match(el1, el2, RECIPES)
    
    if result:
        res_name, inn, deg, lore = result
        if res_name.lower() not in state["inventory"]:
            state["inventory"].append(res_name.lower())
            state["innovation"] += inn
            state["degradation"] += deg
            return jsonify({"success": True, "discovery": res_name, "lore": lore})
        return jsonify({"success": True, "message": "Already discovered"})
    
    return jsonify({"success": False, "message": "No reaction"})

import nltk
from library import RECIPES, STARTING_ELEMENTS

# Attempt to download wordnet if not present
try:
    from nltk.corpus import wordnet as wn
    wn.synsets('test')
except:
    nltk.download('wordnet')
    from nltk.corpus import wordnet as wn

class DigitalAlchemist:
    def __init__(self):
        self.inventory = set(STARTING_ELEMENTS)
        self.innovation = 0
        self.degradation = 0
        self.discovered_count = 0

    def get_synonym_match(self, item1, item2):
        # Normalize and sort to ensure order doesn't matter
        pair = tuple(sorted([item1.lower(), item2.lower()]))
        if pair in RECIPES:
            return RECIPES[pair]
        return None

    def play(self):
        print("====================================")
        print("       ⚗️ DIGITAL ALCHEMIST ⚗️       ")
        print("====================================")
        print("Goal: Reach 'The Emerald Planet' or 'Galactic Civilization'.")
        print("Watch your Degradation! If it exceeds Innovation by 150, you fail.")

        while True:
            print(f"\nInventory ({len(self.inventory)}): {', '.join(sorted(self.inventory))}")
            print(f"Stats: Innovation [{self.innovation}] | Degradation [{self.degradation}]")
            
            if self.degradation > self.innovation + 150:
                print("\n🚨 CRITICAL FAILURE: Ecological Collapse. GAME OVER.")
                break

            user_input = input("\nCombine two elements (or 'quit'): ").strip().lower().split()
            
            if not user_input: continue
            if user_input[0] == 'quit': break
            if len(user_input) != 2:
                print("Please enter exactly two elements.")
                continue
            
            el1, el2 = user_input
            if el1 not in self.inventory or el2 not in self.inventory:
                print(f"You don't have one of those elements yet.")
                continue

            result = self.get_synonym_match(el1, el2)
            
            if result:
                res_name, inn, deg, lore = result
                res_key = res_name.lower()
                if res_key not in self.inventory:
                    self.inventory.add(res_key)
                    self.innovation += inn
                    self.degradation += deg
                    self.discovered_count += 1
                    print(f"\n✨ NEW DISCOVERY: {res_name}")
                    print(f"📖 {lore}")
                    if res_key in ["the_emerald_planet", "galactic_civilization"]:
                        print("\n🏆 VICTORY: You have secured the future of humanity!")
                        break
                else:
                    print(f"\nYou already discovered {res_name}.")
            else:
                print("\n❌ No reaction. Try a different combination.")

if __name__ == '__main__':
    game = DigitalAlchemist()
    game.play()
