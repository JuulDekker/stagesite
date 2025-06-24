from flask import Flask, render_template, request

app = Flask(__name__)

companies = [
    {
        "name": "Flynth",
        "type": "Afstudeerstage",
        "logo": "flynth.jpg",
        "pay": "€800/month",
        "period": "Insufficient information",
        "location": "Zierikzee",
        "site": "",
        "department": "Insufficient information"
    },
    {
        "name": "Baker Tilly",
        "type": "Afstudeerstage",
        "logo": "bakertilly.jpg",
        "department": "Audit",
        "pay": "€725-€850/month",
        "period": "Insufficient information",
        "location": "Goes",
        "site": "https://www.werkenbijbakertilly.nl/vacatures/afstudeerstage-audit-goes-2055684"
    },
    {
        "name": "Schipper Accountants",
        "type": "Insufficient information",
        "logo": "schipper.jpg",
        "pay": "Insufficient information",
        "period": "Insufficient information",
        "location": "Zeeland",
        "site": "https://www.schipperaccountants.nl/werken-bij/vacature/stage-sollicitatie/",
        "department": "Accountancy, Audit or Tax"
    },
    {
        "name": "WEA Accountants, Adviseurs",
        "type": "Insufficient information",
        "logo": "wea.jpg",
        "pay": "Insufficient information",
        "period": "Insufficient information",
        "location": "Hulst, Middelburg, Oost-Souburg, Vlissingen",
        "site": "https://werkenbij.wea.nl/vacature/vacature-stagiair-hbo-aa-be-en-fc-wea-zeeland/",
        "department": "Insufficient information"
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