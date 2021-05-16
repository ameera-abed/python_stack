from flask import Flask ,render_template
app = Flask(__name__) 
@ app.route("/")
def checkbord_1():
    return  render_template("index.html",choice="1")

@ app.route("/4")
def checkbord_2():
    return  render_template("index.html",choice="2")

@ app.route("/<int:x>/<int:y>")
def checkbord_3(x,y):
  
    return  render_template("index.html",choice="3",x=x,y=y)




if __name__=="__main__":     
    app.run(debug=True) 