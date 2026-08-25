from flask import Flask, jsonify, request

app = Flask(__name__)

# SIMPLE FLASK APPLICATION 

health = "App is running"

votes = {}

@app.route("/")
def new_app():
    return "Welcome to the App"

@app.route("/health")
def health_check():
    return health


# VOTING APPLICATION

votes = {}

@app.route("/vote/<name>")
def vote(name):
    if name in votes:
        votes[name] = votes[name] + 1
        return f"{name} now has {votes[name]} vote(s)."
    else:
        votes[name] = 1
        return f"{name} now has {votes[name]} vote(s)."

@app.route("/result")
def result():
    return jsonify(votes)
