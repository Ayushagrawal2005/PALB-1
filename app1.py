from flask import Flask,render_template
app=Flask(__name__)

@app.route("/")
def welcome():
    return "<html><body><h1>Welcome to Flask</h1></body></html>"

@app.route("/hello")
def hello():
    return render_template("hello.html")


@app.route('/success/<int:score>')
def success(score):
    res=""
    if score>=50:
        res="passed"
    else:
        res="failed"
    return render_template("result1.html",result=res)

if __name__=="__main__":
    app.run(debug=True)


