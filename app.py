from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("first_page.html")

@app.route("/second")
def second():
    return render_template("second_page.html")
    
if __name__ == "__main__":
    app.run(debug=True)
