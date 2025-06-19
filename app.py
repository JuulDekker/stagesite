from flask import Flask, render_template, request

app = Flask(__name__)

companies = [
    {
        "name": "GreenTech Solutions",
        "logo": "greentech.png",  # Place this image in static/logos/
        "pay": "€500/month",
        "period": "Feb 2026 - Jul 2026",
        "location": "Amsterdam"
    },
    {
        "name": "Sage Innovations",
        "logo": "sageinnovations.png",
        "pay": "€400/month",
        "period": "Jan 2026 - Jun 2026",
        "location": "Rotterdam"
    },
    # Add more companies as needed
]

@app.route("/", methods=["GET"])
def home():
    query = request.args.get("q", "").lower()
    if query:
        filtered = [c for c in companies if query in c["name"].lower()]
    else:
        filtered = companies
    return render_template("index.html", companies=filtered, query=query)