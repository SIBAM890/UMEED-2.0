from flask import Flask
from .extensions import socketio, db
import google.generativeai as genai
import os
from dotenv import load_dotenv # --- NEW ---

# --- NEW: Load environment variables from .env file ---
load_dotenv()

def create_app():
    app = Flask(__name__)
    
    # --- API KEY CONFIGURATION (NOW SECURE) ---
    # We now read the key from the .env file
    GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")
    
    if not GEMINI_API_KEY:
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print("ERROR: GEMINI_API_KEY not found in environment.")
        print("Please create a .env file and add it.")
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    
    # --- REMOVED OLLAMA CONFIG ---
    
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///umeed.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # --- Configure Gemini API ---
    try:
        genai.configure(api_key=GEMINI_API_KEY)
        print("Gemini API configured successfully.")
    except Exception as e:
        print(f"!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print(f"ERROR: Failed to configure Gemini API: {e}")
        print(f"Please check your API key.")
        print(f"!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

    # Initialize extensions
    socketio.init_app(app)
    db.init_app(app)

    # Register blueprints
    from .routes import main as main_blueprint
    app.register_blueprint(main_blueprint)
    
    # Import events to register handlers
    from . import events
    
    # Import models and create tables
    from . import models
    from .routes import seed_data
    
    with app.app_context():
        db.create_all()
        seed_data()

    return app