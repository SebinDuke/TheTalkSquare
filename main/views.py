from django.shortcuts import render,get_object_or_404
from django.core.exceptions import ObjectDoesNotExist #This may be used instead of Users.DoesNotExist
from django.http import HttpResponse,HttpResponseRedirect
from django.views import generic
import re

from django.urls import reverse
#for older versoins of Django use:
#from django.core.urlresolvers import reverse


from .models import Topic,Opinion,Tag
from login.models import User
from main.forms import LoginForm,AddTopicForm,AddOpinionForm,SearchForm

def index(request):
    if request.session.has_key('user_id'):
        uid=request.session['user_id']
        try:
            li=Topic.objects.order_by('-pk')[:10]
            user=User.objects.get(pk=uid)
            return render(request, 'Temp/logged.html',{'user_id':user,"list":li})
        except User.DoesNotExist:
            return HttpResponse("UserName not found")
    else:
        return render(request, 'Temp/main.html')


def search(request):
    if request.method == 'POST':
        topic=SearchForm(request.POST)
        if topic.is_valid():

            #t=Topic.objects.get(topic_text=topic.cleaned_data.get('topic_text'))
            top_li = Topic.objects.all()
            li=[]
            for t in top_li:
                if re.search(topic.cleaned_data.get('topic_text'),t.topic_text,re.IGNORECASE):
                    li.append(t)
            if request.session.has_key('user_id'):
                uid = request.session['user_id']
                user = User.objects.get(pk=uid)
                return render(request, 'Temp/searchresults.html', {'user_id':user,"list": li})
            else:
                return render(request, 'Temp/searchresults.html', {"list": li})
        else:
            return HttpResponse("Form not valid")
    else:
        return HttpResponse("not POST")



"""
class LoggedIn(generic.DetailView):
	model = Users
	template_name = 'Temp/logged.html'
	context_object_name = 'user_id'
"""


def addtopic(request):
    if request.method == 'POST':
        uid = request.session['user_id']
        topic=AddTopicForm(request.POST)
        if topic.is_valid():
            tag = []
            tag_str=topic.cleaned_data.get('tag_text')
            topic_str = topic.cleaned_data.get('topic_text')
            topic_desc = topic.cleaned_data.get('topic_desc')
            tag = tag_str.split(',')
            p=Topic(user=User.objects.get(pk=uid),topic_text=topic_str,topic_desc=topic_desc)
            p.save()
            try:
                for i in tag:
                    q = Tag(topic=Topic.objects.get(topic_text=topic_str),
                            tag_name=i)
                    q.save()
            except:
                return HttpResponse("Topic already exists")
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
            p=Opinion(user=User.objects.get(pk=uid),opinion_text=opinion.cleaned_data.get('opinion_text'),topic=top)
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
