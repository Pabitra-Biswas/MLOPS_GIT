from flask import Flask,render_template


app = Flask(__name__)

@app.route("/")
def welcome():
    return "hello world my name is pabitra biswas "
@app.route("/about")
def about():
    return render_template('about.html')



if __name__=="__main__":
    app.run(debug=True)
    