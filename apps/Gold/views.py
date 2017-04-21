from django.shortcuts import render, HttpResponse, redirect
import random

def index(request):
    if 'gold' not in request.session:
        request.session['gold'] = 0
    if 'move' not in request.session:
        request.session['move'] = []


    return render(request, 'Gold/index.html')

def execute(request):
    print request.POST['location']
    if request.POST['location'] == 'farm':
        gold = random.randint(10,20)
    elif request.POST['location'] == 'cave':
        gold = random.randint(5,10)
    elif request.POST['location'] == 'house':
        gold = random.randint(2,5)
    else:
        gold = random.randint(-50,50)
    request.session['gold'] += gold

    messageObj = {}

    if gold>0:
        action='Gained'
        messageObj['color'] = 'green'

    else:
        action='Lost'
        messageObj['color'] = 'red'

    message = "{} {} gold from {}".format(action, abs(gold), request.POST['location'])
    messageObj['message'] = message
    request.session['move'].insert(0, messageObj)
    print messageObj['color']
    print messageObj['message']
    return redirect('/')

def reset(request):
    request.session.pop('gold', None)
    request.session['move'] = []
    return redirect("/")
