from flask import Flask, render_template, request

app = Flask(__name__)

companies = [
    {
        "name": "Flynth",
        "type": "Afstudeerstage",
        "logo": "greentech.png",  # Place this image in static/logos/
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
        "site": '<a href="https://www.werkenbijbakertilly.nl/vacatures/afstudeerstage-audit-goes-2055684">Baker Tilly</a>',
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
    {
        "name": "EcoBuild Corp",
        "logo": "ecobuild.png",
        "pay": "€550/month",
        "period": "Apr 2026 - Sep 2026",
        "location": "The Hague"
    },
    {
        "name": "DataSphere Analytics",
        "logo": "datasphere.png",
        "pay": "€700/month",
        "period": "May 2026 - Oct 2026",
        "location": "Eindhoven"
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