
from flask import Flask, render_template, request, flash, redirect, url_for
from dotenv import load_dotenv
from data.demo_data import TRENDING_COLLECTIONS
from services.validator import validate_preferences
from services.recommender import get_recommendation

load_dotenv()

app = Flask(__name__)
app.secret_key = 'super_secret_key_for_flash'

@app.route('/')
def home():
    return render_template('index.html', collections=TRENDING_COLLECTIONS)

@app.route('/recommend', methods=['POST'])
def recommend():
    form_data = request.form
    errors = validate_preferences(form_data)
    
    if errors:
        for error in errors:
            flash(error, 'error')
        return redirect(url_for('home'))
        
    recommendation = get_recommendation(form_data)
    return render_template('results.html', rec=recommendation)

@app.route('/results')
def results():
    # Fallback preview
    dummy_prefs = {
        "gender": "Women",
        "skin_tone": "Medium",
        "body_shape": "Hourglass",
        "occasion": "Party",
        "budget": "5000"
    }
    recommendation = get_recommendation(dummy_prefs)
    return render_template('results.html', rec=recommendation)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
