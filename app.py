from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello, Azure App Service with Python Flask!"

if __name__ == "__main__":
    # Run the app in production mode (debug=False)
    app.run(host='0.0.0.0', port=5000, debug=False)  # Set debug=False for production
