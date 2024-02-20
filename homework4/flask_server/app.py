from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", user_name="Alex")

@app.route("/users/<user_name>")
def user(user_name):
    return render_template("index.html", user_name=user_name)

@app.route("/contact", methods=["GET", "POST"])
def contact():

    if request.method == "POST":
        username = request.form.get("username")
        email = request.form.get("email")
        message = request.form.get("message")

        print(username, email, message)
        return render_template("thanks.html", user_name=username)
    else:
        return render_template("contact.html")

if __name__ == "__main__":
    app.run()