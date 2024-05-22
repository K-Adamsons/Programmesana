from flask import Flask, render_template, request 
from dati import dabut_rindinas, pierakstit_klat

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/tests")
def te():
    return render_template("tests.html")

@app.route("/saraksts")
def saraksts():
    saraksts = []
    bildes = ["https://g.delphi.lv//images/pix/not-personality-45774342.jpg"]
    kopejais_saraksts = []
    faila_rindas = dabut_rindinas()
    for rinda in faila_rindas:
        elements = rinda.split(", ")
        kopejais_saraksts.append(elements)
    return render_template("saraksts.html", vardi = saraksts, bildes = bildes)

@app.route("/info", methods=['POST', 'GET'])
def info():
     if request.method == "POST":
        nosaukums = request.form["nosaukums"]
        adrese = request.form[""]
        rinda = nosaukums + "," + adrese 
        pierakstit_klat(rinda)
     return render_template("Info.html")


if __name__ == '__main__':
      app.run(port = 5000)