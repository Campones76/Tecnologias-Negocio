from flask import Flask
from backend.views.home import home_bp

app = Flask(__name__, template_folder='../frontend/templates')

# Register Blueprints
app.register_blueprint(home_bp)

if __name__ == '__main__':
    app.run(debug=True)