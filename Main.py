import pandas as pd
import os

#here i am asking for the specific database
file_name = "ingredient makeup.xlsx"
file_path = r'C: /Users/alondra/Downloads'
file = os.path.join(file_path,file_name)

df = pd.read_excel(file) #use pandas on it

# This is a simple code that we will expand the project on. 

pore_clogging_ingredients = {
    "coconut oil": "Coconut oil is pore-clogging because the molecules are too big for your pore size, especially if you already struggle with keratinization.",
    "lanolin": "Lanolin is highly comedogenic and can trap dirt and bacteria in your pores, leading to breakouts.",
    "isopropyl myristate": "Isopropyl myristate clogs pores and exacerbates acne-prone skin.",
    "wheat germ oil": "Wheat germ oil has a high comedogenic rating and can block pores, causing acne.",
    "algae extract": "Algae extract can be too rich for sensitive or acne-prone skin, leading to clogged pores.",
}

# Making a function to analyze ingredients
def analyze_ingredients(ingredient_list):
    print("Analyzing ingredients: \n")
    for ingredient in ingredient_list:
        ingredient_lower = ingredient.lower()  
        if ingredient_lower in pore_clogging_ingredients:
            print(ingredient.capitalize() + " is not good for your skin.")
            print("Reason: " + pore_clogging_ingredients[ingredient_lower] + "\n")
        else:
            print(ingredient.capitalize() + " appears to be safe for your skin.\n")
    print("Analysis complete! ˚✧₊⁎❝᷀ົཽ≀ˍ̮ ❝᷀ົཽ⁎⁺˳✧༚ \nYou are now on your way to clearer skin! ☆*:.｡. o(≧▽≦)o .｡.:*☆")

# Example list of ingredients to analyze including both good and bad
ingredient_list = [
    "Coconut Oil", 
    "Aloe Vera", 
    "Lanolin", 
    "Vitamin E", 
    "Isopropyl Myristate"
]

# Calling it
analyze_ingredients(ingredient_list)



# This is the basis for part two of what I want the program to also do
base_compatibility = {
    "water": "Water-based products work best with other water-based products.",
    "silicone": "Silicone-based products work best with other silicone-based products.",
}

# Function to analyze compatibility between two products
def analyze_compatibility(product_1, base_1, product_2, base_2):
    print("Analyzing product compatibility: \n")
    
    base_1_lower = base_1.lower()
    base_2_lower = base_2.lower()
    
    # Checking if base presented is even in the list of ingredients to look for
    if base_1_lower not in base_compatibility or base_2_lower not in base_compatibility:
        print("Unknown base detected. Ensure both products have either 'water' or 'silicone' as their base.")
        return

    # Compare bases for compatibility
    if base_1_lower == base_2_lower:
        print(product_1.capitalize() + " (" + base_1.capitalize() + "-based) and " + 
              product_2.capitalize() + " (" + base_2.capitalize() + "-based) are compatible!")
        print("Reason: " + base_compatibility[base_1_lower] + "\n")
        print("Your makeup look is on its way to perfection! ✨ (ﾉ◕ヮ◕)ﾉ*:･ﾟ✧\n")
    else:
        print(product_1.capitalize() + " (" + base_1.capitalize() + "-based) and " + 
              product_2.capitalize() + " (" + base_2.capitalize() + "-based) are NOT compatible.")
        print("Reason: Mixing " + base_1.capitalize() + "-based and " + base_2.capitalize() + 
              "-based products can cause separation and poor blending.\n")
        print("Consider matching product bases for a flawless application! ✨ (*´∇｀*)\n")

#Temporary example 
analyze_compatibility("primer", "water", "foundation", "silicone")
analyze_compatibility("primer", "water", "foundation", "water")









