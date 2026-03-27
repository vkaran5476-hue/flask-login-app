from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def login():
    return render_template("index.html")

@app.route("/submit", methods=["POST"])
def submit():
    username = request.form.get("username")
    password = request.form.get("password")
    age = request.form.get("age")
    gender = request.form.get("gender")

    if username == "karan12" and password == "pass" and age == "21" and gender == "male":
        return render_template("welcome.html", name=username)
    else:
        return "Invalid details"

if __name__ == "__main__":
    app.run(debug=True)