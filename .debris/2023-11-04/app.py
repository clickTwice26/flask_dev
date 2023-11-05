from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")
    # return 'Welcome to index'
@app.route('/products')
def products():
    return 'Welcome to products'
@app.route('/contact')
def contact():
    return 'Welcome to contact page'


if __name__ == "__main__":
    app.run(debug=True, port=8000)