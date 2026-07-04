# services/recommender.py
from data.products import PRODUCTS
from data.style_rules import get_style_info, generate_why_it_suits
import urllib.parse

def score_product(product, preferences):
    score = 0
    
    # +5 Gender Match (or Unisex)
    if preferences["gender"] in product["gender"] or "Unisex" in product["gender"]:
        score += 5
    else:
        return -1 # Exclude mismatched gender
        
    # +5 Occasion Match
    if preferences["occasion"] in product["occasions"]:
        score += 5
        
    # +3 Skin Tone Match
    if preferences["skin_tone"] in product["skin_tones"]:
        score += 3
        
    # +3 Body Shape Match
    if preferences["body_shape"] in product["body_shapes"]:
        score += 3
        
    return score

def get_recommendation(preferences):
    from data.style_rules import OUTFIT_TEMPLATES
    
    # Parse budget
    try:
        max_budget = int(preferences.get("budget", 5000))
    except:
        max_budget = 5000
        
    gender = "Women" if "Women" in preferences.get("gender", "") else "Men"
    occasion = preferences.get("occasion", "Casual")
    
    templates = OUTFIT_TEMPLATES.get(gender, {}).get(occasion, OUTFIT_TEMPLATES["Men"]["Casual"])
    
    scored_products = []
    for p in PRODUCTS:
        s = score_product(p, preferences)
        if s > 0:
            scored_products.append({"product": p, "score": s})
            
    # Sort by score
    scored_products.sort(key=lambda x: x["score"], reverse=True)
    
    best_look = []
    best_look_price = 0
    best_template = None
    missing_slots = []
    filled_slots = []
    
    for template in templates:
        current_look = []
        current_price = 0
        current_missing = []
        current_filled = []
        skip_bottomwear = False
        
        for slot in template["slots"]:
            if slot == "bottomwear" and skip_bottomwear:
                continue
                
            allowed_categories = template["categories"].get(slot, [])
            best_for_slot = None
            
            for item in scored_products:
                p = item["product"]
                if p["category"] in allowed_categories and p not in current_look:
                    if current_price + p["price"] <= max_budget:
                        best_for_slot = p
                        break
            
            if best_for_slot:
                current_look.append(best_for_slot)
                current_price += best_for_slot["price"]
                current_filled.append(slot)
                if slot == "topwear" and best_for_slot["category"] in ["dresses", "sarees"]:
                    skip_bottomwear = True
            else:
                current_missing.append(slot)
                
        if not best_template or len(current_look) > len(best_look):
            best_look = current_look
            best_look_price = current_price
            best_template = template
            missing_slots = current_missing
            filled_slots = current_filled
            
        core_missing = [s for s in current_missing if s in ["topwear", "bottomwear", "footwear"]]
        if not core_missing:
            break

    budget_status = ""
    core_items = [s for s in filled_slots if s in ["topwear", "bottomwear", "footwear"]]
    expected_core = [s for s in best_template["slots"] if s in ["topwear", "bottomwear", "footwear"]]
    if "bottomwear" in expected_core and "bottomwear" not in filled_slots and "bottomwear" not in missing_slots:
        expected_core.remove("bottomwear")
        
    is_starter_look = False
    
    if len(core_items) < len(expected_core):
        is_starter_look = True
        missing_names = ", ".join(missing_slots)
        if len(best_look) == 0:
             budget_status = f"Your budget of ₹{max_budget} is too low. We couldn't find pieces for a look."
        else:
             budget_status = f"Build Your Look in Stages! Due to your budget, we couldn't include {missing_names}. We recommend starting with these pieces."
    elif max_budget - best_look_price > 2000:
        budget_status = f"Great news! We built a full look and you still have ₹{max_budget - best_look_price} left in your budget."
    else:
        budget_status = "We built a complete look that perfectly maximizes your budget!"
        
    for sp in best_look:
        q = urllib.parse.quote(sp["search_query"])
        sp["amazon_link"] = f"https://www.amazon.in/s?k={q}"
        sp["flipkart_link"] = f"https://www.flipkart.com/search?q={q}"
        
    style_info = get_style_info(preferences["gender"], preferences["occasion"])
    reasons = generate_why_it_suits(
        preferences["gender"], 
        preferences["skin_tone"], 
        preferences["body_shape"], 
        preferences["occasion"]
    )
    
    if len(best_look) > 0:
        if is_starter_look:
            lara_msg = f"I've curated a Starter {style_info['style']} look just for you."
        else:
            lara_msg = f"I've curated a complete {style_info['style']} look just for you."
    else:
        lara_msg = "I couldn't find a full outfit in this range, but try adjusting your budget!"
        
    from services.gemini_service import generate_lara_message
    
    rec_data = {
        "recommended_style": style_info["style"],
        "color_palette": style_info["palette"],
        "why_this_suits_you": reasons,
        "total_price": best_look_price,
        "budget_status": budget_status,
        "local_lara_message": lara_msg,
        "products": best_look
    }
    
    gemini_msg = generate_lara_message(rec_data)
    is_gemini_message = False
    
    if gemini_msg:
        lara_msg = gemini_msg
        is_gemini_message = True
        
    rec_data["local_lara_message"] = lara_msg
    rec_data["is_gemini_message"] = is_gemini_message
    
    return rec_data
