favorite_chais = [
    "Masala Chai", "Green Tea", "Masala Chai",
    "Lemon Tea", "Green Tea", "Elaichi chai"
]

unique_chais = {chai for chai in favorite_chais}
print(unique_chais)

recipes = {
    "Masala Chai": ["ginger", "cardamom", "clove"],
    "Elaichi chai": ["ginger", "milk"],
    "Spicy chai": ["ginger", "black pepper", "clove"]
}

unique_spices = {spice for ingredients in recipes.values() for spice in ingredients}
print(unique_spices)