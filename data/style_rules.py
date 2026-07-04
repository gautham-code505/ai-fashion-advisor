# data/style_rules.py

STYLE_MAPPINGS = {
    "Office": {
        "Men": {"style": "Sharp & Professional", "palette": ["#1A1A1A", "#4A4A4A", "#F5F5F5", "#0F2027"]},
        "Women": {"style": "Elegant Corporate", "palette": ["#2C3E50", "#EAECEE", "#D5D8DC", "#17202A"]},
        "Unisex": {"style": "Modern Professional", "palette": ["#34495E", "#BDC3C7", "#ECF0F1", "#2C3E50"]}
    },
    "Casual": {
        "Men": {"style": "Relaxed Streetwear", "palette": ["#3498DB", "#ECF0F1", "#95A5A6", "#2980B9"]},
        "Women": {"style": "Chic & Effortless", "palette": ["#E74C3C", "#FDF2E9", "#F5B041", "#CB4335"]},
        "Unisex": {"style": "Everyday Minimalist", "palette": ["#7F8C8D", "#ECF0F1", "#BDC3C7", "#2C3E50"]}
    },
    "Party": {
        "Men": {"style": "Evening Dapper", "palette": ["#000000", "#C0392B", "#F39C12", "#1C2833"]},
        "Women": {"style": "Glamorous Evening", "palette": ["#8E44AD", "#F1C40F", "#000000", "#4A235A"]},
        "Unisex": {"style": "Night Out Glam", "palette": ["#17202A", "#D4AC0D", "#7B241C", "#1B2631"]}
    },
    "College": {
        "Men": {"style": "Smart Campus", "palette": ["#2E86C1", "#F2F3F4", "#5D6D7E", "#1B4F72"]},
        "Women": {"style": "Trendy Campus", "palette": ["#F1948A", "#FDEDEC", "#F8C471", "#C0392B"]},
        "Unisex": {"style": "Campus Casual", "palette": ["#1ABC9C", "#E8F8F5", "#73C6B6", "#0E6251"]}
    },
    "Festival": {
        "Men": {"style": "Traditional Festive", "palette": ["#922B21", "#F9E79F", "#B9770E", "#641E16"]},
        "Women": {"style": "Vibrant Ethnic", "palette": ["#E67E22", "#FAD7A1", "#CB4335", "#7E5109"]},
        "Unisex": {"style": "Festive Fusion", "palette": ["#D35400", "#FDEBD0", "#A04000", "#78281F"]}
    },
    "Wedding Guest": {
        "Men": {"style": "Classic Formal", "palette": ["#1F618D", "#EBF5FB", "#85929E", "#154360"]},
        "Women": {"style": "Regal Elegance", "palette": ["#C39BD3", "#F4ECF7", "#7D3C98", "#4A235A"]},
        "Unisex": {"style": "Sophisticated Guest", "palette": ["#76448A", "#F5EEF8", "#5B2C6F", "#4A235A"]}
    },
    "Vacation": {
        "Men": {"style": "Tropical Resort", "palette": ["#1ABC9C", "#FEF9E7", "#F1C40F", "#0E6655"]},
        "Women": {"style": "Breezy Resort", "palette": ["#48C9B0", "#E8F8F5", "#F4D03F", "#117A65"]},
        "Unisex": {"style": "Relaxed Vacation", "palette": ["#5DADE2", "#EBF5FB", "#F5B041", "#1B4F72"]}
    }
}

def get_style_info(gender, occasion):
    occ_data = STYLE_MAPPINGS.get(occasion, STYLE_MAPPINGS["Casual"])
    return occ_data.get(gender, occ_data["Unisex"])

def generate_why_it_suits(gender, skin_tone, body_shape, occasion):
    reasons = []
    
    if skin_tone in ["Fair", "Wheatish"]:
        reasons.append("The selected colors provide a beautiful contrast to your lighter undertones.")
    elif skin_tone in ["Medium", "Olive"]:
        reasons.append("These warm and earthy hues perfectly complement your neutral/olive complexion.")
    else:
        reasons.append("These rich, vibrant tones will look absolutely stunning against your deep skin tone.")
        
    if body_shape == "Hourglass":
        reasons.append("The silhouettes are chosen to naturally highlight your well-defined waistline.")
    elif body_shape == "Pear":
        reasons.append("This look balances your proportions by drawing attention upwards.")
    elif body_shape == "Inverted Triangle":
        reasons.append("The bottomwear adds a bit of volume to perfectly balance your broader shoulders.")
    elif body_shape == "Rectangle":
        reasons.append("These pieces add subtle curves and create a structured, flattering silhouette.")
    elif body_shape == "Apple":
        reasons.append("The relaxed fit around the midsection ensures comfort while looking incredibly chic.")
        
    if occasion == "Office":
        reasons.append("It maintains a professional edge without compromising on personal style.")
    elif occasion in ["Festival", "Wedding Guest"]:
        reasons.append("The intricate details bring out a festive grandeur suitable for celebrations.")
    else:
        reasons.append("It hits the perfect balance between comfortable and trendy for your occasion.")
        
    return reasons

OUTFIT_TEMPLATES = {
    "Men": {
        "College": [
            {
                "slots": ["topwear", "bottomwear", "footwear", "accessory", "optional"],
                "categories": {
                    "topwear": ["t-shirts", "shirts"],
                    "bottomwear": ["jeans", "trousers"],
                    "footwear": ["footwear"],
                    "accessory": ["watches", "accessories"],
                    "optional": ["glasses", "perfumes", "bags"]
                }
            }
        ],
        "Casual": [
            {
                "slots": ["topwear", "bottomwear", "footwear", "accessory", "optional"],
                "categories": {
                    "topwear": ["t-shirts", "shirts"],
                    "bottomwear": ["jeans", "trousers"],
                    "footwear": ["footwear"],
                    "accessory": ["watches", "accessories"],
                    "optional": ["glasses", "perfumes", "bags"]
                }
            }
        ],
        "Vacation": [
            {
                "slots": ["topwear", "bottomwear", "footwear", "accessory", "optional"],
                "categories": {
                    "topwear": ["t-shirts", "shirts"],
                    "bottomwear": ["jeans", "trousers"],
                    "footwear": ["footwear"],
                    "accessory": ["watches", "accessories"],
                    "optional": ["glasses", "perfumes", "bags"]
                }
            }
        ],
        "Office": [
            {
                "slots": ["topwear", "bottomwear", "footwear", "accessory", "optional"],
                "categories": {
                    "topwear": ["shirts", "blazers"],
                    "bottomwear": ["trousers"],
                    "footwear": ["footwear"],
                    "accessory": ["accessories", "watches"],
                    "optional": ["perfumes", "bags"]
                }
            }
        ],
        "Party": [
            {
                "slots": ["topwear", "bottomwear", "footwear", "accessory", "optional"],
                "categories": {
                    "topwear": ["shirts", "t-shirts", "blazers"],
                    "bottomwear": ["trousers", "jeans"],
                    "footwear": ["footwear"],
                    "accessory": ["watches", "accessories"],
                    "optional": ["glasses", "perfumes"]
                }
            }
        ],
        "Wedding Guest": [
            {
                "slots": ["topwear", "bottomwear", "footwear", "accessory", "optional"],
                "categories": {
                    "topwear": ["shirts", "blazers", "kurtas"],
                    "bottomwear": ["trousers"],
                    "footwear": ["footwear"],
                    "accessory": ["watches", "accessories"],
                    "optional": ["perfumes"]
                }
            }
        ],
        "Festival": [
            {
                "slots": ["topwear", "bottomwear", "footwear", "accessory", "optional"],
                "categories": {
                    "topwear": ["kurtas", "shirts"],
                    "bottomwear": ["trousers", "jeans"],
                    "footwear": ["footwear"],
                    "accessory": ["watches", "accessories"],
                    "optional": ["perfumes"]
                }
            }
        ],
    },
    "Women": {
        "College": [
            {
                "slots": ["topwear", "bottomwear", "footwear", "optional", "accessory"],
                "categories": {
                    "topwear": ["t-shirts", "shirts", "kurtas"],
                    "bottomwear": ["jeans", "trousers"],
                    "footwear": ["footwear"],
                    "optional": ["bags", "glasses"],
                    "accessory": ["accessories", "watches"]
                }
            }
        ],
        "Casual": [
            {
                "slots": ["topwear", "bottomwear", "footwear", "optional", "accessory"],
                "categories": {
                    "topwear": ["t-shirts", "shirts", "kurtas", "dresses"],
                    "bottomwear": ["jeans", "trousers"],
                    "footwear": ["footwear"],
                    "optional": ["bags", "glasses"],
                    "accessory": ["accessories", "watches"]
                }
            }
        ],
        "Vacation": [
            {
                "slots": ["topwear", "bottomwear", "footwear", "optional", "accessory"],
                "categories": {
                    "topwear": ["dresses", "t-shirts", "shirts"],
                    "bottomwear": ["jeans", "trousers"],
                    "footwear": ["footwear"],
                    "optional": ["bags", "glasses"],
                    "accessory": ["accessories", "watches"]
                }
            }
        ],
        "Office": [
            {
                "slots": ["topwear", "bottomwear", "footwear", "optional", "accessory"],
                "categories": {
                    "topwear": ["shirts", "blazers"],
                    "bottomwear": ["trousers"],
                    "footwear": ["footwear"],
                    "optional": ["bags"],
                    "accessory": ["watches", "accessories"]
                }
            }
        ],
        "Party": [
            {
                "slots": ["topwear", "footwear", "optional", "accessory"],
                "categories": {
                    "topwear": ["dresses"],
                    "footwear": ["footwear"],
                    "optional": ["bags"],
                    "accessory": ["accessories", "watches"]
                }
            },
            {
                "slots": ["topwear", "bottomwear", "footwear", "optional", "accessory"],
                "categories": {
                    "topwear": ["shirts", "t-shirts", "blazers"],
                    "bottomwear": ["jeans", "trousers"],
                    "footwear": ["footwear"],
                    "optional": ["bags"],
                    "accessory": ["accessories", "watches"]
                }
            }
        ],
        "Festival": [
            {
                "slots": ["topwear", "bottomwear", "footwear", "accessory", "optional"],
                "categories": {
                    "topwear": ["sarees", "kurtas"],
                    "bottomwear": ["trousers", "jeans"],
                    "footwear": ["footwear"],
                    "accessory": ["accessories"],
                    "optional": ["bags"]
                }
            }
        ],
        "Wedding Guest": [
            {
                "slots": ["topwear", "bottomwear", "footwear", "accessory", "optional"],
                "categories": {
                    "topwear": ["sarees", "dresses", "kurtas"],
                    "bottomwear": ["trousers"],
                    "footwear": ["footwear"],
                    "accessory": ["accessories"],
                    "optional": ["bags", "perfumes"]
                }
            }
        ]
    }
}
