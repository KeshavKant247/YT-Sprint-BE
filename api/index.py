import sys
import os

# Add the backend directory to the path
backend_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'backend')
sys.path.insert(0, backend_path)

# Import the Flask app
from app import app

# Vercel expects the app to be accessible
# The app variable is what Vercel will use
app = app
