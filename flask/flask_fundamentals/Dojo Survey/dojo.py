from flask import Flask ,render_template,request
app=Flask(__name__)

@ app.route("/")
def index():
    return render_template("index.html")

@ app.route("/result",methods=["post"])
def result():
    name=request.form["username"]
    dojo_loction=request.form["dojo"]
    fav_lang=request.form["fav-lang"]
    comments=request.form["comments"]
    return render_template("result.html",name=name,dojo_loction=dojo_loction,fav_lang=fav_lang,comments=comments)





if __name__=="__main__":     
    app.run(debug=True) 