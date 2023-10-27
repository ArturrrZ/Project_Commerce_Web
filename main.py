from flask import Flask, request,render_template,redirect

from flask_bootstrap import Bootstrap5
app=Flask(__name__)

Bootstrap5(app)

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/check_father")
def check():
    return render_template("father_template.html")

@app.route("/items")
def display_items():
    return render_template("items.html")

















if __name__ == "__main__":
    app.run(debug=True)


