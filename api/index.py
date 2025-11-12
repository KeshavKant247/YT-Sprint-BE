import sys
import os

# Add the backend directory to the path
backend_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'backend'))
if backend_path not in sys.path:
    sys.path.insert(0, backend_path)

try:
    # Import the Flask app
    from app import app as application

    # Vercel serverless handler
    app = application
except Exception as e:
    # Create a minimal error handler if import fails
    from flask import Flask, jsonify
    app = Flask(__name__)

    @app.route('/')
    def error():
        return jsonify({
            'error': 'Failed to load application',
            'details': str(e),
            'backend_path': backend_path,
            'sys_path': sys.path
        }), 500
