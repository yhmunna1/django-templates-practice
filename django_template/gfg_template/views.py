from django.shortcuts import render
import datetime
# Create your views here.

def home(request):
    d = {'author' : "R'ahim",'fullname': 'Md Rahim Uddin' , 'father': 'malek', 'age': 20, 'brother': '', 'birthday': datetime.datetime.now(), 'size': '123456789', 'courses': [
        {
            'id': 1,
            'name': "Python",
            'fee': 5000
        },
        {
            'id': 2,
            'name': "Django",
            'fee': 3000
        },
        {
            'id': 3,
            'name': "Javascript",
            'fee': 5000
        },
    ]}
    return render(request, 'home.html', d)

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

