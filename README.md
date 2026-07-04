
# LARA – AI Fashion Advisor

**College Mini Project**

## Project Overview
LARA (Local AI Recommendation Advisor) is an intelligent, web-based virtual stylist. Finding the right outfit for a specific occasion, body shape, and budget is often a time-consuming and overwhelming process for consumers. LARA solves this by combining a robust local recommendation engine with an optional Generative AI layer to curate highly personalized, complete outfits tailored to individual user preferences.

## Problem Statement
E-commerce platforms often flood users with endless scrolling and disconnected product listings. Users struggle to visualize complete outfits or find items that suit their specific body shape, skin tone, and budget. There is a clear need for a unified, intelligent system that acts as a personal stylist, curating complete, ready-to-wear looks.

## Key Features
- **Intelligent Local Recommendation Engine**: Curates complete outfits (topwear, bottomwear, footwear, accessories) based on 100+ style rules encompassing Gender, Skin Tone, Body Shape, Occasion, and Budget.
- **Dynamic Image Integration**: Uses direct integration with Unsplash to pull high-quality, relevant fashion imagery seamlessly.
- **Client-Side "Save This Look"**: A privacy-first bookmarking feature leveraging browser `localStorage` to save favorite curated looks instantly without requiring user accounts or databases.
- **Gemini AI Stylist Integration**: Connects with Google's Gemini 1.5 Flash API to generate friendly, contextual explanations of *why* the outfit works.
- **Resilient Fallback Architecture**: Automatically degrades gracefully to localized text processing if the Gemini API key is missing or the network drops.
- **Responsive Premium UI**: Built with Tailwind CSS, featuring glassmorphism elements, subtle micro-animations, and dynamic empty states.

## Technology Stack
- **Frontend**: HTML5, Vanilla JavaScript, Tailwind CSS (via CDN)
- **Backend**: Python 3.x, Flask
- **AI Integration**: `google-generativeai` SDK
- **Data Storage**: Client-side `localStorage` (No SQL/NoSQL DB required)
- **Environment Management**: `python-dotenv`

## Folder Structure
```text
lara-ai-fashion-advisor/
├── app.py                  # Main Flask application entry point
├── requirements.txt        # Python dependencies
├── .env.example            # Template for environment variables
├── README.md               # Project documentation
├── TESTING.md              # Test cases and expected behavior
├── data/                   
│   ├── products.py         # Curated local dataset of 40+ fashion items
│   └── style_rules.py      # Hardcoded rules for body shape/skin tone matching
├── services/               
│   ├── recommender.py      # Core engine building complete outfits
│   └── gemini_service.py   # Wrapper for Google Gemini API integration
├── static/                 
│   ├── css/style.css       # Custom animations and variables
│   ├── js/main.js          # LocalStorage and UI interactions
│   └── images/             # Local fallback images and avatars
├── templates/              
│   ├── base.html           # Master layout and navbar
│   ├── index.html          # Homepage and input form
│   └── results.html        # Curated look and shop buttons
└── reference/              # Original design exports (Stitch UI)
```

## Installation & Local Run

### Prerequisites
- Python 3.10+ installed on your system.

### Steps
1. **Clone the repository**:
   ```bash
   git clone <your-repo-url>
   cd "lara AI 2"
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   # On Windows:
   .\venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up Environment Variables**:
   Copy the example file to create your local config.
   ```bash
   cp .env.example .env
   ```
   *(Optional)* Open `.env` and add your Google Gemini API key to enable AI messages. If you leave it blank, LARA will use a built-in fallback message automatically.

5. **Run the Flask App**:
   ```bash
   python app.py
   ```
   Open your browser and navigate to: `http://127.0.0.1:5000/`

## Recommendation Flow Architecture
1. **Input**: User submits a form via POST to `/recommend`.
2. **Filtering**: `recommender.py` filters the local `products.py` database based on Gender, Occasion, and Budget.
3. **Scoring**: Remaining products are scored heavily on Skin Tone and Body Shape matches using `style_rules.py`.
4. **Assembly**: The engine prioritizes a "complete look" template (e.g., Top + Bottom + Shoes) ensuring the combined total stays under the selected budget limit.
5. **Enrichment**: The final outfit data is passed to `gemini_service.py`. If configured, Gemini returns a cohesive 90-word summary of the look.
6. **Output**: The data is rendered via Jinja2 into `results.html`.

## Limitations
- **Static Dataset**: Currently relies on a local Python dictionary of 40 curated items rather than a live external product database.
- **No User Accounts**: Uses `localStorage`, meaning saved looks do not persist across different devices or browsers.
- **Simulated Cart**: The "Search on Amazon/Flipkart" buttons run keyword searches rather than linking to exact, live SKUs.

## Future Scope
- **Database Integration**: Migrate local product dictionaries to PostgreSQL/MongoDB and implement live web scraping for accurate prices.
- **User Authentication**: Implement JWT or OAuth for cross-device saved look persistence.
- **Computer Vision**: Allow users to upload a photo to automatically detect skin tone and body shape.
- **Virtual Try-On**: Integrate an AI diffusion model to overlay recommended outfits onto user-uploaded photos.
