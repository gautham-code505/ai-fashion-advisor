def recommend_outfit(occasion, color):
    if occasion == "college":
        return f"Try a casual {color} t-shirt with jeans"
    elif occasion == "formal":
        return f"Wear a {color} shirt with trousers"
    else:
        return f"{color} outfit works great!"

print(recommend_outfit("college", "black"))
