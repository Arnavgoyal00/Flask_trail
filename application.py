from flask import Flask,render_template,request
import pickle
app = Flask(__name__)

@app.route("/", methods =['GET','POST'])
def home():
    return "Arnav Here"

if __name__ == "_main_":
    app.run(debug=True)
