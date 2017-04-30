from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect

from django.urls import reverse
#for older versoins of Django use:
#from django.core.urlresolvers import reverse

from .models import User
from .forms import SignupForm,LoginForm

def login(request):
    return render(request, 'Html/login.html')
def signup(request):
    return render(request, 'Html/signup.html')

def register(request):
    if request.method == 'POST':
        signup=SignupForm(request.POST)
        if signup.is_valid():
            p=User(user_name=signup.cleaned_data.get('username'),first_name=signup.cleaned_data.get('firstname'),last_name=signup.cleaned_data.get('lastname'),email=signup.cleaned_data.get('email'),pwd=signup.cleaned_data.get('pwd'))
            p.save()
    request.session['user_id'] = p.id
    return HttpResponseRedirect(reverse('main:index'))

def logInReq(request):
    if request.method == 'POST':
        log=LoginForm(request.POST)
        if log.is_valid():
            try:
                user=User.objects.get(user_name=log.cleaned_data.get('username'),pwd=log.cleaned_data.get('pwd'))
                request.session['user_id'] = user.id
                return HttpResponseRedirect(reverse('main:index'))
            except User.DoesNotExist:
                return HttpResponse("WRONG USERNAME OR PASSWORD")

def logout(request):
   try:
      del request.session['user_id']
   except:
      pass
   return HttpResponseRedirect(reverse('main:index'))