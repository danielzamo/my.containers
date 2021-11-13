from flask import Flask, render_template

app = Flask(__name__)

@app.route("/beta")
def beta():
    return render_template("beta.html")

@app.route("/")
def index():
    num = [1, 2, 3, 4, 5, 6, 7]
    return render_template("index.html", num=num)

@app.route("/contacto")
def contacto():
    path = "Contacto"
    return render_template("contacto.html", path=path)


if __name__ == '__main__':    
    app.run(port=5000, debug=True, host='0.0.0.0')
