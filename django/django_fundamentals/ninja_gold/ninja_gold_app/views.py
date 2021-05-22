from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
import random
from datetime import datetime

# Create your views here.

def process_money(request):
    if "gold" in request.session:
        pass
    else:
        request.session['gold'] = 0
    if "activities" not in request.session:
        request.session['activities'] = []
    return render(request, 'index.html')



def process_gold(request):
   
    farm = random.randint(10, 20) 
    cave = random.randint(5, 10)
    house = random.randint(2, 5)
    casino = random.randint(0, 50)

    now_formatted = datetime.now().strftime("%m/%d/%Y %I:%M%p") 

    if request.POST['building']=='farm':
        request.session['gold']+= farm
        activities=f"You earn {farm} pieces of gold from the Farm! ({now_formatted})"
        request.session["activities"].append(activities)
        return redirect('/')

    if request.POST['building']=='cave':
        request.session['gold']+= cave
        activities=f"You earn {cave} pieces of gold from the Cave! ({now_formatted})"
        request.session["activities"].append(activities)
        return redirect('/')

    if request.POST['building']=='house':
        request.session['gold']+= house
        activities=f"You earn {house} pieces of gold from the House! ({now_formatted})"
        request.session["activities"].append(activities)
        return redirect('/')

    if request.POST['building'] == 'casino':
        if casino > 25: 
            request.session['gold'] -= casino
            activities= f"Entered a << Casino >> and lost {casino} golds!! Oops!) ({now_formatted})"
            request.session["lose"]="lose"
            request.session["activities"].append(activities) 
        else:
            request.session['gold'] += casino
            activities=f"You earn {casino} pieces of gold from the Casino ({now_formatted})"
            request.session["activities"].append(activities) 
                    
    return redirect('/')            

