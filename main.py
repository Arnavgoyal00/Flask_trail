from flask import Flask,render_template,request
import pickle
app = Flask(__name__)

@app.route("/", methods =['GET','POST'])
def home():
    if request.method =='POST':
        model = pickle.load(open('model.pkl','rb'))
        user_input=request.form.get('size')
        print(user_input)
        user_input=float(user_input)
        pred = model.predict([[user_input]])
        print(pred)
    return render_template('index.html',value=pred)

if __name__ == "_main_":
    app.run(debug=True)