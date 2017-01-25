from django import forms

class SignupForm(forms.Form):
    username=forms.CharField(max_length = 80)
    firstname = forms.CharField(max_length=30)
    lastname = forms.CharField(max_length=30)
    email = forms.CharField(max_length=120)
    pwd= forms.CharField(max_length=80)

class LoginForm(forms.Form):
    username=forms.CharField(max_length = 80)
    pwd= forms.CharField(max_length=80)

class AddTopicForm(forms.Form):
    topic_text=forms.CharField(max_length = 250)

class AddOpinionForm(forms.Form):
    opinion_text=forms.CharField(max_length = 500)
    topic = forms.CharField(max_length = 5)