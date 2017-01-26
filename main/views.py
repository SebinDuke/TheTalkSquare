from django.shortcuts import render,get_object_or_404
from django.core.exceptions import ObjectDoesNotExist #This may be used instead of Users.DoesNotExist
from django.http import HttpResponse,HttpResponseRedirect
from django.views import generic
import re

from django.urls import reverse
#for older versoins of Django use:
#from django.core.urlresolvers import reverse


from .models import Users,Topic,Opinion
from main.forms import SignupForm,LoginForm,AddTopicForm,AddOpinionForm

def index(request):
    if request.session.has_key('user_id'):
        uid=request.session['user_id']
        try:
            li=Topic.objects.order_by('-pk')[:10]
            user=Users.objects.get(pk=uid)
            return render(request, 'Temp/logged.html',{'user_id':user,"list":li})
        except Users.DoesNotExist:
            return HttpResponse("UserName not found")
    else:
        return render(request, 'Temp/main.html')

def login(request):
    return render(request, 'Temp/login.html')
def signup(request):
    return render(request, 'Temp/signup.html')

def search(request):
    if request.method == 'POST':
        topic=AddTopicForm(request.POST)
        if topic.is_valid():

            #t=Topic.objects.get(topic_text=topic.cleaned_data.get('topic_text'))
            top_li = Topic.objects.all()
            li=[]
            for t in top_li:
                if re.search(topic.cleaned_data.get('topic_text'),t.topic_text,re.IGNORECASE):
                    li.append(t)

            return render(request, 'Temp/searchresults.html', {"list": li})
        else:
            return HttpResponse("Form not valid")
    else:
        return HttpResponse("not POST")


def register(request):
    if request.method == 'POST':
        signup=SignupForm(request.POST)
        if signup.is_valid():
            p=Users(user_name=signup.cleaned_data.get('username'),first_name=signup.cleaned_data.get('firstname'),last_name=signup.cleaned_data.get('lastname'),email=signup.cleaned_data.get('email'),pwd=signup.cleaned_data.get('pwd'))
            p.save()
    request.session['user_id'] = p.id
    return HttpResponseRedirect(reverse('main:index'))

def logInReq(request):
    if request.method == 'POST':
        log=LoginForm(request.POST)
        if log.is_valid():
            try:
                user=Users.objects.get(user_name=log.cleaned_data.get('username'),pwd=log.cleaned_data.get('pwd'))
                request.session['user_id'] = user.id
                return HttpResponseRedirect(reverse('main:index'))
            except Users.DoesNotExist:
                return HttpResponse("WRONG USERNAME OR PASSWORD")

        
"""
class LoggedIn(generic.DetailView):
	model = Users
	template_name = 'Temp/logged.html'
	context_object_name = 'user_id'
"""

def logout(request):
   try:
      del request.session['user_id']
   except:
      pass
   return HttpResponseRedirect(reverse('main:index'))

def addtopic(request):
    if request.method == 'POST':
        uid = request.session['user_id']
        topic=AddTopicForm(request.POST)
        if topic.is_valid():
            p=Topic(user=Users.objects.get(pk=uid),topic_text=topic.cleaned_data.get('topic_text'))
            p.save()
        else:
            return HttpResponse("Form not valid")
    else:
        return HttpResponse("not POST")
    return HttpResponseRedirect(reverse('main:index'))

def addopinion(request):
    if request.method == 'POST':
        uid = request.session['user_id']
        opinion=AddOpinionForm(request.POST)
        if opinion.is_valid():
            top=Topic.objects.get(pk=opinion.cleaned_data.get('topic'))
            p=Opinion(user=Users.objects.get(pk=uid),opinion_text=opinion.cleaned_data.get('opinion_text'),topic=top)
            p.save()
        else:
            return HttpResponse("Form not valid")
    else:
        return HttpResponse("not POST")
    return HttpResponseRedirect(reverse('main:topic', args=(opinion.cleaned_data.get('topic'))))

class TopicView(generic.DetailView):
	model = Topic
	template_name = 'Temp/Topic.html'
	context_object_name = 't'