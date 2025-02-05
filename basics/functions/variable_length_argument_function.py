def make_sandwich(*ingredients):
    return f"Sandwich with: {', '.join(ingredients)}"

print(make_sandwich("ham", "cheese", "lettuce"))