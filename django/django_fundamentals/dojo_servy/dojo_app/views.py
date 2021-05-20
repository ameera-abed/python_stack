from django.shortcuts import render


def root(request):
    return render(request,"index.html")

def result(request):
    if request.method == "POST":
        username=request.POST["username"]
        dojo_location=request.POST["dojo"]     
        comments=request.POST["comments"]
        language= request.POST["fav-lang"]  
        context={
            "username": username,
            "dojo_location":dojo_location,           
            "comments":comments,
             "language" :language  
        }
        return render(request,"result.html",context)
