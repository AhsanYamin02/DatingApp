from flask import Flask, render_template, request

app = Flask(__name__)

# Sample user data
users = [
    {"name": "Alice", "age": 25, "interests": ["hiking", "reading"]},
    {"name": "Bob", "age": 30, "interests": ["cooking", "movies"]},
    {"name": "Charlie", "age": 28, "interests": ["traveling", "photography"]},
]

@app.route("/")
def index():
    return render_template("index.html", users=users)

@app.route("/profile/<name>")
def profile(name):
    user = next((user for user in users if user["name"] == name), None)
    if user:
        return render_template("profile.html", user=user)
    else:
        return "User not found", 404

if __name__ == "__main__":
    app.run(debug=True)
