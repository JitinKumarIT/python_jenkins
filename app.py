from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Jenkins CI/CD Pipeline!"

if __name__ == "__main__":
    # Tell Bandit to ignore the B104 warning for this specific line
    app.run(host="0.0.0.0", port=5000)  # nosec B104
