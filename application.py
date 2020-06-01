from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
@app.route("/home")
def index():
    return render_template("index.html")

@app.route("/services")
def services():
    return render_template("services.html", title='Services')

@app.route("/about")
def about():
    return render_template("aboutme.html", title='About')

@app.route("/contact")
def contact():
    return render_template("contactme.html", title='Contact')


if __name__ == '__main__':
    app.run(debug=True)
