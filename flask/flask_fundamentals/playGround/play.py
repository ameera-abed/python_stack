from flask import Flask ,render_template
app = Flask(__name__) 
@ app.route("/play")
def play_level_1():
    return  render_template("index.html")

@ app.route("/play/<int:x>")
def play_level_2(x):
    return  render_template("index2.html",times=x)

@ app.route("/play/<int:x>/<color>")
def play_level_3(x,color):
    return  render_template("index3.html",times=x,c=color) 



if __name__=="__main__":     
    app.run(debug=True) 