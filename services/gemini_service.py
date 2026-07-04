import os
import google.generativeai as genai
import json

def generate_lara_message(rec_data):
    """
    Generates a personalized stylist message from LARA using Gemini API.
    Uses strict rules and fallbacks if API is unavailable or disabled.
    """
    use_gemini = os.getenv("USE_GEMINI", "False").lower() == "true"
    api_key = os.getenv("GEMINI_API_KEY")
    
    if not use_gemini or not api_key or api_key == "invalid_key":
        return None
        
    try:
        genai.configure(api_key=api_key)
        # Use gemini-1.5-flash for fast text generation
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        prompt = f"""You are LARA, an AI Fashion Advisor. Write a friendly, personalized stylist message to the user based on their selections.

USER DATA:
- Recommended Style: {rec_data.get('recommended_style')}
- Selected Products: {', '.join([p['name'] for p in rec_data.get('products', [])])}
- Color Palette: {', '.join(rec_data.get('color_palette', []))}
- Budget Status: {rec_data.get('budget_status')}
- Local Reasons: {' '.join(rec_data.get('why_this_suits_you', []))}

STRICT RULES:
1. Do not invent products, prices, ratings, discounts, links, availability, brands, or claims not present in the provided data.
2. Keep the message under 90 words.
3. Be friendly and conversational, acting as a personal stylist.
4. Do not mention that you are an AI. Just be LARA.
5. Acknowledge the budget status gracefully.
"""

        response = model.generate_content(prompt)
        
        if response and response.text:
            return response.text.strip()
            
    except Exception as e:
        # Silently fail and fallback to local message
        print(f"Gemini API Error: {e}")
        pass
        
    return None
