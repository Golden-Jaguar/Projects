from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html")


@app.route("/result", methods=['POST', 'GET'])
def result():
    output = request.form.to_dict()
    name = output["name"]
    return render_template("index.html", name = name)


if __name__ == '__main__':
    app.run(debug=True, port=5001)

# from flask import render_template
#
# @app.route('/hello/')
# @app.route('/hello/<name>')
# def hello(name=None):
#     return render_template('index.html', name=name)
