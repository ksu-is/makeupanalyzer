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














