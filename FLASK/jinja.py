from flask import Flask,render_template,request,redirect,url_for


app = Flask(__name__)

@app.route("/")
def welcome():
    return "hello world my name is pabitra biswas "
@app.route("/about")
def about():
    return render_template('about.html')

## variable rule 
'''
{{ }}  expression to priint output in html
{%...... %} conditions , for loops 
{# ..... # } this is for singlre line comments 
'''


@app.route("/success/<int:score>")
def success(score):
    res =""
    if score>=55:
        res = 'PASSED'
    else :
        res = 'FAILED'
    return render_template('result.html',results=res)
    

@app.route("/successres/<int:score>")
def successres(score):
    res =""
    if score>=55:
        res = 'PASSED'
    else :
        res = 'FAILED'
    exp ={'score':score,'res':res}
    return render_template('result1.html',results=exp)

if __name__=="__main__":
    app.run(debug=True)
    