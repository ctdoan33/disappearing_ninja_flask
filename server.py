from flask import Flask, render_template, request, redirect
app = Flask(__name__)
@app.route("/")
def noninja():
    return render_template("index.html")
@app.route("/ninja")
def ninjas():
    src="../static/tmnt.png"
    return render_template("ninjas.html", source=src)
@app.route("/ninja/<ninja_color>")
def ninja(ninja_color):
    if ninja_color=="blue":
        src="../static/leonardo.jpg"
    elif ninja_color=="orange":
        src="../static/michelangelo.jpg"
    elif ninja_color=="red":
        src="../static/raphael.jpg"
    elif ninja_color=="purple":
        src="../static/donatello.jpg"
    else:
        src="../static/notapril.jpg"
    return render_template("ninjas.html", source=src)
app.run(debug=True)