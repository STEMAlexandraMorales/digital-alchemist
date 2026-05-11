from flask import Flask, request, jsonify
import os
from library import RECIPES, STARTING_ELEMENTS
from utils import check_semantic_match

app = Flask(__name__)

# Game State - Initialized with starting elements from library.py
# Using a list comprehension to ensure all base elements are lowercase
state = {
    "inventory": [e.lower().replace(" ", "_") for e in STARTING_ELEMENTS],
    "innovation": 0,
    "degradation": 0
}

@app.route('/')
def home():
    # If the browser is asking for a webpage, serve the index.html file
    if 'text/html' in request.headers.get('Accept', ''):
        try:
            # Assumes index.html is in the same root directory
            with open('index.html', 'r') as f:
                return f.read()
        except FileNotFoundError:
            return "CRITICAL ERROR: index.html not found in root directory.", 404
    
    # Provide current state if requested via API
    return jsonify({
        "inventory": state["inventory"],
        "stats": {
            "innovation": state["innovation"],
            "degradation": state["degradation"]
        }
    })

@app.route('/combine', methods=['POST'])
def combine():
    data = request.get_json()
    if not data:
        return jsonify({"success": False, "message": "No data received"}), 400
        
    # Get elements and normalize them to match library keys (lowercase + underscores)
    el1 = data.get('el1', '').lower().strip().replace(" ", "_")
    el2 = data.get('el2', '').lower().strip().replace(" ", "_")

    # Security check: Ensure the player actually owns these elements
    if el1 not in state["inventory"] or el2 not in state["inventory"]:
        return jsonify({"success": False, "message": "Elements not found in your system inventory."}), 400

    # Use the semantic utility to check for a valid recipe
    result = check_semantic_match(el1, el2, RECIPES)
    
    if result:
        res_name, inn, deg, lore = result
        # Standardize the result key for inventory storage
        res_key = res_name.lower().replace(" ", "_")
        
        is_new = False
        if res_key not in state["inventory"]:
            state["inventory"].append(res_key)
            state["innovation"] += int(inn)
            state["degradation"] += int(deg)
            is_new = True
            
        return jsonify({
            "success": True, 
            "discovery": res_name, # Returns the "Pretty Name" for UI display
            "innovation": inn,
            "degradation": deg,
            "new": is_new, 
            "lore": lore
        })
    
    return jsonify({"success": False, "message": "The elements remain inert. No reaction detected."})

if __name__ == "__main__":
    # Local development setting
    app.run(debug=True)
