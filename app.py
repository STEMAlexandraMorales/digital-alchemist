from flask import Flask, request, jsonify
from library import RECIPES, STARTING_ELEMENTS
from utils import check_semantic_match

app = Flask(__name__)

state = {
    "inventory": [e.lower() for e in STARTING_ELEMENTS], # Force lowercase
    "innovation": 0,
    "degradation": 0
}

@app.route('/')
def home():
    # Return the game state as JSON for the JavaScript to read
    return jsonify({
        "inventory": state["inventory"],
        "stats": {
            "innovation": state["innovation"],
            "degradation": state["degradation"]
        }
@app.route('/combine', methods=['POST'])
def combine():
    data = request.get_json()
    if not data:
        return jsonify({"success": False, "message": "No data received"}), 400
        
    el1 = data.get('el1', '').lower()
    el2 = data.get('el2', '').lower()

    if el1 not in state["inventory"] or el2 not in state["inventory"]:
        return jsonify({"success": False, "message": "Elements not in inventory"}), 400

    result = check_semantic_match(el1, el2, RECIPES)
    
    if result:
        res_name, inn, deg, lore = result
        res_key = res_name.lower()
        
        is_new = False
        if res_key not in state["inventory"]:
            state["inventory"].append(res_key)
            state["innovation"] += inn
            state["degradation"] += deg
            is_new = True
            
        return jsonify({
            "success": True, 
            "discovery": res_name, 
            "new": is_new, 
            "lore": lore
        })
    
    return jsonify({"success": False, "message": "No reaction"})
