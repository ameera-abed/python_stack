from django.shortcuts import redirect, render
import random 	                # import the random module
 

# Create your views here.
def root(request):
    request.session['my-q'] = random.randint(1, 100)
    request.session['show_submit_btn']=True
    show_submit_btn=request.session['show_submit_btn']
 
    
    context={
        "quess":request.session['my-q'] ,
       "show_submit_btn":show_submit_btn
        
        }
    return render(request,"index.html",context)

def result(request): 
    request.session['your_q'] = int(request.POST['user_input'])
    request.session['show_submit_btn']=False
    show_submit_btn=request.session['show_submit_btn']
    request.session["show_try_btn"]=False
    try_btn= request.session["show_try_btn"]
    
    s=0 
    if request.session['my-q']==request.session['your_q']:
        s=1   
    elif request.session['my-q'] > request.session['your_q']:
        try_btn=True
        s=2 
    else:
        try_btn=True
        s=3 
    context={
        "status":s,
        "your_quess":request.session['your_q'],
        "show_submit_btn":show_submit_btn,
        "try_btn":try_btn
        
        
        }
    return render(request,"index.html",context)

def reset(request):
    return redirect("/") 


def back(request):
    return redirect("/")       
    