from django.shortcuts import redirect, render

# Create your views here.
def root(request):
    num_visits = request.session.get('num_visits', 1)
    request.session['num_visits'] = num_visits + 1
    context={
        "num_visits":num_visits,
    }
    return render(request,"index.html",context)

def distroy(request):
    del request.session['num_visits'] 
    return redirect("/")