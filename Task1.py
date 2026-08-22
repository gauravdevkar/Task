from flask import Flask, jsonify, request

app = Flask(__name__)

health = "App is running"

@app.route("/")
def new_app():
    return "Welcome to the App"

@app.route("/health")
def health_check():
    return health

