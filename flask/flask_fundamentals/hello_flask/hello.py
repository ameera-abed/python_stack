from flask import Flask 
app = Flask(__name__) 
@ app.route("/")
def hello():
    return "Hello World!"

@app.route("/dojo")
def dojo():
    return "Dojo!"

@app.route("/say/<name>")
def say(name):
    return f"hi {name}"

@app.route("/repeat/<int:num>/hello")
def repeate(num): 
    return f"hello  " *num 

if __name__=="__main__":     
    app.run(debug=True) 