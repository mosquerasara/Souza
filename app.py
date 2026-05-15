from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def inicio():
    return render_template("inicio.html")

@app.route("/reservas")
def reservas():
    return render_template("reserva.html")

@app.route("/menu")
def menu():
    return render_template("menu.html")

@app.route("/contacto")
def contacto():
    return render_template("contacto.html")

@app.route("/nosotros")
def nosotros():
    return render_template("nosotros.html")

@app.route("/mar")
def mar():
    return render_template("mar.html")

@app.route("/tierra")
def tierra():
    return render_template("tierra.html")

@app.route("/especialidades")
def especialidades():
    return render_template("especialidades.html")

if __name__ == "__main__":
    app.run(debug=True)