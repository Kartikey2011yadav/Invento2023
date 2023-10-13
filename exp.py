from flask import Flask, render_template, redirect, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def test():
    if (request.method == "POST"):
        auth = request.form["author"]
        print(auth)
        return render_template("input.html")
    else:
        return render_template("input.html")


if (__name__ == "__main__"):
    app.run(debug=True)
