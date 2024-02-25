from flask import Flask, render_template,request
import pickle

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html', data=[1,2,3,4])


@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/profile/<int:id>')
def profile(id):
    return ' Your requested user with id '+ str(id)

@app.route('/predict',methods=['POST'])
def submit():
    if request.method == "POST":
        FS= int(request.form["FS"])
        FU = int(request.form["FU"])
        with open('my_model', 'rb') as file:
            model= pickle.load(file)
        print(model.predict([[FS<FU]]))
        return 'submitted successfully'
    else:
        return "something went wrong"

if __name__=="__main__":
    app.run(debug=True)