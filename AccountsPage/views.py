from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def userlogin(request):
    return render(request , 'AccountsPage/login.html')

def userlogout(request):
    return render(request , 'AccountsPage/logout.html')

def usersignup(request):
    return render(request , 'AccountsPage/signup.html')
