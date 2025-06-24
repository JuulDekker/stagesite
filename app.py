from flask import Flask, render_template, request

app = Flask(__name__)

companies = [
    {
        "name": "Flynth",
        "type": "Afstudeerstage",
        "logo": "abc.png",  # Place this image in static/logos/
        "pay": "€800/month",
        "period": "N.A.",
        "location": "Zierikzee",
        "site": ""
    },
    {
        "name": "Baker Tilly",
        "type": "Afstudeerstage",
        "logo": "sageinnovations.png",
        "department": "Audit",
        "pay": "€725-€850/month",
        "period": "N.A.",
        "location": "Goes",
        "site": "https://www.werkenbijbakertilly.nl/vacatures/afstudeerstage-audit-goes-2055684",
    },
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
    {
        "name": "TechWave",
        "logo": "techwave.png",
        "pay": "€600/month",
        "period": "Mar 2026 - Aug 2026",
        "location": "Utrecht"
    },
    # It is very easy to add more companies if needed, copy the code above and change the information.
]

@app.route("/", methods=["GET"])
def home():
    query = request.args.get("q", "").lower()
    if query:
        filtered = [c for c in companies if query in c["name"].lower()]
    else:
        filtered = companies
    return render_template("index.html", companies=filtered, query=query)