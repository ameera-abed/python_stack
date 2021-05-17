from flask import Flask ,render_template,redirect,session
from flask.globals import request
app=Flask(__name__)
app.secret_key="jkbedewugfuiew"
count=0
@app.route("/")
def counter():
    global count
    count=count+1
    session["count"]=count
    return render_template("index.html")

@ app.route("/destroy_session")
def destroy_session():
    session.clear()
    global count
    count=0
    return redirect("/")
    









if __name__=="__main__":     
    app.run(debug=True) 