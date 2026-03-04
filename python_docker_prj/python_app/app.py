from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # Simple data dictionary for the frontend
    user_data = {
        "name": "Python Developer",
        "status": "Running",
        "year": 2026
    }
    return render_template('index.html', data=user_data)

if __name__ == '__main__':
    # Hardcoded to listen on all interfaces (0.0.0.0) 
    # so it works both in Ubuntu and inside Docker.
    app.run(host='0.0.0.0', port=5000)
